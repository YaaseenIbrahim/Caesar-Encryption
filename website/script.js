// Giving flashlight animation 
window.addEventListener('load', function () {
    document.querySelector(".overlay").classList.add("startup");

    setTimeout(() => {
        document.querySelector(".overlay").classList.remove("startup");
    }, 3000);
})


const topSection = document.querySelector("#topSection")
const windowHeight = (screen.height) - 110;
topSection.style.height =  windowHeight + "px"; 

// const DiamondSvg = Array.from(document.querySelectorAll(".diamondsvg"))
// const Options = document.querySelector(".options");
// window.onresize = window.onload = function () {

//     if (window.innerWidth < 510){
//         DiamondSvg.forEach(diamond => {
//             diamond.classList.add("scalarDiamond")
//             Options.classList.add("scalarOptions")
//             Options.classList.remove("options")

//         });

//     }
//     else{
//         DiamondSvg.forEach(diamond => {
//             diamond.classList.remove("scalarDiamond")
//             Options.classList.remove("scalarOptions")
//             Options.classList.add("options")

//         });

//     }
//     console.log(Options.classList)


// }