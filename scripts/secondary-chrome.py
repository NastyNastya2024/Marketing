#!/usr/bin/env python3
"""Вставляет на второстепенные страницы хедер и меню как на главной."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V = "2026-05-11-1605"

HEADER_ROOT = """<header class="hero">
      <div class="hero-block">
        <div class="hero-block__top">
          <div class="hero-block__inner hero-block__inner--full">
            <nav class="nav nav--hero" aria-label="Основная навигация">
              <span></span>

              <div class="nav__right">
                <a class="pill pill--ghost" href="./index.html#contact">Контакты</a>
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
    HEADER_ROOT.replace('href="./index.html#contact"', 'href="../index.html#contact"')
    .replace('href="./cases.html"', 'href="../cases.html"')
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
              <a class="mobile-menu__links-span" href="./index.html#contact">Контакты</a>
            </div>
            <a class="pill pill--dark mobile-menu__cta" href="./index.html#contact">Обсудить проект</a>
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
    m = m.replace('href="./index.html#', 'href="../index.html#')
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


def render_header(template: str, h1: str) -> str:
    safe = h1.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return template.replace("{{PAGE_H1}}", safe)


def process_article(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = patch_articles_styles(html)
    h1 = desired_h1(html)
    header = render_header(HEADER_ARTICLE, h1)
    html = _ARTICLE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _SITE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _HERO_HDR_RE.sub(header + "\n    ", html, count=1)
    # Always replace menu/script to keep menu in sync
    html = _MENU_BLOCK_RE.sub("\n", html)
    html = _SCRIPT_RE.sub("\n", html)
    html = insert_before_body_close(html, "\n" + MENU_ARTICLE)
    path.write_text(html, encoding="utf-8")


def process_root_subpage(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = html.replace("./styles.css?v=2026-05-11-1500", f"./styles.css?v={V}")
    html = html.replace("./styles.css?v=2026-05-11-1530", f"./styles.css?v={V}")
    html = html.replace("./subpage.css?v=2026-05-11-1500", f"./subpage.css?v={V}")
    html = re.sub(r"(\.\/styles\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)
    html = re.sub(r"(\.\/subpage\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)

    h1 = desired_h1(html)
    header = render_header(HEADER_ROOT, h1)
    html = _SUB_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _SITE_HDR_RE.sub(header + "\n    ", html, count=1)
    html = _HERO_HDR_RE.sub(header + "\n    ", html, count=1)

    # Always replace menu/script to keep menu in sync
    html = _MENU_BLOCK_RE.sub("\n", html)
    html = _SCRIPT_RE.sub("\n", html)
    html = insert_before_body_close(html, "\n" + MENU_ROOT)
    # o-kompanii loads article.css
    html = html.replace("./articles/article.css?v=2026-05-11-1500", f"./articles/article.css?v={V}")
    html = re.sub(r"(\./articles/article\.css\?v=)[^\"'&]+", rf"\g<1>{V}", html)

    path.write_text(html, encoding="utf-8")


def main() -> None:
    for path in sorted((ROOT / "articles").glob("*.html")):
        process_article(path)

    for name in ("chto-my-delaem.html", "cases.html", "o-kompanii.html"):
        process_root_subpage(ROOT / name)


if __name__ == "__main__":
    main()
