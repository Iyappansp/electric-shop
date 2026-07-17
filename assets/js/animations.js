/* ==========================================================================
   VOLTAGE — animations.js
   Handles: Scroll reveal, Counter animation, Carousel, Category slider,
   Testimonial slider, Accordion (FAQ), Offer countdown timers.
   ========================================================================== */

(function () {
  "use strict";

  /* ---------------- SCROLL REVEAL ---------------- */
  function initScrollReveal() {
    const targets = document.querySelectorAll("[data-reveal]");
    if (!("IntersectionObserver" in window) || !targets.length) {
      targets.forEach(t => t.classList.add("is-visible"));
      return;
    }
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -60px 0px" });
    targets.forEach((t, i) => {
      t.style.setProperty("--i", i % 8);
      io.observe(t);
    });
  }

  /* Re-run reveal for dynamically injected content (products.js renders after DOMContentLoaded) */
  function observeDynamicReveal() {
    document.addEventListener("voltage:layoutReady", () => {
      setTimeout(initScrollReveal, 60);
    });
  }

  /* ---------------- COUNTER ANIMATION ---------------- */
  function initCounters() {
    const counters = document.querySelectorAll("[data-counter]");
    if (!counters.length) return;
    const animate = (el) => {
      const target = Number(el.getAttribute("data-counter"));
      const suffix = el.getAttribute("data-counter-suffix") || "";
      const duration = 1600;
      const start = performance.now();
      function step(now) {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target).toLocaleString() + suffix;
        if (progress < 1) requestAnimationFrame(step);
        else el.textContent = target.toLocaleString() + suffix;
      }
      requestAnimationFrame(step);
    };
    if ("IntersectionObserver" in window) {
      const io = new IntersectionObserver(entries => {
        entries.forEach(e => {
          if (e.isIntersecting) { animate(e.target); io.unobserve(e.target); }
        });
      }, { threshold: 0.4 });
      counters.forEach(c => io.observe(c));
    } else {
      counters.forEach(animate);
    }
  }

  /* ---------------- GENERIC CAROUSEL ---------------- */
  function initCarousels() {
    document.querySelectorAll("[data-carousel]").forEach(carousel => {
      const track = carousel.querySelector("[data-carousel-track]");
      const prev = carousel.querySelector("[data-carousel-prev]");
      const next = carousel.querySelector("[data-carousel-next]");
      const dotsWrap = carousel.querySelector("[data-carousel-dots]");
      if (!track) return;
      const slides = Array.from(track.children);
      let index = 0;

      function visibleCount() {
        const w = carousel.clientWidth;
        if (w >= 1024) return Number(carousel.getAttribute("data-per-desktop")) || 4;
        if (w >= 768) return Number(carousel.getAttribute("data-per-tablet")) || 2;
        return 1;
      }

      function update() {
        const per = visibleCount();
        const maxIndex = Math.max(0, slides.length - per);
        index = Math.min(index, maxIndex);
        const slideWidth = slides[0] ? slides[0].getBoundingClientRect().width + 24 : 0;
        track.style.transform = `translateX(${document.documentElement.getAttribute("dir") === "rtl" ? "" : "-"}${index * slideWidth}px)`;
        if (dotsWrap) {
          const dotCount = maxIndex + 1;
          dotsWrap.innerHTML = Array.from({ length: dotCount }).map((_, i) => `<button class="carousel-dot ${i === index ? "active" : ""}" data-go="${i}" aria-label="Go to slide ${i + 1}"></button>`).join("");
        }
      }

      prev && prev.addEventListener("click", () => { index = Math.max(0, index - 1); update(); });
      next && next.addEventListener("click", () => {
        const per = visibleCount();
        index = Math.min(slides.length - per, index + 1);
        update();
      });
      dotsWrap && dotsWrap.addEventListener("click", e => {
        const btn = e.target.closest("[data-go]");
        if (btn) { index = Number(btn.getAttribute("data-go")); update(); }
      });
      window.addEventListener("resize", update);
      setTimeout(update, 50);
    });
  }

  /* ---------------- ACCORDION (FAQ) ---------------- */
  function initAccordions() {
    document.querySelectorAll("[data-accordion]").forEach(acc => {
      acc.querySelectorAll(".accordion-item").forEach(item => {
        const trigger = item.querySelector(".accordion-trigger");
        const panel = item.querySelector(".accordion-panel");
        trigger && trigger.addEventListener("click", () => {
          const isOpen = item.classList.contains("open");
          if (acc.hasAttribute("data-single-open")) {
            acc.querySelectorAll(".accordion-item.open").forEach(openItem => {
              if (openItem !== item) {
                openItem.classList.remove("open");
                openItem.querySelector(".accordion-panel").style.maxHeight = null;
                openItem.querySelector(".accordion-trigger").setAttribute("aria-expanded", "false");
              }
            });
          }
          item.classList.toggle("open", !isOpen);
          trigger.setAttribute("aria-expanded", String(!isOpen));
          panel.style.maxHeight = !isOpen ? panel.scrollHeight + "px" : null;
        });
      });
    });
  }

  /* ---------------- TABS ---------------- */
  function initTabs() {
    document.querySelectorAll("[data-tabs]").forEach(tabGroup => {
      const buttons = tabGroup.querySelectorAll("[data-tab-btn]");
      const panels = tabGroup.querySelectorAll("[data-tab-panel]");
      buttons.forEach(btn => {
        btn.addEventListener("click", () => {
          const target = btn.getAttribute("data-tab-btn");
          buttons.forEach(b => b.classList.toggle("active", b === btn));
          panels.forEach(p => p.classList.toggle("active", p.getAttribute("data-tab-panel") === target));
        });
      });
    });
  }

  /* ---------------- COUNTDOWN (Weekly Deals / Offer Cards) ---------------- */
  function initCountdowns() {
    document.querySelectorAll("[data-countdown]").forEach(el => {
      const hours = Number(el.getAttribute("data-countdown")) || 48;
      const end = Date.now() + hours * 3600 * 1000;
      function render() {
        const diff = Math.max(0, end - Date.now());
        const d = Math.floor(diff / 86400000);
        const h = Math.floor((diff % 86400000) / 3600000);
        const m = Math.floor((diff % 3600000) / 60000);
        const s = Math.floor((diff % 60000) / 1000);
        el.innerHTML = `
          <div class="unit"><strong>${String(d).padStart(2, "0")}</strong><span>Days</span></div>
          <div class="unit"><strong>${String(h).padStart(2, "0")}</strong><span>Hrs</span></div>
          <div class="unit"><strong>${String(m).padStart(2, "0")}</strong><span>Min</span></div>
          <div class="unit"><strong>${String(s).padStart(2, "0")}</strong><span>Sec</span></div>`;
        if (diff > 0) requestAnimationFrame(() => setTimeout(render, 1000));
      }
      render();
    });
  }

  /* ---------------- TESTIMONIAL / REVIEW SLIDER (simple auto-rotate) ---------------- */
  function initTestimonialSlider() {
    document.querySelectorAll("[data-testimonial-slider]").forEach(wrap => {
      const slides = wrap.querySelectorAll(".testimonial-slide");
      if (slides.length < 2) return;
      let i = 0;
      slides.forEach((s, idx) => s.classList.toggle("active", idx === 0));
      setInterval(() => {
        slides[i].classList.remove("active");
        i = (i + 1) % slides.length;
        slides[i].classList.add("active");
      }, 5000);
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    initScrollReveal();
    observeDynamicReveal();
    initCounters();
    initCarousels();
    initAccordions();
    initTabs();
    initCountdowns();
    initTestimonialSlider();
  });
})();
