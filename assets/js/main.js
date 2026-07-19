/* ==========================================================================
   VOLTAGE — main.js
   Handles: Header injection, Footer injection, Theme toggle, RTL toggle,
   Active navigation, Mobile menu, Search, Back-to-top, Icon counts.
   ========================================================================== */

(function () {
  "use strict";

  /* ---------------- Path helper: works from root or any sub-depth ---------------- */
  const ROOT = (function () {
    // All pages live flat in project root, so relative paths are simply "./"
    return "";
  })();

  /* ---------------- SVG ICON LIBRARY (inline, no external deps) ---------------- */
  const ICONS = {
    search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>',
    heart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>',
    cart: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2.05 2.05h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 2-1.58l1.65-7.42H5.12"/></svg>',
    sun: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>',
    moon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>',
    globe: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20 15 15 0 0 1 0-20Z"/></svg>',
    menu: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6h16M4 12h16M4 18h16"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
    chevronDown: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    chevronRight: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon-arrow"><path d="m9 18 6-6-6-6"/></svg>',
    arrowUp: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
    user: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    mapPin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>',
    phoneIcon: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92Z"/></svg>',
    mail: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    clock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
  };
  window.VOLTAGE_ICONS = ICONS;

  /* ---------------- NAVIGATION DATA ---------------- */
  const NAV = [
    {
      label: "Home",
      href: "index.html",
      active: ["index.html","home-2.html"],
      dropdown: [
        ["Home 1", "index.html"],
        ["Home 2", "home-2.html"]
      ]
    },
    {
      label: "Shop", href: "categories.html", mega: true, active: ["categories.html","laptops.html","smartphones.html","headphones.html","smartwatches.html","gaming.html","accessories.html"],
      columns: [
        { title: "Computing", links: [["Laptops","laptops.html"]] },
        { title: "Accessories", links: [["Accessories","accessories.html"]] },
        { title: "Mobile", links: [["Smartphones","smartphones.html"],["Smartwatches","smartwatches.html"]] },
        { title: "Audio & Gaming", links: [["Headphones","headphones.html"],["Gaming Zone","gaming.html"]] }
      ]
    },
    { label: "Deals", href: "weekly-deals.html", active: ["weekly-deals.html"] },
    { label: "Compare", href: "product-comparison.html", active: ["product-comparison.html"] },
    { label: "Brands", href: "brands.html", active: ["brands.html"] },
    { label: "Bulk Orders", href: "bulk-orders.html", active: ["bulk-orders.html"] },
    { label: "Stores", href: "store-locator.html", active: ["store-locator.html"] },
    { label: "About", href: "about.html", active: ["about.html"] },
    { label: "Contact", href: "contact.html", active: ["contact.html"] },
  ];

  function currentPage() {
    const path = window.location.pathname.split("/").pop() || "index.html";
    return path;
  }

  /* ---------------- HEADER TEMPLATE ---------------- */
  function buildMegaMenu(cols) {
    return `<div class="mega-menu"><div class="container mega-menu__grid" style="grid-template-columns: repeat(4, 1fr);">
      ${cols.map(c => `<div class="mega-menu__col"><h4>${c.title}</h4>${c.links.map(l => `<a href="${l[1]}">${l[0]}</a>`).join("")}</div>`).join("")}
    </div></div>`;
  }

  function buildHeader() {
    const cur = currentPage();
    const navItems = NAV.map(item => {
      const isActive = item.active.includes(cur);
      if (item.dropdown) {
        const dropMenu = `<ul class="dropdown-menu">
          ${item.dropdown.map(d => `<li><a href="${d[1]}" class="${cur === d[1] ? 'active' : ''}">${d[0]}</a></li>`).join("")}
        </ul>`;
        return `<li class="has-dropdown ${isActive ? "active" : ""}">
          <a href="${item.href}">${item.label} ${ICONS.chevronDown}</a>
          ${dropMenu}
        </li>`;
      }
      const mega = item.mega ? buildMegaMenu(item.columns) : "";
      return `<li class="${isActive ? "active" : ""} ${item.mega ? "has-mega" : ""}">
        <a href="${item.href}">${item.label}${item.mega ? ICONS.chevronDown : ""}</a>
        ${mega}
      </li>`;
    }).join("");

    return `
    <div class="utility-bar">
      <div class="container">
        <div class="utility-bar__msg">${ICONS.mapPin}<span>Free shipping on orders over $99</span></div>
        <div class="utility-bar__links">
          <a href="store-locator.html">Store Locator</a>
          <a href="bulk-orders.html">Corporate Orders</a>
          <a href="contact.html">Track Order</a>
        </div>
      </div>
    </div>
    <div class="spec-strip" aria-hidden="true">
      <div class="spec-strip__track" id="specStripTrack"></div>
    </div>
    <div class="site-header">
      <div class="container">
        <a href="index.html" class="brand-logo" aria-label="Voltage home">
          <span class="brand-logo__mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/></svg></span>
          <span class="brand-logo__text">Volt<span>age</span></span>
        </a>
        <nav class="main-nav" aria-label="Primary">
          <ul>${navItems}</ul>
        </nav>
        <div class="header-actions">
          <a href="login.html" class="icon-btn" aria-label="Account">${ICONS.user}</a>
          <a href="#" class="icon-btn" aria-label="Cart">${ICONS.cart}<span class="icon-btn__count">2</span></a>
          <button class="icon-btn rtl-toggle" id="rtlToggle" aria-label="Toggle right-to-left layout">${ICONS.globe}</button>
          <button class="icon-btn theme-toggle" id="themeToggle" aria-label="Toggle dark mode">
            <span class="icon-sun">${ICONS.sun}</span><span class="icon-moon">${ICONS.moon}</span>
          </button>
          <a href="login.html" class="btn btn-outline btn-sm header-cta" style="border-radius:var(--radius-pill);">Sign In</a>
          <button class="menu-toggle" id="menuToggle" aria-label="Open menu" aria-expanded="false">${ICONS.menu}</button>
        </div>
      </div>
    </div>
    <div class="nav-overlay" id="navOverlay"></div>
    <aside class="mobile-nav" id="mobileNav" aria-label="Mobile navigation">
      <div class="mobile-nav__head">
        <span class="brand-logo__text">Volt<span style="color:var(--c-primary)">age</span></span>
        <button class="mobile-nav__close" id="mobileNavClose" aria-label="Close menu">${ICONS.close}</button>
      </div>
      <div class="mobile-nav__body">
        <ul>
          ${NAV.map(item => {
            const isActive = item.active.includes(cur);
            if (item.dropdown) {
              return `<li class="${isActive ? 'active' : ''}">
                <button class="mobile-accordion-toggle">${item.label} ${ICONS.chevronDown}</button>
                <div class="mobile-submenu">${item.dropdown.map(d => `<a href="${d[1]}">${d[0]}</a>`).join("")}</div>
              </li>`;
            }
            if (item.mega) {
              const links = item.columns.flatMap(c => c.links);
              return `<li class="${isActive ? 'active' : ''}">
                <button class="mobile-accordion-toggle">${item.label} ${ICONS.chevronDown}</button>
                <div class="mobile-submenu">${links.map(l => `<a href="${l[1]}">${l[0]}</a>`).join("")}</div>
              </li>`;
            }
            return `<li class="${isActive ? 'active' : ''}"><a href="${item.href}">${item.label}</a></li>`;
          }).join("")}
        </ul>
      </div>
      <div class="mobile-nav__foot">
        <a href="login.html" class="btn btn-primary btn-block">Sign In / Register</a>
        <div class="d-flex gap-3 justify-center">
          <button class="icon-btn rtl-toggle" data-sync="rtlToggle" aria-label="Toggle RTL">${ICONS.globe}</button>
          <button class="icon-btn theme-toggle" data-sync="themeToggle" aria-label="Toggle dark mode"><span class="icon-sun">${ICONS.sun}</span><span class="icon-moon">${ICONS.moon}</span></button>
        </div>
      </div>
    </aside>`;
  }

  /* ---------------- FOOTER TEMPLATE ---------------- */
  function buildFooter() {
    const year = new Date().getFullYear();
    return `
    <div class="footer-top">
      <div class="container footer-grid">
        <div class="footer-col footer-brand">
          <a href="index.html" class="brand-logo" style="margin-bottom:14px;">
            <span class="brand-logo__mark"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8Z"/></svg></span>
            <span class="brand-logo__text" style="color:#fff;">Volt<span>age</span></span>
          </a>
          <p>Premium electronics and next-generation gadgets, curated for people who expect more from their technology.</p>
          <div class="footer-social">
            <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg></a>
            <a href="#" aria-label="X / Twitter"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h3l-7.5 8.6L22 22h-6.8l-5.3-6.9L4 22H1l8-9.2L2 2h7l4.8 6.3L18 2Z"/></svg></a>
            <a href="#" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 8.5a4 4 0 0 0-2.8-2.8C17 5 12 5 12 5s-5 0-7.2.7A4 4 0 0 0 2 8.5 41 41 0 0 0 2 12a41 41 0 0 0 0 3.5 4 4 0 0 0 2.8 2.8C7 19 12 19 12 19s5 0 7.2-.7A4 4 0 0 0 22 15.5 41 41 0 0 0 22 12a41 41 0 0 0 0-3.5Z"/><path d="m10 9.5 5 2.5-5 2.5v-5Z"/></svg></a>
          </div>
        </div>
        <div class="footer-col">
          <h5>Categories</h5>
          <ul>
            <li><a href="laptops.html">Laptops</a></li>
            <li><a href="smartphones.html">Smartphones</a></li>
            <li><a href="headphones.html">Headphones</a></li>
            <li><a href="smartwatches.html">Smartwatches</a></li>
            <li><a href="gaming.html">Gaming</a></li>
            <li><a href="accessories.html">Accessories</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Company</h5>
          <ul>
            <li><a href="about.html">About Us</a></li>
            <li><a href="brands.html">Our Brands</a></li>
            <li><a href="weekly-deals.html">Weekly Deals</a></li>
            <li><a href="bulk-orders.html">Bulk &amp; Corporate</a></li>
            <li><a href="store-locator.html">Store Locator</a></li>
          </ul>
        </div>
        
        <div class="footer-col footer-newsletter">
          <h5>Stay Updated</h5>
          <p style="font-size:var(--fs-sm); margin:0;">Get exclusive deals &amp; launch alerts.</p>
          <form id="footerNewsletterForm">
            <input type="email" required placeholder="Your email" aria-label="Email for newsletter">
            <button type="submit" class="btn btn-primary">Join</button>
          </form>
          <ul class="footer-contact" style="margin-top:var(--sp-5);">
            <li>${ICONS.phoneIcon}<span>1-800-VOLTAGE</span></li>
            <li>${ICONS.mail}<span>support@voltage-store.example</span></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <span>&copy; ${year} Voltage Electronics. All rights reserved.</span>
        <div class="footer-payments">
          <span>VISA</span><span>MC</span><span>AMEX</span><span>PayPal</span>
        </div>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a><a href="#">Terms of Service</a>
        </div>
      </div>
    </div>`;
  }

  /* ---------------- SPEC STRIP CONTENT ---------------- */
  function buildSpecStrip() {
    const items = [
      { label: "RTX 5090 Laptops", meta: "In Stock", trend: "up" },
      { label: "iPhone 17 Pro", meta: "Now Shipping", trend: "" },
      { label: "Weekly Deal", meta: "Up to 40% off headphones", trend: "down" },
      { label: "Galaxy Watch 8", meta: "New Arrival", trend: "up" },
      { label: "Bulk Orders", meta: "Corporate pricing available", trend: "" },
      { label: "Free Shipping", meta: "On orders over $99", trend: "" },
      { label: "Gaming Consoles", meta: "Restocked", trend: "up" },
      { label: "Trade-In Program", meta: "Get up to $400 back", trend: "" }
    ];
    const renderItems = arr => arr.map(i => `<div class="spec-strip__item"><strong>${i.label}</strong><span class="dot"></span><span>${i.meta}</span>${i.trend ? `<span class="${i.trend}">${i.trend === 'up' ? '▲' : '▼'}</span>` : ""}</div>`).join("");
    // duplicate the list for seamless marquee loop
    return renderItems(items) + renderItems(items);
  }

  /* ---------------- THEME (Dark Mode) ---------------- */
  function initTheme() {
    const stored = localStorage.getItem("voltage-theme");
    const prefersDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    const theme = stored || (prefersDark ? "dark" : "light");
    document.documentElement.classList.toggle("dark", theme === "dark");

    function toggleTheme() {
      const isDark = document.documentElement.classList.toggle("dark");
      localStorage.setItem("voltage-theme", isDark ? "dark" : "light");
    }
    document.addEventListener("click", e => {
      if (e.target.closest("#themeToggle") || e.target.closest('[data-sync="themeToggle"]')) {
        toggleTheme();
      }
    });
  }

  /* ---------------- RTL ---------------- */
  function initRTL() {
    const stored = localStorage.getItem("voltage-dir");
    if (stored === "rtl") {
      document.documentElement.setAttribute("dir", "rtl");
    }
    function toggleRTL() {
      const isRTL = document.documentElement.getAttribute("dir") === "rtl";
      document.documentElement.setAttribute("dir", isRTL ? "ltr" : "rtl");
      localStorage.setItem("voltage-dir", isRTL ? "ltr" : "rtl");
    }
    document.addEventListener("click", e => {
      if (e.target.closest("#rtlToggle") || e.target.closest('[data-sync="rtlToggle"]')) {
        toggleRTL();
      }
    });
  }

  /* ---------------- MOBILE NAV ---------------- */
  function initMobileNav() {
    const nav = document.getElementById("mobileNav");
    const overlay = document.getElementById("navOverlay");
    const openBtn = document.getElementById("menuToggle");
    const closeBtn = document.getElementById("mobileNavClose");

    function open() {
      nav.classList.add("active");
      overlay.classList.add("active");
      openBtn.setAttribute("aria-expanded", "true");
      document.body.style.overflow = "hidden";
    }
    function close() {
      nav.classList.remove("active");
      overlay.classList.remove("active");
      openBtn.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    }
    openBtn && openBtn.addEventListener("click", open);
    closeBtn && closeBtn.addEventListener("click", close);
    overlay && overlay.addEventListener("click", close);

    document.querySelectorAll(".mobile-accordion-toggle").forEach(btn => {
      btn.addEventListener("click", () => {
        const li = btn.closest("li");
        const submenu = li.querySelector(".mobile-submenu");
        const isOpen = li.classList.contains("open");
        document.querySelectorAll(".mobile-nav__body li.open").forEach(openLi => {
          openLi.classList.remove("open");
          openLi.querySelector(".mobile-submenu").style.maxHeight = null;
        });
        if (!isOpen) {
          li.classList.add("open");
          submenu.style.maxHeight = submenu.scrollHeight + "px";
        }
      });
    });

    // Escape key closes drawer
    document.addEventListener("keydown", e => {
      if (e.key === "Escape") close();
    });
  }

  /* ---------------- BACK TO TOP ---------------- */
  function initBackToTop() {
    const btn = document.createElement("button");
    btn.className = "back-to-top";
    btn.setAttribute("aria-label", "Back to top");
    btn.innerHTML = ICONS.arrowUp;
    document.body.appendChild(btn);
    window.addEventListener("scroll", () => {
      btn.classList.toggle("show", window.scrollY > 500);
    }, { passive: true });
    btn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
  }

  /* ---------------- HEADER SCROLL STYLE ---------------- */
  function initHeaderScroll() {
    const header = document.querySelector(".site-header");
    if (!header) return;
    window.addEventListener("scroll", () => {
      header.style.boxShadow = window.scrollY > 8 ? "var(--shadow-sm)" : "none";
    }, { passive: true });
  }

  /* ---------------- NEWSLETTER (demo-only, no backend) ---------------- */
  function initNewsletter() {
    const form = document.getElementById("footerNewsletterForm");
    if (!form) return;
    form.addEventListener("submit", e => {
      e.preventDefault();
      const btn = form.querySelector("button");
      const original = btn.textContent;
      btn.textContent = "Subscribed ✓";
      form.querySelector("input").value = "";
      setTimeout(() => (btn.textContent = original), 2200);
    });
  }

  /* ---------------- INIT ---------------- */
  function injectLayout() {
    const headerEl = document.getElementById("main-header");
    const footerEl = document.getElementById("main-footer");
    if (headerEl) headerEl.innerHTML = buildHeader();
    if (footerEl) footerEl.innerHTML = buildFooter();
    const strip = document.getElementById("specStripTrack");
    if (strip) strip.innerHTML = buildSpecStrip();
  }

  document.addEventListener("DOMContentLoaded", () => {
    injectLayout();
    initTheme();
    initRTL();
    initMobileNav();
    initBackToTop();
    initHeaderScroll();
    initNewsletter();
    document.dispatchEvent(new CustomEvent("voltage:layoutReady"));
  });
})();
