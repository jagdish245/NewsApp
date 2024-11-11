document.addEventListener("DOMContentLoaded", () => {
    const preferenceItems = document.querySelectorAll(".preference-item");

    preferenceItems.forEach(item => {
        item.addEventListener("click", () => {
            item.classList.toggle("checked");

            // Toggle the checkbox state (optional, for backend use if needed)
            const checkbox = item.querySelector(".preference-checkbox");
            checkbox.checked = !checkbox.checked;
        });
    });
});
