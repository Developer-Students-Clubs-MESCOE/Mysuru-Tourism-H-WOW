const tl = new gsap.timeline();
tl.to(".navbar", {
  clipPath: "circle(150% at 45px 45px)"
}).to(
  ".item",
  {
    opacity: 1,
    y: 0,
    scale: 1,
    duration: 0.5,
    stagger: 0.25
  },
  "-=0.25"
);

tl.pause();

const navIcon = document.querySelector(".nav-icon");
navIcon.addEventListener("click", () => {
  if (tl.reversed() || tl.paused()) tl.play();
  else tl.reverse();
});
