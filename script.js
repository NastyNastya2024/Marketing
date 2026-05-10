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
    menu.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    closeBtn.focus();
  };

  const close = () => {
    menu.hidden = true;
    menu.setAttribute("aria-hidden", "true");
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

function setupCasesSlider() {
  const root = document.querySelector("[data-case-slider]");
  const img = document.querySelector("[data-case-img]");
  const prev = document.querySelector("[data-case-prev]");
  const next = document.querySelector("[data-case-next]");
  const titleEl = document.querySelector("[data-case-title]");
  const descEl = document.querySelector("[data-case-desc]");
  const linkEl = document.querySelector("[data-case-link]");

  if (
    !root ||
    !(img instanceof HTMLImageElement) ||
    !prev ||
    !next ||
    !titleEl ||
    !descEl ||
    !(linkEl instanceof HTMLAnchorElement)
  ) {
    return;
  }

  const slides = [
    {
      img: "./pic/Pic1.png",
      imgAlt: "Иллюстрация кейса: B2B-логистика",
      title: "Кейс 1. B2B-логистика: как перестали терять лидов из Telegram-чатов",
      desc:
        "Social Scout, Intent Routing и AI‑агент: лиды из Telegram, доля голоса в чатах и CAC — метрики и отладка на странице кейса.",
      href: "./cases.html#case-1",
    },
    {
      img: "./pic/Pic2.png",
      imgAlt: "Иллюстрация кейса: SaaS CRM",
      title: "Кейс 2. SaaS (CRM для МСП): сделки на этапе сравнения",
      desc:
        "Intent Routing, AI‑агент на типовых вопросах и Case Factory: рост регистрации, меньше рутины у менеджеров, открытия КП.",
      href: "./cases.html#case-2",
    },
    {
      img: "./pic/Pic3.png",
      imgAlt: "Иллюстрация кейса: FinTech",
      title: "Кейс 3. FinTech — платёжный агрегатор для e‑commerce",
      desc:
        "Онбординг и отток: Conversation Intelligence, типовые вопросы по API и документации — что поменяли за первые недели.",
      href: "./cases.html#case-3",
    },
    {
      img: "./pic/Pic4.png",
      imgAlt: "Иллюстрация кейса: EdTech",
      title: "Кейс 4. EdTech — корпоративная онлайн-школа",
      desc:
        "Маршрутизация запросов, автокурсы под роль и метрики вовлечённости — как сократили нагрузку на методистов.",
      href: "./cases.html#case-4",
    },
    {
      img: "./pic/Pic5.png",
      imgAlt: "Иллюстрация кейса: retail",
      title: "Кейс 5. Retail — сеть «товары для дома»",
      desc:
        "Intent Routing в чате, AI по каталогу и прогноз возврата: вопросы о размере и цвете без очереди, меньше возвратов.",
      href: "./cases.html#case-5",
    },
  ];

  let idx = slides.findIndex((s) => s.img === (img.getAttribute("src") ?? ""));
  if (idx < 0) idx = 0;

  const apply = (n) => {
    idx = (n + slides.length) % slides.length;
    const s = slides[idx];
    img.src = s.img;
    img.alt = s.imgAlt;
    titleEl.textContent = s.title;
    descEl.textContent = s.desc;
    linkEl.href = s.href;
  };

  prev.addEventListener("click", () => apply(idx - 1));
  next.addEventListener("click", () => apply(idx + 1));

  window.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") apply(idx - 1);
    if (e.key === "ArrowRight") apply(idx + 1);
  });

  apply(idx);
}

setupFaq();
setupMobileMenu();
setupCasesSlider();

