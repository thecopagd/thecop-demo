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