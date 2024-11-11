// const API_KEY = "2bbf2df77929457daf5438180688406a";
// const url = "https://newsapi.org/v2/top-headlines?q=";

// // window.addEventListener("load", () => fetchNews("India"));

// function reload() {
//     window.location.reload();
// }

// async function fetchNews(query) {
//     const res = await fetch(`${url}${query}&apiKey=${API_KEY}`);
//     const data = await res.json();
//     bindData(data.articles);
// }

// function bindData(articles) {
//     const cardsContainer = document.getElementById("cards-container");
//     const newsCardTemplate = document.getElementById("template-news-card");

//     cardsContainer.innerHTML = "";

//     articles.forEach((article) => {
//         if (!article.urlToImage) return;
//         const cardClone = newsCardTemplate.content.cloneNode(true);
//         fillDataInCard(cardClone, article);
//         cardsContainer.appendChild(cardClone);
//     });
// }

// function fillDataInCard(cardClone, article) {
//     const newsImg = cardClone.querySelector("#news-img");
//     const newsTitle = cardClone.querySelector("#news-title");
//     const newsSource = cardClone.querySelector("#news-source");
//     const newsDesc = cardClone.querySelector("#news-desc");

//     newsImg.src = article.urlToImage;
//     newsTitle.innerHTML = article.title;
//     newsDesc.innerHTML = article.description;

//     const date = new Date(article.publishedAt).toLocaleString("en-US", {
//         timeZone: "Asia/Jakarta",
//     });

//     newsSource.innerHTML = `${article.source.name} · ${date}`;

//     cardClone.firstElementChild.addEventListener("click", () => {
//         window.open(article.url, "_blank");
//     });
// }

// let curSelectedNav = null;
// function onNavItemClick(id) {
//     fetchNews(id);
//     const navItem = document.getElementById(id);
//     curSelectedNav?.classList.remove("active");
//     curSelectedNav = navItem;
//     curSelectedNav.classList.add("active");
// }

// const searchButton = document.getElementById("search-button");
// const searchText = document.getElementById("search-text");

// searchButton.addEventListener("click", () => {
//     const query = searchText.value;
//     if (!query) return;
//     fetchNews(query);
//     curSelectedNav?.classList.remove("active");
//     curSelectedNav = null;
// });




// // New JS

// document.getElementById('signup-form')?.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const name = document.getElementById('signup-name').value;
//     const email = document.getElementById('signup-email').value;
//     const password = document.getElementById('signup-password').value;
//     const confirmPassword = document.getElementById('signup-confirm-password').value;

//     if (password !== confirmPassword) {
//         alert("Passwords do not match");
//         return;
//     }

//     // Here you would typically save the user data
//     // Redirect to preferences page
//     window.location.href = 'preferences.html';
// });

// document.getElementById('preferences-form')?.addEventListener('submit', (event) => {
//     event.preventDefault();
//     const preferences = Array.from(document.querySelectorAll('input[name="preference"]:checked'))
//                              .map(pref => pref.value);

//     // Save preferences, then redirect or update the interface
//     console.log("User preferences:", preferences);
//     alert("Preferences saved successfully!");
//     window.location.href = 'index.html'; // Redirect to homepage
// });





// // Django JS
