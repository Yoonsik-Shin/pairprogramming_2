const nav = document.querySelector("#navbarNav");
const navbar_toggler = document.querySelector(".navbar-toggler");

nav.addEventListener("click", () => {
    nav.classList.toggle("show");
    // if (navbar_toggler.getAttribute("aria-expanded") === "true") {
    //     navbar_toggler.setAttribute("aria-expanded", "false");
    }
});
