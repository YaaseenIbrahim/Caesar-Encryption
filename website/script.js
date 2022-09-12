
window.addEventListener('load', function () {
    document.querySelector(".overlay").classList.add("startup");

    setTimeout(() => {
        document.querySelector(".overlay").classList.remove("startup");
    }, 3000);
})

