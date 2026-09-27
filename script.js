let currentSlide = 0;

const slides = presentation.slides;

const card = document.getElementById("card");
const heading = document.getElementById("heading");
const content = document.getElementById("content");
const sectionLabel = document.getElementById("sectionLabel");
const slideNumber = document.getElementById("slideNumber");
const counter = document.getElementById("counter");
const progressBar = document.getElementById("progressBar");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

function renderSlide() {
  const slide = slides[currentSlide];

  // Change section theme
  document.body.className = `theme-${slide.theme}`;

  // Update card content
  heading.textContent = slide.heading;
  content.innerHTML = slide.content;

  // Update slide information
  sectionLabel.textContent = slide.section;
  slideNumber.textContent = `Slide ${currentSlide + 1}`;
  counter.textContent = `Slide ${currentSlide + 1} / ${slides.length}`;

  // Update progress bar
  const progress = ((currentSlide + 1) / slides.length) * 100;
  progressBar.style.width = `${progress}%`;

  // Replay card animation
  card.classList.remove("pop");
  void card.offsetWidth;
  card.classList.add("pop");

  // Button states
  prevBtn.disabled = currentSlide === 0;

  nextBtn.disabled = currentSlide === slides.length - 1;

  nextBtn.textContent =
    currentSlide === slides.length - 1
      ? "Finished ✓"
      : "Next →";
}


// ===============================
// NEXT SLIDE
// ===============================

function nextSlide() {
  if (currentSlide < slides.length - 1) {
    currentSlide++;
    renderSlide();
  }
}


// ===============================
// PREVIOUS SLIDE
// ===============================

function previousSlide() {
  if (currentSlide > 0) {
    currentSlide--;
    renderSlide();
  }
}


// ===============================
// BUTTON EVENTS
// ===============================

nextBtn.addEventListener("click", nextSlide);

prevBtn.addEventListener("click", previousSlide);


// ===============================
// TAP CARD TO GO NEXT
// ===============================

card.addEventListener("click", (event) => {

  // Don't advance when interacting with special elements
  if (
    event.target.closest("a") ||
    event.target.closest("button") ||
    event.target.closest(".code")
  ) {
    return;
  }

  nextSlide();
});


// ===============================
// KEYBOARD CONTROLS
// ===============================

document.addEventListener("keydown", (event) => {

  // Next
  if (
    event.key === "ArrowRight" ||
    event.key === " " ||
    event.key === "Enter"
  ) {
    event.preventDefault();
    nextSlide();
  }

  // Previous
  if (event.key === "ArrowLeft") {
    event.preventDefault();
    previousSlide();
  }

  // First slide
  if (event.key === "Home") {
    currentSlide = 0;
    renderSlide();
  }

  // Last slide
  if (event.key === "End") {
    currentSlide = slides.length - 1;
    renderSlide();
  }
});


// ===============================
// MOBILE SWIPE
// ===============================

let touchStartX = 0;
let touchEndX = 0;

card.addEventListener(
  "touchstart",
  (event) => {
    touchStartX = event.changedTouches[0].screenX;
  },
  { passive: true }
);

card.addEventListener(
  "touchend",
  (event) => {

    touchEndX = event.changedTouches[0].screenX;

    const distance = touchEndX - touchStartX;

    // Swipe threshold
    if (Math.abs(distance) > 60) {

      // Swipe left → next
      if (distance < 0) {
        nextSlide();
      }

      // Swipe right → previous
      else {
        previousSlide();
      }
    }
  },
  { passive: true }
);


// ===============================
// INITIALIZE
// ===============================

renderSlide();
