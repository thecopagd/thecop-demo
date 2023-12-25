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

const pastorsData = [
  {
    name: "Apostle Eric Nyamekye",
    role: "Chairman",
    bio: "He has been a very good chairman.",
    imageSrc: "/images/Aps.-Eric-Nyamekye.jpg",
  },
  {
    name: "Apostle Alexander Nana Yaw Kumi-Larbi",
    role: "General Secretary",
    bio: "He has been a very good general secretary.",
    imageSrc: "/images/Apostle_kumi.jpg",
  },
  {
    name: "Apostle Emmanuel Agyemang Bekoe",
    role: "International Missions Director",
    bio: "He has been a very good International Missions Director.",
    imageSrc: "/images/Aps-Emmanuel-Agyemang-Bekoe.jpg",
  },
  {
    name: "Apostle Ousmane Zabre ",
    role: " Executive Council Member",
    bio: "He has been a very good  Executive Council Member.",
    imageSrc: "/images/Aps.-Ousmane1-1-Excutive Council.jpg",
  },
  {
    name: "Apostle Samuel Osei Asante  ",
    role: " Executive Council Member",
    bio: "He has been a very good  Executive Council Member.",
    imageSrc: "/images/Aps.-S.O-Asante-1.jpg",
  },
  // Add more pastor data as needed
];

// Get the div where you want to display the data
const container = document.querySelector(".container");

// Loop through the data and create HTML elements for each pastor
pastorsData.forEach((pastor) => {
  // Create the leader_div element
  const leaderDiv = document.createElement("div");
  leaderDiv.classList.add("leader_div");

  // Create the image element
  const imageElement = document.createElement("img");
  imageElement.src = pastor.imageSrc;
  imageElement.alt = pastor.role;

  // Create the details div
  const detailsDiv = document.createElement("div");
  detailsDiv.classList.add("details");

  // Create the name element
  const nameElement = document.createElement("h3");
  nameElement.classList.add("name");
  nameElement.textContent = pastor.name;

  // Create the role element
  const roleElement = document.createElement("h4");
  roleElement.classList.add("role");
  roleElement.innerHTML = `<span>Role</span>: ${pastor.role}`;

  // Append the image, name, and role to the details div
  detailsDiv.appendChild(nameElement);
  detailsDiv.appendChild(roleElement);

  // Append the image and details div to the leader_div
  leaderDiv.appendChild(imageElement);
  leaderDiv.appendChild(detailsDiv);

  // Append the leader_div to the container
  container.appendChild(leaderDiv);
});






//Songs

        const songs = [
            {
                title: "Amazing Grace",
                lyrics: [
                    "Amazing grace! How sweet the sound",
                    "That saved a wretch like me!",
                    "I once was lost, but now am found;",
                    "Was blind, but now I see."
                ]
            },
            {
                title: "When Peace Like a River",
                lyrics: [
                    "When peace like a river, attendeth my way,",
                    "When sorrows like sea billows roll;",
                    "Whatever my lot, Thou hast taught me to say",
                    "It is well, it is well, with my soul."
                ]
            }
            // Add more songs similarly
        ];

        let currentSongIndex = 0;

        function navigateSong(direction) {
            if (direction === 'previous') {
                currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
            } else if (direction === 'next') {
                currentSongIndex = (currentSongIndex + 1) % songs.length;
            }

            displaySongs(); // Refresh the displayed songs
        }

        function displaySongs() {
            const container = document.querySelector('.songcontainer');

            // Clear existing content
            container.innerHTML = '';

            // Display the current song
            const currentSong = songs[currentSongIndex];
            const lyricsDiv = document.createElement('div');
            lyricsDiv.className = 'lyrics';
            lyricsDiv.innerHTML = `
                <h1>${currentSong.title}</h1>
                <p>${currentSong.lyrics.join('<br>')}</p>
            `;

            container.appendChild(lyricsDiv);

            // Add navigation buttons
            container.innerHTML += `
                <div class="pagination">
                    <button onclick="navigateSong('previous')">Previous Song</button>
                    <button onclick="navigateSong('next')">Next Song</button>
                </div>
            `;

            container.innerHTML += `
        <div class="comments">
            <h2>Comments</h2>
            <textarea id="commentInput" placeholder="Add your comment here..."></textarea>
            <button onclick="addComment()">Submit</button>
            <div id="commentDisplay"></div>
        </div>
    `;
        }
        displaySongs();

        function addComment() {
            const comment = document.getElementById('commentInput').value;
            const commentDisplay = document.getElementById('commentDisplay');

            if (comment.trim() !== '') {
                const commentElement = document.createElement('p');
                commentElement.textContent = comment;
                commentDisplay.appendChild(commentElement);
                document.getElementById('commentInput').value = '';
            }
        }



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

function openNav(a){
    document.getElementById(a).style.width = "250px";
    document.getElementById("nav-wrapper").style.display = "block"
}

function closeNav(a){
    document.getElementById(a).style.width = "0px"
    document.getElementById("nav-wrapper").style.display = "none"
}