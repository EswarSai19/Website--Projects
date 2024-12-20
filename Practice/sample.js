let currentVideoIndex = 0;
const videoContainers = document.querySelectorAll(".ad-video-container");
const videos = document.querySelectorAll("video");

// Function to show the next video after the current one ends
function showNextVideo() {
  // Hide current video
  videoContainers[currentVideoIndex].classList.remove("active");

  // Move to the next video
  currentVideoIndex = (currentVideoIndex + 1) % videoContainers.length;
  console.log(currentVideoIndex);

  // Show the next video
  videoContainers[currentVideoIndex].classList.add("active");

  // Ensure that the video starts playing when switched
  videos[currentVideoIndex].play();
}

// Attach the 'ended' event listener to each video
videos.forEach((video, index) => {
  video.addEventListener("ended", () => {
    // Show next video when the current video ends
    showNextVideo();
  });
});

// Ensure the videos are loaded and ready to play
window.addEventListener("load", () => {
  // Preload videos
  videos.forEach((video) => {
    video.load();
  });
});

// Start the slideshow when the page is loaded
window.onload = function () {
  // Start the first video
  videos[0].play();

  // Start the image slideshow
  startImageSlideshow();
};

// Function to start the image slideshow for ad-boxes
function startImageSlideshow() {
  const adBoxes = document.querySelectorAll(".ad-box .ad-slideshow");

  adBoxes.forEach((adBox) => {
    // Skip the video box (first box)
    if (adBox.querySelector(".ad-video-container")) return;

    const images = adBox.querySelectorAll(".ad-image-container");
    let activeIndex = 0;

    // Set the first image to active initially
    images[activeIndex].classList.add("active");

    // Change the active image every 3 seconds (3000 milliseconds)
    setInterval(() => {
      images[activeIndex].classList.remove("active"); // Hide the current image
      activeIndex = (activeIndex + 1) % images.length; // Move to the next image (circular)
      images[activeIndex].classList.add("active"); // Show the next image
    }, 3000); // 3 seconds interval
  });
}
