function setupFaq() {
  const buttons = document.querySelectorAll(".faq__q");
  for (const btn of buttons) {
    btn.addEventListener("click", () => {
      const expanded = btn.getAttribute("aria-expanded") === "true";
      const item = btn.closest(".faq__item");
      const answer = item?.querySelector(".faq__a");
      if (!answer) return;

      btn.setAttribute("aria-expanded", expanded ? "false" : "true");
      answer.hidden = expanded;
    });
  }
}

function setupMobileMenu() {
  const menu = document.querySelector("[data-menu]");
  const openBtn = document.querySelector("[data-menu-btn]");
  const closeBtn = document.querySelector("[data-menu-close]");
  const backdrop = menu?.querySelector(".mobile-menu__backdrop");
  const links = menu?.querySelectorAll("a") ?? [];

  if (!menu || !openBtn || !closeBtn || !backdrop) return;

  const open = () => {
    menu.hidden = false;
    document.body.style.overflow = "hidden";
    closeBtn.focus();
  };

  const close = () => {
    menu.hidden = true;
    document.body.style.overflow = "";
    openBtn.focus();
  };

  openBtn.addEventListener("click", open);
  closeBtn.addEventListener("click", close);
  backdrop.addEventListener("click", close);
  for (const a of links) a.addEventListener("click", close);

  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !menu.hidden) close();
  });
}

function setupTestimonialSlider() {
  const root = document.querySelector("[data-testimonial]");
  const img = document.querySelector("[data-testimonial-img]");
  const prev = document.querySelector("[data-testimonial-prev]");
  const next = document.querySelector("[data-testimonial-next]");

  if (!root || !(img instanceof HTMLImageElement) || !prev || !next) return;

  const images = [
    "./pic/Pic1.png",
    "./pic/Pic2.png",
    "./pic/Pic3.png",
    "./pic/Pic4.png",
    "./pic/Pic5.png",
    "./pic/Pic6.png",
  ];

  let idx = Math.max(0, images.indexOf(img.getAttribute("src") ?? ""));
  const set = (n) => {
    idx = (n + images.length) % images.length;
    img.src = images[idx];
  };

  prev.addEventListener("click", () => set(idx - 1));
  next.addEventListener("click", () => set(idx + 1));

  window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") set(idx - 1);
    if (e.key === "ArrowRight") set(idx + 1);
  });
}

setupFaq();
setupMobileMenu();
setupTestimonialSlider();

