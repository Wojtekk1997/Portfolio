document.addEventListener("DOMContentLoaded", function() {
    var hamburgerMenu = document.querySelector('.hamburger-menu');
    var mobileMenu = document.querySelector('.header-menu-mobile');

    hamburgerMenu.addEventListener('click', function() {
        this.classList.toggle('active');
        mobileMenu.classList.toggle('active');
    });
});