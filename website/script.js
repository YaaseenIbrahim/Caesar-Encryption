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
topSection.style.height = windowHeight + "px";

// Mobile to PC switches
window.onload = window.onresize = function () {
    const wrapping = $(".wrapping")
    const KeyTextContainerHTML = "<div class=\"keyTextContainer flex-parent\"></div>"
    if (window.innerWidth <= 500 && wrapping.parent().is($(".keyTextContainer"))) {
        wrapping.unwrap()
        console.log($("[asymkey]").src)
        $("[asymkey]").attr("src", "website/Pics/key2-mobile.svg")
    }
    else if (window.innerWidth > 500 && wrapping.parent().is($(".options"))) {
        wrapping.slice(0, 2).wrapAll(KeyTextContainerHTML)
        wrapping.slice(2).wrapAll(KeyTextContainerHTML)
        $("[asymkey]").attr("src", "website/Pics/key2.svg")
    }
}