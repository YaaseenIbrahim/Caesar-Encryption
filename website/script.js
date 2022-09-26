// Giving flashlight animation 
window.addEventListener('load', function () {
    document.querySelector(".overlay").classList.add("startup");

    setTimeout(() => {
        document.querySelector(".overlay").classList.remove("startup");
    }, 3000);
})


const topSection = document.querySelector("#topSection")
const TopToolbars = window.outerHeight - window.innerHeight
const windowHeight = (window.screen.availHeight) - TopToolbars;
topSection.style.height =  windowHeight + "px"; 