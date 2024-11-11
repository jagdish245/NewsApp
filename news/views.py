import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User, Preference  # Assuming you have a custom User model with name, email, and password fields
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, authenticate, logout

API_KEY = "2bbf2df77929457daf5438180688406a"
BASE_URL = "https://newsapi.org/v2/everything"


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Check for matching passwords
        if password != confirm_password:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email is already registered'}, status=400)

        # Create new user
        user = User(name=name, email=email, password=make_password(password))
        user.save()

        # Authenticate and log in the user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('preferences') 
        return JsonResponse({'message': 'User created successfully'}, status=201)
    
    return render(request, 'news/signup.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if user exists and authenticate
        if User.objects.filter(email=email).exists():
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'news/login.html', {'error': 'Invalid credentials'})
        else:
            return render(request, 'news/login.html', {'error': 'User does not exist'})

    return render(request, 'news/login.html')


def index(request):
    # Retrieve the user's preferred categories from the database
    if request.user.is_authenticated:
        user_preferences = Preference.objects.filter(user=request.user).values_list('category', flat=True)
        
    else:
       user_preferences = None

    # Prepare parameters for API request
    params = {
        'language': 'en',
        'apiKey': API_KEY,
    }
        

     # If user has preferences, fetch news only for those categories
    news_data = []
    if user_preferences:
        for category in user_preferences:
            params['q'] = category
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                news_data.extend(response.json().get('articles', []))
    else:
         # Default to some news if no preferences are set
        params['q'] = 'India'  # Or another default category of your choice
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            news_data = response.json().get('articles', [])

    return render(request, 'news/index.html', {'news_data': news_data})


def preferences(request):
    if request.method == 'POST':
        categories = request.POST.getlist('preferences')
        
        if categories:
            for category in categories:
                preference, created = Preference.objects.get_or_create(
                    user=request.user, 
                    category=category
                )
        
        return redirect('index')


    return render(request, 'news/preferences.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('index')
