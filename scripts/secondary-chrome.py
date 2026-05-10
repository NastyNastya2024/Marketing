#!/usr/bin/env python3
"""Вставляет на второстепенные страницы хедер и меню как на главной."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
V = "2026-05-11-1605"

HEADER_ROOT = """<header class="hero">
      <div class="hero-block">
        <div class="hero-block__top">
          <div class="hero-block__inner hero-block__inner--full">
            <nav class="nav nav--hero" aria-label="Основная навигация">
              <span></span>

              <div class="nav__right">
                <a class="pill pill--ghost" href="#contact">Контакты</a>
                <button class="icon-btn" type="button" aria-label="Меню" data-menu-btn>
                  <span class="icon-btn__bars" aria-hidden="true"></span>
                </button>
              </div>
            </nav>

            <div class="hero-block__top-grid"></div>
          </div>
        </div>

        <div class="hero-block__bottom">
          <div class="hero-block__inner hero-block__inner--full">
            <div class="hero-bottom">
              <div class="hero-bottom__left">
                <h1 class="h1">{{PAGE_H1}}</h1>
                <div class="hero-bottom__actions">
                  <a class="pill pill--light" href="./cases.html">Узнать больше</a>
                  <a class="icon-pill" href="./cases.html" aria-label="Открыть">
                    <span aria-hidden="true">›</span>
                  </a>
                </div>
              </div>

              <div class="hero-bottom__right">
                <article class="stat-card stat-card--dark">
                  <div class="stat-card__kpi">+130K</div>
                  <div class="stat-card__meta">
                    Методики внутренней работы и коучинговые пакеты для снижения стресса.
                  </div>
                  <a class="stat-card__link" href="./cases.html">Узнать больше</a>
                </article>

                <article class="stat-card stat-card--light">
                  <div class="stat-card__kpi">34%</div>
                  <div class="stat-card__meta">
                    Методики внутренней работы и коучинговые пакеты для снижения стресса.
                  </div>
                  <div class="stat-card__icons" aria-label="Действия">
                    <span class="dot-icon" aria-hidden="true"></span>
                    <span class="dot-icon" aria-hidden="true"></span>
                    <span class="dot-icon" aria-hidden="true"></span>
                    <span class="dot-icon" aria-hidden="true"></span>
                  </div>
                </article>

                <div class="social-rail" aria-label="Соцсети">
                  <a class="social" href="#" aria-label="Dribbble">◎</a>
                  <a class="social" href="#" aria-label="Behance">Be</a>
                  <a class="social" href="#" aria-label="LinkedIn">in</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>"""

HEADER_ARTICLE = (
    HEADER_ROOT.replace('href="./cases.html"', 'href="../cases.html"')
)

MENU_ROOT = """    <div class="mobile-menu" hidden data-menu aria-hidden="true">
      <div class="mobile-menu__row">
        <button class="mobile-menu__backdrop" type="button" aria-label="Закрыть меню"></button>

        <div class="mobile-menu__sheet" role="dialog" aria-modal="true" aria-label="Меню">
          <div class="mobile-menu__top">
            <button class="icon-btn" type="button" aria-label="Закрыть меню" data-menu-close>
              <span class="icon-btn__x" aria-hidden="true"></span>
            </button>
          </div>

          <div class="mobile-menu__scroll">
            <div class="menu-toc__title">Содержание</div>
            <nav class="menu-toc" aria-label="Содержание страницы">
              <ul class="menu-toc__list">
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead" href="./articles/starie-metody-prodaj.html"
                    >Старые методы продаж не работают</a>
                </li>
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead" href="./articles/novyj-cjm.html">Новый CJM</a>
                </li>
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead"
                    href="./articles/modernizacija-staryh-instrumentov.html"
                    >Модернизируем старые инструменты</a>
                  <ul class="menu-toc__sub">
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/instrument-site.html">Сайт</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/instrument-bazy-dannyh.html"
                        >Базы данных</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/instrument-soc-seti.html"
                        >Соц сети</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/instrument-zvonki.html"
                        >Звонки</a>
                    </li>
                  </ul>
                </li>
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead" href="./articles/ai-obzor.html">AI инструменты</a>
                  <ul class="menu-toc__sub">
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/ai-agenty.html">агенты</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/ai-skauty-social.html"
                        >скауты social</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/simulatory-mneniy-message.html"
                        >симуляторы мнений + message</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub"
                        href="./articles/ponimanie-klienta-prognoz.html"
                        >Понимание клиента и прогноз покупки</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub"
                        href="./articles/conversation-intelligence.html"
                        >conversation intelligence</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/case-factory.html"
                        >case factory</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/intent-routing.html"
                        >Intent routing</a>
                    </li>
                  </ul>
                </li>
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead"
                    href="./articles/sistema-metrik-instrumentov.html"
                    >Система метрик для каждого инструмента</a>
                </li>
                <li>
                  <a class="menu-toc__btn menu-toc__btn--lead" href="./articles/uslugi-obzor.html">Услуги</a>
                  <ul class="menu-toc__sub">
                    <li class="menu-toc__svc">
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/usluga-audit.html">Аудит</a>
                    </li>
                    <li class="menu-toc__svc">
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/usluga-strategiya.html"
                        >Стратегия</a>
                    </li>
                    <li class="menu-toc__svc">
                      <a class="menu-toc__btn menu-toc__btn--sub" href="./articles/usluga-vnedrenie.html"
                        >Внедрение</a>
                    </li>
                    <li>
                      <a class="menu-toc__btn menu-toc__btn--sub"
                        href="./articles/usluga-obratnoe-testirovanie.html"
                        >Обратное тестирование</a>
                    </li>
                  </ul>
                </li>
              </ul>
            </nav>
          </div>

          <div class="mobile-menu__foot">
            <div class="mobile-menu__links mobile-menu__links--wide">
              <a href="./chto-my-delaem.html">Что делаем</a>
              <a href="./cases.html">Кейсы</a>
              <a href="./o-kompanii.html">О компании</a>
              <a href="./index.html#faq">Вопросы</a>
              <a class="mobile-menu__links-span" href="#contact">Контакты</a>
            </div>
            <a class="pill pill--dark mobile-menu__cta" href="#contact">Обсудить проект</a>
          </div>
        </div>
      </div>
    </div>

    <script src="./script.js"></script>"""


def menu_for_articles(menu_root: str) -> str:
    m = menu_root.replace('href="./articles/', 'href="./')
    m = m.replace('href="./chto-my-delaem.html"', 'href="../chto-my-delaem.html"')
    m = m.replace('href="./cases.html"', 'href="../cases.html"')
    m = m.replace('href="./o-kompanii.html"', 'href="../o-kompanii.html"')
    # keep local contact anchor, but point FAQ to main
    m = m.replace('href="./index.html#faq"', 'href="../index.html#faq"')
    return m.replace("./script.js", "../script.js")


MENU_ARTICLE = menu_for_articles(MENU_ROOT)

_ARTICLE_HDR_RE = re.compile(
    r"<header\s+class=\"article-header\">.*?</header>\s*",
    re.DOTALL,
)

_SUB_HDR_RE = re.compile(
    r"<header\s+class=\"subpage-head\">.*?</header>\s*", re.DOTALL
)

_SITE_HDR_RE = re.compile(r"<header\s+class=\"site-header\">.*?</header>\s*", re.DOTALL)
_HERO_HDR_RE = re.compile(r"<header\s+class=\"hero\">.*?</header>\s*", re.DOTALL)

_MENU_BLOCK_RE = re.compile(
    r"\s*<div\s+class=\"mobile-menu\"[\s\S]*?</div>\s*</div>\s*</div>\s*</div>\s*",
    re.DOTALL,
)

_SCRIPT_RE = re.compile(r"\s*<script\s+src=\"(?:\./|\.\./)script\.js\"></script>\s*", re.DOTALL)
_TITLE_RE = re.compile(r"<title>(.*?)</title>", re.DOTALL | re.IGNORECASE)
_H1_RE = re.compile(r"<h1[^>]*>(.*?)</h1>", re.DOTALL | re.IGNORECASE)
_ARTICLE_SHEET_RE = re.compile(r"<article\s+class=\"article-sheet\"[\s\S]*?</article>", re.DOTALL)
_SUBPAGE_INTRO_RE = re.compile(r"<div\s+class=\"subpage-intro\"[\s\S]*?</div>", re.DOTALL)
_BODY_TAG_RE = re.compile(r"<body([^>]*)>", re.IGNORECASE)
_RELATED_RE = re.compile(r"\s*<section\s+class=\"more-articles\"[\s\S]*?</section>\s*", re.DOTALL)
_MAIN_CLOSE_RE = re.compile(r"</main>", re.IGNORECASE)
_CONTACT_SECTION_RE = re.compile(r"\s*<section[^>]*\bid=\"contact\"[\s\S]*?</section>\s*", re.DOTALL | re.IGNORECASE)
_ARTICLE_LEAD_RE = re.compile(r"(<p\s+class=\"article-lead\"[^>]*>[\s\S]*?</p>)", re.IGNORECASE)
_ARTICLE_PROSE_RE = re.compile(r"(<div\s+class=\"article-prose\"[^>]*>)([\s\S]*?)(</div>)", re.IGNORECASE)
_FIRST_P_RE = re.compile(r"<p>([\s\S]*?)</p>", re.IGNORECASE)
_BROKEN_BACKREF_RE = re.compile(r"\\1\\n\s*|\\1\s*")
_BODY_STYLE_RE = re.compile(r'(<body[^>]*\bstyle=")([^"]*)(")', re.IGNORECASE)
_BODY_OPEN_RE = re.compile(r"<body[^>]*>", re.IGNORECASE)
_ARTICLE_HERO_IMG_RE = re.compile(r"\s*<img[^>]*class=\"article-hero-img\"[^>]*>\s*", re.IGNORECASE)


def insert_before_body_close(html: str, block: str) -> str:
    parts = html.rsplit("</body>", 1)
    if len(parts) != 2:
        return html
    return f"{parts[0]}{block}\n  </body>{parts[1]}"


def patch_articles_styles(html: str) -> str:
    html = html.replace("../styles.css?v=2026-05-11-1400", f"../styles.css?v={V}")
    html = html.replace("../styles.css?v=2026-05-11-1500", f"../styles.css?v={V}")
    html = html.replace("../styles.css?v=2026-05-11-1530", f"../styles.css?v={V}")
    html = html.replace("./article.css?v=2026-05-11-1400", f"./article.css?v={V}")
    html = html.replace("./article.css?v=2026-05-11-1500", f"./article.css?v={V}")
    html = html.replace("./article.css?v=2026-05-11-1530", f"./article.css?v={V}")
    # ensure stylesheet version if generic
    html = re.sub(
        r'(\.\./styles\.css\?v=)[^"\'&]+',
        rf"\g<1>{V}",
        html,
    )
    html = re.sub(
        r"(\./article\.css\?v=)[^\"'&]+",
        rf"\g<1>{V}",
        html,
    )
    return html


def _strip_tags(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("&nbsp;", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def desired_h1(html: str) -> str:
    # 1) Prefer explicit page/article H1 in content
    m = _ARTICLE_SHEET_RE.search(html)
    if m:
        m2 = _H1_RE.search(m.group(0))
        if m2:
            return _strip_tags(m2.group(1))

    m = _SUBPAGE_INTRO_RE.search(html)
    if m:
        m2 = _H1_RE.search(m.group(0))
        if m2:
            return _strip_tags(m2.group(1))

    m = _H1_RE.search(html)
    if m:
        return _strip_tags(m.group(1))

    # 2) Fallback to document title before dash
    m = _TITLE_RE.search(html)
    if m:
        title = _strip_tags(m.group(1))
        for sep in ("—", "-", "|"):
            if sep in title:
                left = title.split(sep, 1)[0].strip()
                if left:
                    return left
        return title

    return "Маркетинг"

ARTICLES = [
    {
        "slug": "starie-metody-prodaj",
        "title": "Старые методы продаж не работают",
        "desc": "Почему линейные воронки дают дорогой шум и как перейти к реальному пути клиента.",
    },
    {
        "slug": "novyj-cjm",
        "title": "Новый CJM",
        "desc": "Customer Journey как живой инструмент: касания, решения и точки внимания под AI.",
    },
    {
        "slug": "modernizacija-staryh-instrumentov",
        "title": "Модернизируем старые инструменты",
        "desc": "Сайт, данные, соцсети и звонки — усиливаем то, во что уже вложены деньги.",
    },
    {
        "slug": "ai-obzor",
        "title": "AI инструменты",
        "desc": "Набор специализированных сценариев под путь клиента: от агентов до intent routing.",
    },
    {
        "slug": "sistema-metrik-instrumentov",
        "title": "Система метрик для каждого инструмента",
        "desc": "Свои KPI для канала и AI-блока: затраты → эффект → обучение без «общей цифры».",
    },
    {
        "slug": "uslugi-obzor",
        "title": "Услуги",
        "desc": "От аудита journey до внедрения и постоянной оптимизации инструментов по окупаемости.",
    },
]


def _slug_from_path(path: Path) -> str:
    return path.stem


def url_path(rel_path: str) -> str:
    # Ensure spaces and other chars are safe in HTML URLs
    return quote(rel_path, safe="/-_.")


def header_image_files() -> list[str]:
    header_dir = ROOT / "pic" / "header"
    if not header_dir.exists():
        return []
    files = []
    for p in header_dir.iterdir():
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}:
            files.append(p.name)
    return sorted(files)


_HEADER_FILES = header_image_files()


def header_img_for_key(key: str) -> str:
    # Deterministic choice by key; distributes across available images
    if not _HEADER_FILES:
        return "header/martin-martz-0rZdaEtmKnU-unsplash.jpg"
    idx = abs(hash(key)) % len(_HEADER_FILES)
    return f"header/{_HEADER_FILES[idx]}"


def related_section(current_slug: str, is_article_dir: bool) -> str:
    items = [a for a in ARTICLES if a["slug"] != current_slug]
    items = (items + ARTICLES)[:3]  # fallback if slug unknown

    if is_article_dir:
        href = lambda slug: f"./{slug}.html"
        all_href = "../articles.html"
        img_src = lambda slug: f"../pic/{url_path(header_img_for_key(slug))}"
    else:
        href = lambda slug: f"./articles/{slug}.html"
        all_href = "./articles.html"
        img_src = lambda slug: f"./pic/{url_path(header_img_for_key(slug))}"

    cards = []
    for a in items[:3]:
        cards.append(
            f"""          <a class="a-card" href="{href(a['slug'])}">
            <img class="a-card__img" src="{img_src(a['slug'])}" alt="" loading="lazy" />
            <h3 class="a-card__title">{a['title']}</h3>
            <p class="a-card__desc">{a['desc']}</p>
            <div class="a-card__cta">Узнать больше →</div>
          </a>"""
        )

    return f"""
      <section class="more-articles" aria-label="Ещё статьи">
        <div class="more-articles__head">
          <div>
            <h2 class="more-articles__title">Последние статьи и новости</h2>
            <div class="more-articles__hint">Следите за нашими достижениями и обновлениями</div>
          </div>
          <a class="more-articles__all" href="{all_href}">Все статьи →</a>
        </div>
        <div class="more-articles__grid">
{chr(10).join(cards)}
        </div>
      </section>
