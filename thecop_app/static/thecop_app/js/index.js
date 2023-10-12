const menuBtn = document.querySelector(".menu-btn");
const navigationItems = document.querySelector(".navigation-items");
const navigation = document.querySelector(".navigation");

window.addEventListener("scroll", () => {
  const header = document.querySelector(".header");

  if (window.scrollY > 80) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
});

window.addEventListener("scroll", () => {
  const header = document.querySelector(".header");

  if (window.scrollY > 180) {
    header.classList.add("active");
  } else {
    header.classList.remove("active");
  }
});

const dropdownItem = document.querySelectorAll(".dropdown-item");
console.log(dropdownItem);
dropdownItem.forEach((item) => {
  item.addEventListener("click", () => {
    console.log("I have been clicked");
  });
});



const countingEl = document.querySelectorAll(".room");

countingEl.forEach((countingEl) => {
  countingEl.innerText = "0";
  increaseCount();
  function increaseCount() {
    let currentNum = +countingEl.innerText;
    const dataCeil = countingEl.getAttribute("data-ceil");
    const increase = dataCeil / 30;
    currentNum = Math.ceil(increase + currentNum);

    if (currentNum < dataCeil) {
      countingEl.innerText = currentNum;
      setTimeout(increaseCount, 80);
    } else countingEl.innerText = dataCeil;
  }
});

const btns = document.querySelectorAll(".nav-btn");
const slide = document.querySelectorAll(".video-slider");
const content = document.querySelectorAll(".content");

var sliderNav = function (manual) {
  btns.forEach((btn) => {
    btn.classList.remove("active");
  });

  content.forEach((content) => {
    content.classList.remove("active");
  });

  slide.forEach((slide) => {
    slide.classList.remove("active");
  });
  slide[manual].classList.add("active");
  btns[manual].classList.add("active");
  content[manual].classList.add("active");
};

btns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    sliderNav(i);
  });
});


function openNav(a){
    document.getElementById(a).style.width = "250px";
    document.getElementById("nav-wrapper").style.display = "block"
}

function closeNav(a){
    document.getElementById(a).style.width = "0px"
    document.getElementById("nav-wrapper").style.display = "none"
}