const menuBtn = document.querySelector(".menu-btn")
const navigationItems = document.querySelector(".navigation-items")
const navigation = document.querySelector(".navigation")

window.addEventListener('scroll', () => {
    const header = document.querySelector(".header")

    if (window.scrollY > 80) {
        header.classList.add("active")
    } else {
        header.classList.remove("active")
    }
})

// var swiperPopular = new Swiper(".popular_container", {
//     spaceBetween:32,
//     grapCursor: true,
//     centeredSlides: true,
//     slidesPerView: 'auto',
//     loop: true,
//     navigation: {
//       nextEl: ".swiper-button-next",
//       prevEl: ".swiper-button-prev",
//     },
//   });
 

// navigation.addEventListener('click',()=> {
//     menuBtn.classList.toggle("active")

//     navigation.classList.toggle("remove")
// })


menuBtn.addEventListener("click", () => {
    navigationItems.classList.toggle("active")
    navigation.classList.toggle("active")
    menuBtn.classList.toggle("active")

   
    navigation.addEventListener("click", () => {
        navigationItems.classList.toggle("active")
        navigation.classList.toggle("active")
        menuBtn.classList.toggle("active")
    
        const navLink = document.querySelectorAll(".nav-item")
    
        navLink.forEach(link => {
            link.addEventListener("click", () => {
                // link.style.color = '#F0DB4F'
                navigationItems.classList.remove("active")
                navigation.classList.remove("active")
                menuBtn.classList.remove("active")
            })
        })
    })
})



const countingEl = document.querySelectorAll(".room")

countingEl.forEach(countingEl=>{
    countingEl.innerText = "0"
    increaseCount()
    function increaseCount(){
        let currentNum = +countingEl.innerText
        const dataCeil = countingEl.getAttribute("data-ceil");
        const increase = dataCeil/10
        currentNum = Math.ceil(increase + currentNum)
       
        
        
        if(currentNum < dataCeil){
            countingEl.innerText = currentNum 
            setTimeout(increaseCount, 80)
        }
        else(countingEl.innerText = dataCeil)
     
   
    }

})


const btns = document.querySelectorAll(".nav-btn")
const slide = document.querySelectorAll(".video-slider")
const content = document.querySelectorAll(".content")


var sliderNav = function(manual) {

    btns.forEach((btn) => {
    btn.classList.remove("active")
    
});

content.forEach((content) => {
    content.classList.remove("active")
    
});

slide.forEach((slide) => {
    slide.classList.remove("active")
    
});
    slide[manual].classList.add("active") 
    btns[manual].classList.add("active")  
    content[manual].classList.add("active")
}

btns.forEach((btn,i) => {
    btn.addEventListener('click',() =>{
        sliderNav(i);
    });
    
});