"""


FOOTER_ROOT = """\n      <section class="section section--light" id="contact">
        <div class="container">
          <div class="footer-card footer-card--embedded">
            <div class="footer-card__top" aria-hidden="true"></div>

            <div class="footer-card__bottom footer-card__bottom--contact">
              <form class="footer-form" action="#" method="post">
                <div class="form__grid">
                  <label class="field">
                    <span class="field__label">Имя</span>
                    <input class="field__input" name="name" type="text" placeholder="Ваше имя" />
                  </label>
                  <label class="field">
                    <span class="field__label">Email</span>
                    <input
                      class="field__input"
                      name="email"
                      type="email"
                      placeholder="you@company.com"
                    />
                  </label>
                  <label class="field">
                    <span class="field__label">Бюджет</span>
                    <input class="field__input" name="budget" type="text" placeholder="от $5k до $15k" />
                  </label>
                  <label class="field">
                    <span class="field__label">Компания</span>
                    <input class="field__input" name="company" type="text" placeholder="Название компании" />
                  </label>
                  <label class="field field--full">
                    <span class="field__label">Сообщение</span>
                    <textarea
                      class="field__input field__textarea"
                      name="message"
                      rows="5"
                      placeholder="Расскажите, что хотите сделать"
                    ></textarea>
                  </label>
                </div>

                <div class="form__actions">
                  <button class="pill pill--dark" type="submit">Отправить сообщение</button>
                  <span class="form__hint muted">Ответим в течение 1–2 рабочих дней.</span>
                </div>
              </form>

              <div class="footer-card__content">
                <div class="footer-card__left">
                  <div class="footer-card__title">Спасибо<br />за просмотр!</div>
                  <div class="footer-card__contacts">
                    <a class="footer-contact" href="mailto:anastkomarova@yandex.ru">
                      <span class="footer-contact__icon" aria-hidden="true">@</span>
                      <span>anastkomarova@yandex.ru</span>
                    </a>
                    <a class="footer-contact" href="#">
                      <span class="footer-contact__icon" aria-hidden="true">⌁</span>
                      <span>@anastasia_komarova1</span>
                    </a>
                  </div>
                </div>
              </div>

              <div class="footer-card__avatar" aria-label="Аватар">
                <img src="{{AVATAR_SRC}}" alt="" loading="lazy" />
              </div>
            </div>
          </div>
        </div>
      </section>\n"""

def render_footer(template: str, img_src: str) -> str:
    return template.replace("{{AVATAR_SRC}}", img_src)

FOOTER_ARTICLE_TEMPLATE = FOOTER_ROOT

def render_header(template: str, h1: str) -> str:
    safe = h1.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return template.replace("{{PAGE_H1}}", safe)


def ensure_secondary_body_class(html: str) -> str:
    m = _BODY_TAG_RE.search(html)
    if not m:
        return html
    attrs = m.group(1)
    if "page-secondary" in attrs:
        return html
    if "class=" in attrs:
        # append to existing class attribute
        html = re.sub(
            r'(<body[^>]*\bclass=")([^"]*)(")',
            lambda mm: mm.group(1) + (mm.group(2) + " page-secondary").strip() + mm.group(3),
            html,
            count=1,
            flags=re.IGNORECASE,
        )
        return html
    # add new class attr
    return html.replace(m.group(0), f'<body class="page-secondary"{attrs}>', 1)

def ensure_hero_bg(html: str, bg_url: str) -> str:
    # Use single quotes inside url() to keep HTML attribute valid
    decl = f"--hero-bg-img: url('{bg_url}')"
    m = _BODY_TAG_RE.search(html)
    if not m:
        return html

    if _BODY_STYLE_RE.search(html):
        def repl(mm: re.Match) -> str:
            style = mm.group(2).strip()
            if "--hero-bg-img" in style:
                # replace existing value (even if quotes were wrong)
                style = re.sub(r"--hero-bg-img\s*:\s*url\([^)]*\)\s*;?", decl + ";", style)
                style = re.sub(r"\s{2,}", " ", style).strip()
                return mm.group(1) + style + mm.group(3)
            if style and not style.endswith(";"):
                style += ";"
            style = (style + " " + decl + ";").strip()
            return mm.group(1) + style + mm.group(3)

        return _BODY_STYLE_RE.sub(repl, html, count=1)

    body_tag = m.group(0)
    return html.replace(body_tag, body_tag[:-1] + f' style="{decl};">', 1)

def normalize_secondary_body_tag(html: str, bg_url: str) -> str:
    # Rewrites <body ...> into a safe, consistent tag.
    m = _BODY_OPEN_RE.search(html)
    if not m:
        return html
    tag = m.group(0)
    cm = re.search(r'\bclass="([^"]*)"', tag, flags=re.IGNORECASE)
    classes = (cm.group(1) if cm else "").strip()
    if "page-secondary" not in classes.split():
        classes = (classes + " page-secondary").strip()
    new_tag = f'<body class="{classes}" style="--hero-bg-img: url(\'{bg_url}\');">'
    return html.replace(tag, new_tag, 1)


def sanitize_img_filename(name: str, fallback: str = "Picture6.png") -> str:
    name = (name or "").strip()
    if not (name.lower().endswith(".png") or name.lower().endswith(".jpg") or name.lower().endswith(".jpeg")):
        return fallback
    if any(bad in name for bad in ("<", ">", "\"", "'")):
        return fallback
    return name


def process_article(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = patch_articles_styles(html)
    html = ensure_secondary_body_class(html)
    slug = _slug_from_path(path)
    img = header_img_for_key(slug)
    html = normalize_secondary_body_tag(html, f"../pic/{url_path(img)}")
    h1 = desired_h1(html)
    header = render_header(HEADER_ARTICLE, h1)
    html = _ARTICLE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _SITE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _HERO_HDR_RE.sub(header + "\n    ", html, count=1)
    # Always replace menu/script to keep menu in sync
    html = _MENU_BLOCK_RE.sub("\n", html)
    html = _SCRIPT_RE.sub("\n", html)
    html = _RELATED_RE.sub("\n", html)
    html = _CONTACT_SECTION_RE.sub("\n", html)
    html = _ARTICLE_HERO_IMG_RE.sub("\n", html)
    # Fix accidental literal backref insertion from earlier run
    html = _BROKEN_BACKREF_RE.sub("", html)

    # Ensure a lead exists: if missing, promote first prose paragraph
    if "article-lead" not in html:
        m = _ARTICLE_PROSE_RE.search(html)
        if m:
            inner = m.group(2)
            p = _FIRST_P_RE.search(inner)
            if p:
                lead_text = p.group(1).strip()
                inner2 = inner[: p.start()] + inner[p.end() :]
                html = html[: m.start()] + m.group(1) + inner2 + m.group(3) + html[m.end() :]
                # insert lead right after article h1
                html = re.sub(
                    r'(<article\s+class="article-sheet"[^>]*>[\s\S]*?<h1[^>]*>[\s\S]*?</h1>)',
                    r'\1\n        <p class="article-lead">' + lead_text + "</p>",
                    html,
                    count=1,
                    flags=re.IGNORECASE,
                )

    # No inline image inside article body (per request)
    # Insert related cards before closing main
    if _MAIN_CLOSE_RE.search(html):
        html = _MAIN_CLOSE_RE.sub(related_section(_slug_from_path(path), True) + "    </main>", html, count=1)
    # Insert footer (contact) before menu
    footer = render_footer(FOOTER_ARTICLE_TEMPLATE, "../pic/Picture6.png")
    html = insert_before_body_close(html, footer)
    html = insert_before_body_close(html, "\n" + MENU_ARTICLE)
    path.write_text(html, encoding="utf-8")


def process_root_subpage(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = html.replace("./styles.css?v=2026-05-11-1500", f"./styles.css?v={V}")
    html = html.replace("./styles.css?v=2026-05-11-1530", f"./styles.css?v={V}")
    html = html.replace("./subpage.css?v=2026-05-11-1500", f"./subpage.css?v={V}")
    html = re.sub(r"(\.\/styles\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)
    html = re.sub(r"(\.\/subpage\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)

    html = ensure_secondary_body_class(html)
    img = header_img_for_key(path.stem)
    html = normalize_secondary_body_tag(html, f"./pic/{url_path(img)}")
    h1 = desired_h1(html)
    header = render_header(HEADER_ROOT, h1)
    html = _SUB_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _SITE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _HERO_HDR_RE.sub(header + "\n    ", html, count=1)

    # Always replace menu/script to keep menu in sync
    html = _MENU_BLOCK_RE.sub("\n", html)
    html = _SCRIPT_RE.sub("\n", html)
    html = _RELATED_RE.sub("\n", html)
    html = _CONTACT_SECTION_RE.sub("\n", html)
    if _MAIN_CLOSE_RE.search(html):
        html = _MAIN_CLOSE_RE.sub(related_section(_slug_from_path(path), False) + "    </main>", html, count=1)
    html = insert_before_body_close(html, render_footer(FOOTER_ROOT, "./pic/Picture6.png"))
    html = insert_before_body_close(html, "\n" + MENU_ROOT)
    # o-kompanii loads article.css
    html = html.replace("./articles/article.css?v=2026-05-11-1500", f"./articles/article.css?v={V}")
    html = re.sub(r"(\./articles/article\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)

    path.write_text(html, encoding="utf-8")


def main() -> None:
    for path in sorted((ROOT / "articles").glob("*.html")):
        process_article(path)

    for name in ("chto-my-delaem.html", "cases.html", "o-kompanii.html", "articles.html"):
        process_root_subpage(ROOT / name)


if __name__ == "__main__":
    main()
