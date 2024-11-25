// header
let header = document.querySelector(".header");
let header__menu = document.querySelector(".header__menu");

function addOpen() {
  header__menu.classList.toggle("open");
}

window.addEventListener("scroll", function () {
  header.classList.toggle("sticky", window.scrollY > 0);
});

// splide Js Active Hacathons
const mySlider = new Splide("#mySliderActive", {
  type: "loop",
  drag: "free",
  perPage: 2,
  gap: "30px",
  arrows: true,
  pagination: false,
  autoplay: true,
  interval: 3000,
  pauseOnHover: true,
  breakpoints: {
    1200: {
      perPage: 1,
    },
    768: {
      arrows: false,
      pagination: true,
    },
  },
});

mySlider.mount();

// splide Js Upcoming Hacathons
new Splide("#mySliderUpcoming", {
  type: "loop",
  drag: "free",
  perPage: 2,
  gap: "30px",
  arrows: true,
  pagination: false,
  autoplay: true,
  interval: 3000,
  pauseOnHover: true,
  breakpoints: {
    1200: {
      perPage: 1,
    },
    768: {
      arrows: false,
      pagination: true,
    },
  },
}).mount();

// splide Js Past Hacathons
new Splide("#mySliderPast", {
  type: "loop",
  drag: "free",
  perPage: 2,
  gap: "30px",
  arrows: true,
  pagination: false,
  autoplay: true,
  interval: 3000,
  pauseOnHover: true,
  breakpoints: {
    1200: {
      perPage: 1,
    },
    768: {
      arrows: false,
      pagination: true,
    },
  },
}).mount();

// =================================================================================================
