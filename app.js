(() => {
  "use strict";

  /* ------------------------------------------------------------------
     Contact details — edit these values to update the whole site.
     whatsapp: international number, digits only (no +, spaces or dashes).
     socials: add { label, url, icon } to show the "Follow us" row.
     icons: instagram | facebook | tiktok | x | youtube | telegram
  ------------------------------------------------------------------ */
  const CONTACT = {
    whatsapp: "393761443811",
    email: "mdnexa9@gmail.com",
    socials: [],
  };

  const html = document.documentElement;
  const LANG_KEY = "mdnexa-lang";

  const TITLES = {
    ar: "MD Nexa — تطبيقات وألعاب أندرويد",
    en: "MD Nexa — Android apps & games",
  };
  const DESCRIPTIONS = {
    ar: "MD Nexa استوديو مستقل يبني تطبيقات وألعاب أندرويد: MD Work، MD Bolt Master وغيرهما. تصفّح كل المنتجات وتواصل معنا.",
    en: "MD Nexa is an independent Android studio building apps and games: MD Work, MD Bolt Master and more. Browse the catalogue and get in touch.",
  };

  /* ---------------- Language ---------------- */

  const translatable = Array.from(document.querySelectorAll("[data-en]"));
  translatable.forEach((el) => {
    if (!el.dataset.ar) el.dataset.ar = el.textContent;
  });

  const langNames = { ar: "العربية", en: "English" };

  function setLang(lang, persist) {
    const isEn = lang === "en";
    html.lang = isEn ? "en" : "ar";
    html.dir = isEn ? "ltr" : "rtl";

    translatable.forEach((el) => {
      el.textContent = isEn ? el.dataset.en : el.dataset.ar;
    });

    document.title = TITLES[isEn ? "en" : "ar"];
    const meta = document.querySelector('meta[name="description"]');
    if (meta) meta.setAttribute("content", DESCRIPTIONS[isEn ? "en" : "ar"]);

    const toggle = document.getElementById("langToggle");
    const label = document.getElementById("langToggleLabel");
    if (toggle) {
      toggle.setAttribute("aria-label", isEn ? "التبديل إلى العربية" : "Switch to English");
      toggle.setAttribute("title", isEn ? langNames.ar : langNames.en);
    }
    if (label) label.textContent = isEn ? "AR" : "EN";

    if (persist) {
      try { localStorage.setItem(LANG_KEY, isEn ? "en" : "ar"); } catch (e) { /* private mode */ }
    }
  }

  let savedLang = "ar";
  try { savedLang = localStorage.getItem(LANG_KEY) || "ar"; } catch (e) { /* ignore */ }
  if (savedLang === "en") setLang("en", false);

  const langToggle = document.getElementById("langToggle");
  if (langToggle) {
    langToggle.addEventListener("click", () => {
      setLang(html.lang === "ar" ? "en" : "ar", true);
    });
  }

  /* ---------------- Tabs ---------------- */

  const tabs = Array.from(document.querySelectorAll('[role="tab"]'));

  function selectTab(name, moveFocus) {
    tabs.forEach((tab) => {
      const active = tab.dataset.tab === name;
      tab.classList.toggle("is-active", active);
      tab.setAttribute("aria-selected", active ? "true" : "false");
      tab.tabIndex = active ? 0 : -1;

      const panel = document.getElementById(tab.getAttribute("aria-controls"));
      if (!panel) return;
      panel.hidden = !active;
      panel.classList.toggle("is-entering", active);
      if (active) {
        window.setTimeout(() => panel.classList.remove("is-entering"), 500);
      }
      if (active && moveFocus) panel.focus({ preventScroll: true });
    });
  }

  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => selectTab(tab.dataset.tab, false));
    tab.addEventListener("keydown", (event) => {
      if (event.key !== "ArrowRight" && event.key !== "ArrowLeft") return;
      event.preventDefault();
      const dir = event.key === "ArrowRight" ? 1 : -1;
      const next = tabs[(index + dir + tabs.length) % tabs.length];
      selectTab(next.dataset.tab, false);
      next.focus();
    });
  });

  // Counts on the tabs always match the cards actually on the page.
  document.querySelectorAll("[data-count-for]").forEach((badge) => {
    const panel = document.getElementById("panel-" + badge.dataset.countFor);
    if (panel) badge.textContent = panel.querySelectorAll(".card").length;
  });

  // Any link can point at a product section and pre-select its tab.
  document.querySelectorAll("[data-open-tab]").forEach((link) => {
    link.addEventListener("click", () => selectTab(link.dataset.openTab, false));
  });

  /* ---------------- Contact ---------------- */

  const whatsappLink = document.getElementById("whatsappLink");
  if (whatsappLink) {
    const digits = String(CONTACT.whatsapp || "").replace(/\D/g, "");
    if (digits) {
      whatsappLink.href = "https://wa.me/" + digits;
    } else {
      whatsappLink.hidden = true;
    }
  }

  const emailLinks = document.querySelectorAll('[href^="mailto:"]');
  emailLinks.forEach((link) => {
    if (CONTACT.email) link.href = "mailto:" + CONTACT.email;
  });

  const ICONS = {
    instagram: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3.2" y="3.2" width="17.6" height="17.6" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1" fill="currentColor" stroke="none"/></svg>',
    facebook: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.2h2.6l.4-3h-3V8.9c0-.9.3-1.5 1.6-1.5h1.5V4.7c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.9v3h2.5V21h3.1Z"/></svg>',
    tiktok: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 3h-2.9v11.6a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.2a5.6 5.6 0 1 0 4.7 5.5V8.5c1 .8 2.3 1.2 3.6 1.2V6.8a3.9 3.9 0 0 1-3.6-3.8Z"/></svg>',
    x: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 3h3.1l-6.8 7.8L21.5 21h-6.1l-4.4-5.8L5.9 21H2.8l7.2-8.2L2.5 3h6.2l4 5.3L17.5 3Zm-1.1 16.1h1.7L7.4 4.7H5.6l10.8 14.4Z"/></svg>',
    youtube: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2a2.7 2.7 0 0 0-1.9-1.9C18 4.9 12 4.9 12 4.9s-6 0-7.7.4a2.7 2.7 0 0 0-1.9 1.9A28 28 0 0 0 2 12c0 1.6.1 3.2.4 4.8a2.7 2.7 0 0 0 1.9 1.9c1.7.4 7.7.4 7.7.4s6 0 7.7-.4a2.7 2.7 0 0 0 1.9-1.9c.3-1.6.4-3.2.4-4.8s-.1-3.2-.4-4.8ZM10 15.2V8.8L15.5 12 10 15.2Z"/></svg>',
    telegram: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.2 4.3 2.9 11.4c-.9.3-.9 1.5.1 1.7l4.4 1.1 1.7 5.1c.2.7 1.1.9 1.6.3l2.4-2.6 4.5 3.3c.6.4 1.5.1 1.7-.6l3-14c.2-.8-.6-1.5-1.1-1.4ZM9.6 14.2l8.2-6.4-6.5 7.2-.2 3.1-1.5-3.9Z"/></svg>',
  };

  const socials = Array.isArray(CONTACT.socials) ? CONTACT.socials.filter((s) => s && s.url) : [];
  const socialBlock = document.getElementById("socialBlock");
  const socialList = document.getElementById("socialLinks");

  if (socialBlock && socialList && socials.length) {
    socials.forEach((social) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = social.url;
      link.target = "_blank";
      link.rel = "noopener";
      link.setAttribute("aria-label", social.label || "Social");
      link.setAttribute("title", social.label || "Social");
      link.innerHTML = ICONS[social.icon] || ICONS.instagram;
      item.appendChild(link);
      socialList.appendChild(item);
    });
    socialBlock.hidden = false;
  }

  /* ---------------- Coming-soon products ---------------- */

  const SOON_TEXT = {
    ar: "قريباً في بلاي ستور",
    en: "Coming soon on Google Play",
  };
  const toast = document.getElementById("toast");
  let toastTimer = 0;

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("is-visible");
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => toast.classList.remove("is-visible"), 2800);
  }

  document.querySelectorAll("[data-soon]").forEach((card) => {
    card.addEventListener("click", () => {
      showToast(SOON_TEXT[html.lang === "en" ? "en" : "ar"]);
    });
  });

  /* ---------------- Footer ---------------- */

  const year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());
})();
