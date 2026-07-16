/* ST. GEORGE CONCRETE — shared scripts */
(function () {
  "use strict";
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Theme (light / dark) ---------- */
  const root = document.documentElement;
  function applyTheme(t, persist) {
    root.setAttribute("data-theme", t);
    if (persist) { try { localStorage.setItem("sg-theme", t); } catch (e) {} }
    const btn = $("#themeToggle");
    if (btn) btn.setAttribute("aria-pressed", t === "dark" ? "true" : "false");
  }
  // Head script already set the attribute pre-paint; sync button state here.
  applyTheme(root.getAttribute("data-theme") || "light", false);
  const themeBtn = $("#themeToggle");
  if (themeBtn) themeBtn.addEventListener("click", () => {
    applyTheme(root.getAttribute("data-theme") === "dark" ? "light" : "dark", true);
  });
  // Follow system changes unless the user chose manually.
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (e) => {
    try { if (!localStorage.getItem("sg-theme")) applyTheme(e.matches ? "dark" : "light", false); } catch (err) {}
  });

  /* ---------- Header + mobile nav ---------- */
  const header = $("#site-header");
  const onScrollHeader = () => header && header.classList.toggle("scrolled", window.scrollY > 8);
  onScrollHeader();
  window.addEventListener("scroll", onScrollHeader, { passive: true });

  const burger = $("#burger"), panel = $("#mobilePanel"), dim = $("#overlayDim");
  function closeNav() {
    burger && burger.classList.remove("open");
    panel && panel.classList.remove("open");
    dim && dim.classList.remove("show");
    burger && burger.setAttribute("aria-expanded", "false");
  }
  if (burger && panel) {
    burger.addEventListener("click", () => {
      const open = panel.classList.toggle("open");
      burger.classList.toggle("open", open);
      dim && dim.classList.toggle("show", open);
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    dim && dim.addEventListener("click", closeNav);
    $$("a", panel).forEach(a => a.addEventListener("click", closeNav));
  }

  /* ---------- Reveal on scroll ---------- */
  const revealEls = $$(".reveal,.reveal-left,.reveal-right,.reveal-scale");
  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealEls.forEach(el => el.classList.add("in"));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(el => io.observe(el));
  }

  /* ---------- Animated counters ---------- */
  const counters = $$(".count");
  if (counters.length) {
    const run = (el) => {
      const target = parseFloat(el.dataset.target || "0");
      const dec = parseInt(el.dataset.decimal || "0", 10);
      const divisor = dec ? Math.pow(10, dec) : 1;
      if (reduceMotion) { el.textContent = (target / divisor).toFixed(dec); return; }
      const dur = 1400, t0 = performance.now();
      (function tick(now) {
        const p = Math.min((now - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
        el.textContent = ((target * eased) / divisor).toFixed(dec);
        if (p < 1) requestAnimationFrame(tick);
      })(t0);
    };
    const cio = new IntersectionObserver((entries) => {
      entries.forEach(en => { if (en.isIntersecting) { run(en.target); cio.unobserve(en.target); } });
    }, { threshold: 0.5 });
    counters.forEach(c => cio.observe(c));
  }

  /* ---------- Testimonial slider ---------- */
  const tmTrack = $("#tmTrack");
  if (tmTrack) {
    const slides = $$(".tm-slide", tmTrack);
    const dotsWrap = $("#tmDots");
    let i = 0, timer = null;
    const dots = slides.map((_, idx) => {
      const d = document.createElement("button");
      d.setAttribute("aria-label", "Show testimonial " + (idx + 1));
      d.addEventListener("click", () => go(idx, true));
      dotsWrap && dotsWrap.appendChild(d);
      return d;
    });
    function go(n, user) {
      i = (n + slides.length) % slides.length;
      slides.forEach((s, idx) => s.classList.toggle("active", idx === i));
      dots.forEach((d, idx) => d.classList.toggle("active", idx === i));
      if (user) restart();
    }
    function restart() {
      if (timer) clearInterval(timer);
      if (!reduceMotion) timer = setInterval(() => go(i + 1, false), 6500);
    }
    const prev = $("#tmPrev"), next = $("#tmNext");
    prev && prev.addEventListener("click", () => go(i - 1, true));
    next && next.addEventListener("click", () => go(i + 1, true));
    go(0, false); restart();
  }

  /* ---------- Gallery filters + lightbox ---------- */
  const grid = $("#galleryGrid");
  if (grid) {
    const items = $$(".gallery-item", grid);
    $$(".filter-btn").forEach(btn => btn.addEventListener("click", () => {
      $$(".filter-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const f = btn.dataset.filter;
      items.forEach(it => it.classList.toggle("hide", f !== "all" && it.dataset.cat !== f));
    }));

    const lb = $("#lightbox");
    if (lb) {
      const lbImg = $("#lbImg"), lbCap = $("#lbCap");
      let visible = [], idx = 0;
      function openAt(item) {
        visible = items.filter(it => !it.classList.contains("hide"));
        idx = visible.indexOf(item);
        show(); lb.classList.add("open"); document.body.style.overflow = "hidden";
      }
      function show() {
        const it = visible[idx]; if (!it) return;
        const img = $("img", it);
        lbImg.src = img.currentSrc || img.src;
        lbImg.alt = img.alt || "";
        const cat = $(".cat", it), ti = $(".ti", it);
        lbCap.textContent = (cat ? cat.textContent + " — " : "") + (ti ? ti.textContent : "");
      }
      function close() { lb.classList.remove("open"); document.body.style.overflow = ""; }
      items.forEach(it => {
        it.setAttribute("tabindex", "0");
        it.setAttribute("role", "button");
        it.addEventListener("click", () => openAt(it));
        it.addEventListener("keydown", e => { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openAt(it); } });
      });
      $("#lbClose").addEventListener("click", close);
      $("#lbPrev").addEventListener("click", () => { idx = (idx - 1 + visible.length) % visible.length; show(); });
      $("#lbNext").addEventListener("click", () => { idx = (idx + 1) % visible.length; show(); });
      lb.addEventListener("click", e => { if (e.target === lb) close(); });
      document.addEventListener("keydown", e => {
        if (!lb.classList.contains("open")) return;
        if (e.key === "Escape") close();
        if (e.key === "ArrowLeft") { idx = (idx - 1 + visible.length) % visible.length; show(); }
        if (e.key === "ArrowRight") { idx = (idx + 1) % visible.length; show(); }
      });
    }
  }

  /* ---------- FAQ accordion ---------- */
  $$(".faq-item").forEach(item => {
    const q = $(".faq-q", item);
    q && q.addEventListener("click", () => {
      const wasOpen = item.classList.contains("open");
      $$(".faq-item").forEach(i2 => i2.classList.remove("open"));
      if (!wasOpen) item.classList.add("open");
    });
  });

  /* ---------- Contact form (demo submit) ---------- */
  const form = $("#contactForm");
  if (form) form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    form.classList.add("sent");
    const ok = $(".form-success", form);
    ok && ok.classList.add("show");
    ok && ok.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth", block: "center" });
  });

  /* ---------- Newsletter (demo) ---------- */
  $$(".newsletter").forEach(n => {
    const btn = $("button", n), input = $("input", n);
    btn && btn.addEventListener("click", () => {
      if (input && input.value.includes("@")) { input.value = ""; input.placeholder = "Subscribed — thank you!"; }
      else if (input) { input.focus(); }
    });
  });

  /* ---------- Back to top ---------- */
  const topBtn = $("#top-btn");
  if (topBtn) {
    window.addEventListener("scroll", () => {
      topBtn.classList.toggle("show", window.scrollY > 640);
    }, { passive: true });
    topBtn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" }));
  }

  /* ---------- Footer year ---------- */
  const yr = $("#year"); if (yr) yr.textContent = new Date().getFullYear();
})();
