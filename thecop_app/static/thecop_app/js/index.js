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

// var swiper = new Swiper('.swiper', {
//     // Optional parameters
//     direction: 'vertical',
//     loop: true,

//     // If we need pagination
//     pagination: {
//       el: '.swiper-pagination',
//     },

//     // Navigation arrows
//     navigation: {
//       nextEl: '.swiper-button-next',
//       prevEl: '.swiper-button-prev',
//     },

//     // And if we need scrollbar
//     scrollbar: {
//       el: '.swiper-scrollbar',
//     },
//   });

menuBtn.addEventListener("click", () => {
  navigationItems.classList.toggle("active");
  navigation.classList.toggle("active");
  menuBtn.classList.toggle("active");

  navigation.addEventListener("click", () => {
    navigationItems.classList.toggle("active");
    navigation.classList.toggle("active");
    menuBtn.classList.toggle("active");

    const navLink = document.querySelectorAll(".nav-item");
    console.log(navLink);

    navLink.forEach((link) => {
      link.addEventListener("click", () => {
        // link.style.color = '#F0DB4F'
        navigationItems.classList.remove("active");
        navigation.classList.remove("active");
        menuBtn.classList.remove("active");
      });
    });
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

//PASTORS DIV MAP

// const leaderDiv = document.querySelectorAll(".leader_div")
//console.log(leaderDiv);

// const pastorsData = [
//     {
//       name: "Apostle Eric Nyamekye",
//       role: "Chairman",
//       bio: "He has been a very good chairman."
//     }
//   ]

//   const data = pastorsData.map((data)=> {
//     return data
//   })

//   console.log(data);








//Songs





//Gallery

    // Open Modal Function
    function openModal(imageSrc, description) {
      document.getElementById('modalImage').src = imageSrc;
      document.getElementById('modalDescription').textContent = description;
      document.getElementById('myModal').style.display = 'block';
  }


// Close modal function
function closeModal() {
  document.getElementById('myModal').style.display = 'none';
}

// Event listener to close modal on outside click
document.getElementById('myModal').addEventListener('click', function(event) {
  if (event.target === this) {
      closeModal();
  }
});


    // Close Modal on outside click
    window.onclick = function(event) {
        if (event.target == document.getElementById('myModal')) {
            closeModal();
        }
    }

