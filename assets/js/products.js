/* ==========================================================================
   VOLTAGE — products.js
   Handles: Product catalog data, category filters, product-card rendering,
   wishlist state (localStorage), sorting.
   ========================================================================== */

(function () {
  "use strict";

  const prodImg = (id) => `assets/images/products/product_${id}.png`;

  /* ---------------- CATALOG ---------------- */
  const PRODUCTS = [
    { id: 1, name: "AeroBook Pro 16 OLED", cat: "Laptops", sub: "Creator", brand: "ASUS", price: 2199, was: 2499, rating: 4.8, badge: "sale", img: prodImg(1) },
    { id: 2, name: "Vortex Gaming Laptop", cat: "Laptops", sub: "Gaming", brand: "ASUS", price: 2799, was: null, rating: 4.9, badge: "new", img: prodImg(2) },
    { id: 3, name: "EliteBook Ultraslim 14", cat: "Laptops", sub: "Business", brand: "Dell", price: 1349, was: null, rating: 4.6, badge: "", img: prodImg(3) },
    { id: 4, name: "StudyMate Air 13", cat: "Laptops", sub: "Student", brand: "Lenovo", price: 799, was: 899, rating: 4.4, badge: "sale", img: prodImg(4) },
    { id: 5, name: "Zenith Ultrabook X", cat: "Laptops", sub: "Ultrabooks", brand: "ASUS", price: 1599, was: null, rating: 4.7, badge: "", img: prodImg(5) },
    { id: 6, name: "Nimbus Phone 15", cat: "Smartphones", sub: "Flagship", brand: "Samsung", price: 1099, was: null, rating: 4.8, badge: "new", img: prodImg(6) },
    { id: 7, name: "AuraPhone Pro Max", cat: "Smartphones", sub: "iPhone", brand: "Apple", price: 1299, was: null, rating: 4.9, badge: "", img: prodImg(7) },
    { id: 8, name: "Pulse Lite 5G", cat: "Smartphones", sub: "Budget", brand: "Samsung", price: 349, was: 429, rating: 4.2, badge: "sale", img: prodImg(8) },
    { id: 9, name: "DroidCore X3", cat: "Smartphones", sub: "Android", brand: "Sony", price: 749, was: null, rating: 4.5, badge: "", img: prodImg(9) },
    { id: 10, name: "SoundHalo ANC Pro", cat: "Headphones", sub: "Noise Cancelling", brand: "Sony", price: 349, was: 399, rating: 4.8, badge: "sale", img: prodImg(10) },
    { id: 11, name: "GameSound Wireless GX", cat: "Headphones", sub: "Gaming", brand: "Logitech", price: 179, was: null, rating: 4.6, badge: "", img: prodImg(11) },
    { id: 12, name: "StudioTrue Reference", cat: "Headphones", sub: "Studio", brand: "Sony", price: 299, was: null, rating: 4.7, badge: "", img: prodImg(12) },
    { id: 13, name: "SprintFit Sport Buds", cat: "Headphones", sub: "Sports", brand: "JBL", price: 129, was: 159, rating: 4.3, badge: "sale", img: prodImg(13) },
    { id: 14, name: "AirWave Buds 2", cat: "Headphones", sub: "Wireless", brand: "Apple", price: 199, was: null, rating: 4.6, badge: "new", img: prodImg(14) },
    { id: 15, name: "PulseWatch Fit Pro", cat: "Smartwatches", sub: "Fitness", brand: "Samsung", price: 279, was: null, rating: 4.5, badge: "", img: prodImg(15) },
    { id: 16, name: "ChronoLux Premium", cat: "Smartwatches", sub: "Premium", brand: "Apple", price: 599, was: null, rating: 4.8, badge: "new", img: prodImg(16) },
    { id: 17, name: "EveryDay Watch SE", cat: "Smartwatches", sub: "Lifestyle", brand: "Samsung", price: 199, was: 249, rating: 4.3, badge: "sale", img: prodImg(17) },
    { id: 18, name: "JuniorTrack Kids", cat: "Smartwatches", sub: "Kids", brand: "Samsung", price: 89, was: null, rating: 4.1, badge: "", img: prodImg(18) },
    { id: 19, name: "TitanForce Gaming", cat: "Gaming", sub: "Gaming PCs", brand: "ASUS", price: 2999, was: null, rating: 4.9, badge: "new", img: prodImg(19) },
    { id: 20, name: "PixelView 27\" 240Hz", cat: "Gaming", sub: "Monitors", brand: "ASUS", price: 549, was: 649, rating: 4.7, badge: "sale", img: prodImg(20) },
    { id: 21, name: "GripCommand Pro", cat: "Gaming", sub: "Controllers", brand: "Logitech", price: 79, was: null, rating: 4.5, badge: "", img: prodImg(21) },
    { id: 22, name: "StreamCast Capture", cat: "Gaming", sub: "Streaming", brand: "Logitech", price: 249, was: null, rating: 4.6, badge: "", img: prodImg(22) },
    { id: 23, name: "MechType Pro", cat: "Accessories", sub: "Keyboard", brand: "Logitech", price: 149, was: null, rating: 4.7, badge: "", img: prodImg(23) },
    { id: 24, name: "PrecisionGlide Mouse", cat: "Accessories", sub: "Mouse", brand: "Logitech", price: 89, was: 109, rating: 4.6, badge: "sale", img: prodImg(24) },
    { id: 25, name: "VaultDrive 2TB SSD", cat: "Accessories", sub: "Storage", brand: "Dell", price: 159, was: null, rating: 4.8, badge: "", img: prodImg(25) },
    { id: 26, name: "PowerLine 100W GaN", cat: "Accessories", sub: "Chargers", brand: "Apple", price: 59, was: null, rating: 4.5, badge: "new", img: prodImg(26) },
    { id: 27, name: "LinkWeave Mesh", cat: "Accessories", sub: "Networking", brand: "ASUS", price: 229, was: null, rating: 4.6, badge: "", img: prodImg(27) },
    { id: 28, name: "HomeGlow Smart", cat: "Accessories", sub: "Smart Home", brand: "Samsung", price: 69, was: 89, rating: 4.3, badge: "sale", img: prodImg(28) },
    { id: 29, name: "ThinkBook Studio 14", cat: "Laptops", sub: "Business", brand: "Lenovo", price: 1199, was: 1299, rating: 4.6, badge: "sale", img: prodImg(29) },
    { id: 31, name: "iPhone 16 Pro", cat: "Smartphones", sub: "iPhone", brand: "Apple", price: 999, was: null, rating: 4.9, badge: "new", img: prodImg(31) },
    { id: 32, name: "Xperia Ultra 5G", cat: "Smartphones", sub: "Android", brand: "Sony", price: 899, was: 999, rating: 4.5, badge: "sale", img: prodImg(32) },
    { id: 33, name: "TuneSport Wireless", cat: "Headphones", sub: "Sports", brand: "JBL", price: 99, was: null, rating: 4.4, badge: "", img: prodImg(33) },
    { id: 34, name: "ProStream Webcam 4K", cat: "Gaming", sub: "Streaming", brand: "Logitech", price: 199, was: null, rating: 4.6, badge: "", img: prodImg(34) },
    { id: 35, name: "ROG Swift 360Hz", cat: "Gaming", sub: "Monitors", brand: "ASUS", price: 699, was: 799, rating: 4.8, badge: "sale", img: prodImg(35) },
    { id: 36, name: "Apex Run Ultra", cat: "Smartwatches", sub: "Fitness", brand: "Apple", price: 799, was: null, rating: 4.9, badge: "new", img: prodImg(36) },
    { id: 37, name: "Galaxy Watch Ultra 2", cat: "Smartwatches", sub: "Premium", brand: "Samsung", price: 649, was: 749, rating: 4.8, badge: "sale", img: prodImg(37) }
  ];

  const CATEGORY_ICONS = {
    "Laptops": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="1"/><path d="M2 20h20"/></svg>',
    "Smartphones": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="2" width="12" height="20" rx="2"/><path d="M11 18h2"/></svg>',
    "Headphones": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 14v-3a9 9 0 0 1 18 0v3"/><path d="M21 14a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-2a2 2 0 0 1 2-2h3v4ZM3 14a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-2a2 2 0 0 0-2-2H3v4Z"/></svg>',
    "Smartwatches": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M9 7V4h6v3M9 17v3h6v-3"/></svg>',
    "Gaming": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12h4m-2-2v4M15 13h.01M18 11h.01"/><rect x="2" y="7" width="20" height="10" rx="5"/></svg>',
    "Accessories": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.6 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.6a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1Z"/></svg>',
    "Monitors": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
    "Networking": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0M1.42 9a16 16 0 0 1 21.16 0M8.53 16.11a6 6 0 0 1 6.95 0M12 20h.01"/></svg>'
  };
  window.VOLTAGE_CATEGORY_ICONS = CATEGORY_ICONS;
  window.VOLTAGE_PRODUCTS = PRODUCTS;

  const STAR = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 3.09 6.26L22 9.27l-5 4.87L18.18 21 12 17.77 5.82 21 7 14.14l-5-4.87 6.91-1.01L12 2Z"/></svg>';

  /* ---------------- WISHLIST (localStorage) ---------------- */
  const WishlistStore = {
    key: "voltage-wishlist",
    get() { try { return JSON.parse(localStorage.getItem(this.key)) || []; } catch { return []; } },
    toggle(id) {
      let list = this.get();
      if (list.includes(id)) list = list.filter(i => i !== id);
      else list.push(id);
      localStorage.setItem(this.key, JSON.stringify(list));
      return list.includes(id);
    },
    has(id) { return this.get().includes(id); }
  };
  window.VoltageWishlist = WishlistStore;

  /* ---------------- CARD RENDERER ---------------- */
  function money(n) { return "$" + n.toLocaleString("en-US"); }

  function renderProductCard(p, opts = {}) {
    const badgeHtml = p.badge ? `<span class="product-card__badge badge-${p.badge}">${p.badge === "sale" ? "Sale" : "New"}</span>` : "";
    const isWished = WishlistStore.has(p.id);
    const compareAttr = opts.compare ? `<label class="product-card__compare"><input type="checkbox" class="compare-check" data-id="${p.id}"> Add to compare</label>` : "";
    return `
    <article class="product-card" data-cat="${p.cat}" data-brand="${p.brand}" data-price="${p.price}" data-name="${p.name.toLowerCase()}">
      <div class="product-card__media">
        ${badgeHtml}
        <button class="product-card__wishlist ${isWished ? "active" : ""}" data-wishlist="${p.id}" aria-label="Toggle wishlist">${document.querySelector ? '<svg viewBox="0 0 24 24" fill="' + (isWished ? 'currentColor' : 'none') + '" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>' : ''}</button>
        <img src="${p.img}" alt="${p.name} — ${p.sub} ${p.cat}" loading="lazy" width="640" height="480">
      </div>
      <div class="product-card__body">
        <span class="product-card__cat">${p.brand} · ${p.sub}</span>
        <h3 class="product-card__title"><a href="${categoryPage(p.cat)}#product-${p.id}">${p.name}</a></h3>
        <div class="product-card__rating">${STAR.repeat(1)}<span>${p.rating} rating</span></div>
        <div class="product-card__price">
          <span class="now">${money(p.price)}</span>
          ${p.was ? `<span class="was">${money(p.was)}</span>` : ""}
        </div>
      </div>
      ${compareAttr}
      <div class="product-card__actions">
        <a href="${categoryPage(p.cat)}#product-${p.id}" class="btn btn-secondary btn-sm">Details</a>
        <button class="btn btn-primary btn-sm add-to-cart" data-id="${p.id}">Add to Cart</button>
      </div>
    </article>`;
  }

  function categoryPage(cat) {
    const map = { "Laptops": "laptops.html", "Smartphones": "smartphones.html", "Headphones": "headphones.html", "Smartwatches": "smartwatches.html", "Gaming": "gaming.html", "Accessories": "accessories.html" };
    return map[cat] || "categories.html";
  }
  window.VoltageRenderCard = renderProductCard;

  /* ---------------- GRID RENDER + FILTER ENGINE ---------------- */
  function renderGrid(containerEl, list, opts = {}) {
    if (!list.length) {
      containerEl.innerHTML = `<div class="empty-state" style="grid-column:1/-1;text-align:center;padding:var(--sp-8) 0;">
        <p style="font-family:var(--font-display);font-weight:600;font-size:var(--fs-lg);color:var(--text-primary);">No products match your filters</p>
        <p>Try adjusting or clearing your filters to see more results.</p>
      </div>`;
      return;
    }
    containerEl.innerHTML = list.map(p => renderProductCard(p, opts)).join("");
  }

  function initCatalogPage() {
    const grid = document.querySelector("[data-product-grid]");
    if (!grid) return;
    const category = grid.getAttribute("data-category"); // e.g. "Laptops" or "" for all
    let list = category ? PRODUCTS.filter(p => p.cat === category) : PRODUCTS.slice();

    const subFilter = document.querySelector("[data-filter-sub]");
    const brandFilter = document.querySelector("[data-filter-brand]");
    const priceFilter = document.querySelector("[data-filter-price]");
    const sortSelect = document.querySelector("[data-sort]");
    const resultCount = document.querySelector("[data-result-count]");

    function apply() {
      let filtered = category ? PRODUCTS.filter(p => p.cat === category) : PRODUCTS.slice();
      const sub = subFilter ? [...subFilter.querySelectorAll("input:checked")].map(i => i.value) : [];
      const brand = brandFilter ? [...brandFilter.querySelectorAll("input:checked")].map(i => i.value) : [];
      const maxPrice = priceFilter ? Number(priceFilter.value) : null;

      if (sub.length) filtered = filtered.filter(p => sub.includes(p.sub));
      if (brand.length) filtered = filtered.filter(p => brand.includes(p.brand));
      if (maxPrice) filtered = filtered.filter(p => p.price <= maxPrice);

      const sortVal = sortSelect ? sortSelect.value : "featured";
      if (sortVal === "price-asc") filtered.sort((a, b) => a.price - b.price);
      if (sortVal === "price-desc") filtered.sort((a, b) => b.price - a.price);
      if (sortVal === "rating") filtered.sort((a, b) => b.rating - a.rating);

      renderGrid(grid, filtered, { compare: grid.hasAttribute("data-compare-enabled") });
      if (resultCount) resultCount.textContent = `${filtered.length} product${filtered.length !== 1 ? "s" : ""}`;
      grid.querySelectorAll("[data-reveal]").forEach(el => el.classList.add("is-visible"));
    }

    [subFilter, brandFilter].forEach(f => f && f.addEventListener("change", apply));
    priceFilter && priceFilter.addEventListener("input", () => {
      const out = document.querySelector("[data-price-output]");
      if (out) out.textContent = "$" + Number(priceFilter.value).toLocaleString();
      apply();
    });
    sortSelect && sortSelect.addEventListener("change", apply);

    const clearBtn = document.querySelector("[data-clear-filters]");
    clearBtn && clearBtn.addEventListener("click", () => {
      document.querySelectorAll("[data-filter-sub] input, [data-filter-brand] input").forEach(i => (i.checked = false));
      if (priceFilter) priceFilter.value = priceFilter.max;
      apply();
    });

    apply();
  }

  /* ---------------- WISHLIST + CART CLICK DELEGATION (global) ---------------- */
  function initGlobalProductEvents() {
    document.addEventListener("click", e => {
      const wishBtn = e.target.closest("[data-wishlist]");
      if (wishBtn) {
        const id = Number(wishBtn.getAttribute("data-wishlist"));
        const active = WishlistStore.toggle(id);
        wishBtn.classList.toggle("active", active);
        wishBtn.innerHTML = `<svg viewBox="0 0 24 24" fill="${active ? "currentColor" : "none"}" stroke="currentColor" stroke-width="2"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.29 1.51 4.04 3 5.5l7 7Z"/></svg>`;
      }
      const cartBtn = e.target.closest(".add-to-cart");
      if (cartBtn) {
        const original = cartBtn.textContent;
        cartBtn.textContent = "Added ✓";
        cartBtn.disabled = true;
        setTimeout(() => { cartBtn.textContent = original; cartBtn.disabled = false; }, 1600);
      }
    });
  }

  /* ---------------- HOMEPAGE FEATURED RENDER HELPERS ---------------- */
  function initFeaturedSections() {
    document.querySelectorAll("[data-featured]").forEach(el => {
      const type = el.getAttribute("data-featured"); // "all" | "sale" | "new" | category name | "brand-ASUS"
      const limit = Number(el.getAttribute("data-limit")) || 8;
      let list;
      if (type === "sale") list = PRODUCTS.filter(p => p.badge === "sale");
      else if (type === "new") list = PRODUCTS.filter(p => p.badge === "new");
      else if (type === "all") list = PRODUCTS.slice();
      else if (type.startsWith("brand-")) {
        const targetBrand = type.replace("brand-", "").toLowerCase();
        list = PRODUCTS.filter(p => p.brand.toLowerCase() === targetBrand);
        if (targetBrand === "asus") {
          list = list.map((p, idx) => ({ ...p, img: `assets/images/brands/rog_product_${(idx % 4) + 1}.png` }));
        } else if (targetBrand === "apple") {
          list = list.map((p, idx) => ({ ...p, img: `assets/images/brands/apple_product_${(idx % 6) + 1}.png` }));
        }
      } else {
        list = PRODUCTS.filter(p => p.cat === type || p.brand.toLowerCase() === type.toLowerCase());
      }
      renderGrid(el, list.slice(0, limit));
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initGlobalProductEvents();
    initFeaturedSections();
    initCatalogPage();
  });
})();
