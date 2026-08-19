/* iHTC Studio site — main app shell
 * - Language detection & manual switching (persisted in localStorage)
 * - Light / Dark / Auto theme switching
 * - Scroll reveal animations (IntersectionObserver)
 * - Mobile drawer
 * - Anchor links on headings
 * - Homepage app grid (compact / accordion / expand-all)
 * Modular, dependency-free, ~5kB minified.
 */
(function () {
  "use strict";

  var STORAGE_LANG = "ihtc.lang";
  var STORAGE_THEME = "ihtc.theme";
  var SUPPORTED_LANGS = ["en", "zh-CN", "zh-TW"];
  var COARSE_POINTER = "(hover: none), (pointer: coarse)";
  var NARROW_VIEWPORT = "(max-width: 768px)";

  function isCoarsePointer() {
    return window.matchMedia(COARSE_POINTER).matches;
  }

  function isNarrowViewport() {
    return window.matchMedia(NARROW_VIEWPORT).matches;
  }

  function scrollIntoViewIfNeeded(el) {
    if (!el || (!isCoarsePointer() && !isNarrowViewport())) return;
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        el.scrollIntoView({ behavior: "smooth", block: "nearest" });
      });
    });
  }

  function bindOutsideDismiss(root, isActive, onDismiss) {
    function handleOutside(e) {
      if (!isActive()) return;
      if (root.contains(e.target)) return;
      onDismiss();
    }
    document.addEventListener("click", handleOutside);
    document.addEventListener("touchend", handleOutside, { passive: true });
  }

  // ---------------------------------------------------------------------------
  // Language
  // ---------------------------------------------------------------------------
  function detectLang() {
    var stored = safeGet(STORAGE_LANG);
    if (stored && SUPPORTED_LANGS.indexOf(stored) !== -1) return stored;
    var nav = (navigator.languages && navigator.languages[0]) || navigator.language || "en";
    var n = nav.toLowerCase();
    if (n.indexOf("zh") === 0) {
      if (n.indexOf("tw") !== -1 || n.indexOf("hk") !== -1 || n.indexOf("hant") !== -1 || n.indexOf("mo") !== -1) return "zh-TW";
      return "zh-CN";
    }
    return "en";
  }

  function applyLang(code, opts) {
    if (SUPPORTED_LANGS.indexOf(code) === -1) code = "en";
    document.documentElement.setAttribute("lang", code);
    document.documentElement.setAttribute("data-lang", code);
    document.querySelectorAll("[data-lang-toggle]").forEach(function (el) {
      var c = el.getAttribute("data-lang-value");
      el.setAttribute("aria-checked", c === code ? "true" : "false");
    });
    document.querySelectorAll("[data-lang-current]").forEach(function (el) {
      var label = el.getAttribute("data-lang-label-" + code) || code;
      el.textContent = label;
    });
    if (opts && opts.persist) safeSet(STORAGE_LANG, code);
    if (opts && opts.toast) {
      var msg = el => el.getAttribute("data-toast-" + code);
      var toastEl = document.querySelector("[data-toast-en]");
      if (toastEl) showToast(msg(toastEl));
    }
  }

  // ---------------------------------------------------------------------------
  // Theme
  // ---------------------------------------------------------------------------
  function detectTheme() {
    var stored = safeGet(STORAGE_THEME);
    if (stored === "light" || stored === "dark" || stored === "auto") return stored;
    return "auto";
  }

  function applyTheme(theme, opts) {
    if (theme !== "light" && theme !== "dark" && theme !== "auto") theme = "auto";
    document.documentElement.setAttribute("data-theme", theme);
    document.querySelectorAll("[data-theme-toggle]").forEach(function (el) {
      var t = el.getAttribute("data-theme-value");
      el.setAttribute("aria-checked", t === theme ? "true" : "false");
    });
    if (opts && opts.persist) safeSet(STORAGE_THEME, theme);
  }

  // ---------------------------------------------------------------------------
  // UI: dropdowns
  // ---------------------------------------------------------------------------
  function initDropdowns() {
    var dropdowns = document.querySelectorAll(".dropdown");
    dropdowns.forEach(function (dd) {
      var trigger = dd.querySelector("[data-dropdown-trigger]");
      var panel = dd.querySelector("[data-dropdown-panel]");
      if (!trigger || !panel) return;

      trigger.addEventListener("click", function (e) {
        e.stopPropagation();
        closeAllDropdowns(dd);
        dd.classList.toggle("is-open");
        trigger.setAttribute("aria-expanded", dd.classList.contains("is-open") ? "true" : "false");
      });

      panel.addEventListener("click", function (e) { e.stopPropagation(); });
    });

    document.addEventListener("click", function () { closeAllDropdowns(); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeAllDropdowns();
    });
  }

  function closeAllDropdowns(except) {
    document.querySelectorAll(".dropdown.is-open").forEach(function (dd) {
      if (dd === except) return;
      dd.classList.remove("is-open");
      var trig = dd.querySelector("[data-dropdown-trigger]");
      if (trig) trig.setAttribute("aria-expanded", "false");
    });
  }

  // ---------------------------------------------------------------------------
  // UI: language + theme toggles
  // ---------------------------------------------------------------------------
  function initLangToggles() {
    document.querySelectorAll("[data-lang-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var code = btn.getAttribute("data-lang-value");
        applyLang(code, { persist: true, toast: true });
        closeAllDropdowns();
      });
    });
  }

  function initThemeToggles() {
    document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var theme = btn.getAttribute("data-theme-value");
        applyTheme(theme, { persist: true });
        closeAllDropdowns();
      });
    });
  }

  // ---------------------------------------------------------------------------
  // Mobile drawer
  // ---------------------------------------------------------------------------
  function initMobileDrawer() {
    var drawer = document.querySelector("[data-drawer]");
    var openers = document.querySelectorAll("[data-drawer-open]");
    var closers = document.querySelectorAll("[data-drawer-close]");
    if (!drawer) return;

    function toggle(open) {
      drawer.classList.toggle("is-open", open);
      document.body.classList.toggle("is-drawer-open", open);
      drawer.setAttribute("aria-hidden", open ? "false" : "true");
    }
    openers.forEach(function (b) { b.addEventListener("click", function () { toggle(true); }); });
    closers.forEach(function (b) { b.addEventListener("click", function () { toggle(false); }); });

    drawer.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { toggle(false); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && drawer.classList.contains("is-open")) toggle(false);
    });
  }

  // ---------------------------------------------------------------------------
  // Scroll reveal
  // ---------------------------------------------------------------------------
  function initReveal() {
    if (!("IntersectionObserver" in window)) {
      document.querySelectorAll("[data-reveal], [data-reveal-stagger]").forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }
    // threshold 0 = fire as soon as any pixel enters. A fixed ratio like 0.12
    // never fires for elements taller than the viewport (e.g. the long
    // URL-scheme doc), which would leave them stuck at opacity:0.
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0, rootMargin: "0px 0px -5% 0px" });

    document.querySelectorAll("[data-reveal], [data-reveal-stagger]").forEach(function (el) {
      observer.observe(el);
    });
  }

  // ---------------------------------------------------------------------------
  // Guide page nav tables ("On this page")
  // ---------------------------------------------------------------------------
  function getActiveLangSection() {
    var lang = document.documentElement.getAttribute("lang") || "en";
    return document.querySelector('section[lang="' + lang + '"]');
  }

  function getGuidePartHeadings(section) {
    if (!section) return [];
    return Array.prototype.filter.call(section.querySelectorAll("h2"), function (h2) {
      return /Part \d+|第 \d+ 部分/.test(h2.textContent);
    });
  }

  function scrollToGuidePart(partIndex, opts) {
    var section = getActiveLangSection();
    var headings = getGuidePartHeadings(section);
    var target = headings[partIndex];
    if (!target) return;
    target.scrollIntoView({ behavior: (opts && opts.smooth) ? "smooth" : "auto", block: "start" });
    if (target.id) {
      history.replaceState(null, "", "#" + target.id);
    }
  }

  function initGuideNav() {
    var prose = document.querySelector(".prose");
    if (!prose) return;
    prose.querySelectorAll("h2").forEach(function (h2) {
      if (!/on this page|本页导航|本頁導覽/i.test(h2.textContent)) return;
      var table = h2.nextElementSibling;
      if (!table || table.tagName !== "TABLE") return;
      h2.classList.add("guide-nav-heading");
      table.classList.add("guide-nav-table");

      var rows = table.querySelectorAll("tbody tr");
      rows.forEach(function (row, index) {
        var link = row.querySelector("a[href^='#']");
        if (!link) return;
        link.addEventListener("click", function (e) {
          e.preventDefault();
          var lang = document.documentElement.getAttribute("lang") || "en";
          var activeSection = document.querySelector('section[lang="' + lang + '"]');
          var headings = getGuidePartHeadings(activeSection);
          var target = headings[index];
          if (target) {
            target.scrollIntoView({ behavior: "smooth", block: "start" });
            if (target.id) history.replaceState(null, "", "#" + target.id);
          }
        });
      });
    });

    if (location.hash) {
      var m = location.hash.match(/^#part-(\d+)$/);
      if (m) {
        requestAnimationFrame(function () {
          scrollToGuidePart(parseInt(m[1], 10) - 1, { smooth: false });
        });
      }
    }
  }

  // ---------------------------------------------------------------------------
  // Anchor links on prose headings
  // ---------------------------------------------------------------------------
  function initHeadingAnchors() {
    var prose = document.querySelector(".prose");
    if (!prose) return;
    prose.querySelectorAll("h2, h3, h4").forEach(function (h) {
      var id = h.id;
      if (!id) {
        id = h.textContent.trim()
          .toLowerCase()
          .replace(/[^\w\u4e00-\u9fff\s-]/g, "")
          .replace(/\s+/g, "-")
          .substring(0, 60);
        if (id) h.id = id;
      }
      if (!id) return;
      if (h.querySelector(".anchor")) return;
      var a = document.createElement("a");
      a.className = "anchor";
      a.href = "#" + id;
      a.setAttribute("aria-hidden", "true");
      a.textContent = "#";
      h.appendChild(a);
    });
  }

  // ---------------------------------------------------------------------------
  // Hero stats — expandable detail panels
  // ---------------------------------------------------------------------------
  function initHeroStats() {
    var root = document.querySelector("[data-hero-stats]");
    if (!root) return;

    var buttons = root.querySelectorAll("[data-hero-stat]");
    var detail = root.querySelector("[data-hero-stat-detail]");
    var panels = root.querySelectorAll("[data-hero-panel]");
    var active = null;

    function syncGroupLabel() {
      var group = root.querySelector(".hero__stats-row");
      if (!group) return;
      var lang = document.documentElement.getAttribute("data-lang") || "en";
      var label = group.getAttribute("data-aria-label-" + lang) || group.getAttribute("data-aria-label-en");
      if (label) group.setAttribute("aria-label", label);
    }

    function syncDetailHeight() {
      if (!detail) return;
      if (!detail.classList.contains("is-open")) {
        detail.style.maxHeight = "0px";
        return;
      }
      var panel = detail.querySelector("[data-hero-panel]:not([hidden])");
      if (!panel) return;
      detail.style.maxHeight = panel.scrollHeight + "px";
    }

    function closeDetail() {
      active = null;
      buttons.forEach(function (btn) {
        btn.classList.remove("is-active");
        btn.setAttribute("aria-expanded", "false");
      });
      if (detail) {
        detail.classList.remove("is-open");
        detail.setAttribute("aria-hidden", "true");
        detail.style.maxHeight = "0px";
      }
      panels.forEach(function (panel) { panel.setAttribute("hidden", ""); });
    }

    function openDetail(key, btn) {
      if (active === key) {
        closeDetail();
        return;
      }
      active = key;
      buttons.forEach(function (b) {
        var on = b === btn;
        b.classList.toggle("is-active", on);
        b.setAttribute("aria-expanded", on ? "true" : "false");
      });
      if (detail) {
        detail.classList.add("is-open");
        detail.setAttribute("aria-hidden", "false");
      }
      panels.forEach(function (panel) {
        var show = panel.getAttribute("data-hero-panel") === key;
        if (show) panel.removeAttribute("hidden");
        else panel.setAttribute("hidden", "");
      });
      if (btn) {
        btn.classList.remove("is-pulse");
        void btn.offsetWidth;
        btn.classList.add("is-pulse");
      }
      syncDetailHeight();
      scrollIntoViewIfNeeded(detail);
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        openDetail(btn.getAttribute("data-hero-stat"), btn);
      });
      btn.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openDetail(btn.getAttribute("data-hero-stat"), btn);
        }
      });
    });

    bindOutsideDismiss(root, function () { return !!active; }, closeDetail);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && active) closeDetail();
    });

    root.querySelectorAll("[data-hero-stat-link]").forEach(function (link) {
      link.addEventListener("click", function () { closeDetail(); });
    });

    window.addEventListener("resize", syncDetailHeight, { passive: true });
    window.addEventListener("orientationchange", function () {
      setTimeout(syncDetailHeight, 120);
    });

    syncGroupLabel();
    var langObserver = new MutationObserver(function () {
      syncGroupLabel();
      syncDetailHeight();
    });
    langObserver.observe(document.documentElement, { attributes: true, attributeFilter: ["data-lang"] });
  }

  // ---------------------------------------------------------------------------
  // Feature / value cards — click highlight
  // ---------------------------------------------------------------------------
  function initFeatureCards() {
    var grid = document.querySelector("[data-feature-grid]");
    if (!grid) return;

    var cards = grid.querySelectorAll("[data-feature-card]");
    var active = null;

    function deactivateAll() {
      active = null;
      cards.forEach(function (card) {
        card.classList.remove("is-active");
        card.setAttribute("aria-pressed", "false");
      });
    }

    function activate(card) {
      if (active === card) {
        deactivateAll();
        return;
      }
      active = card;
      cards.forEach(function (c) {
        var on = c === card;
        c.classList.toggle("is-active", on);
        c.setAttribute("aria-pressed", on ? "true" : "false");
      });
      card.classList.remove("is-pulse");
      void card.offsetWidth;
      card.classList.add("is-pulse");
      scrollIntoViewIfNeeded(card);
    }

    cards.forEach(function (card) {
      card.setAttribute("role", "button");
      card.setAttribute("aria-pressed", "false");
      card.addEventListener("click", function () { activate(card); });
      card.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          activate(card);
        }
      });
    });

    bindOutsideDismiss(grid, function () { return !!active; }, deactivateAll);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && active) deactivateAll();
    });
  }

  // ---------------------------------------------------------------------------
  // App Store button tooltip (touch tap to show)
  // ---------------------------------------------------------------------------
  function initAppStoreTooltips() {
    document.querySelectorAll(".app-hero__cta-tip.has-tooltip").forEach(function (wrap) {
      var link = wrap.querySelector("a");
      if (!link) return;

      function show() { wrap.classList.add("is-tooltip-visible"); }
      function hide() { wrap.classList.remove("is-tooltip-visible"); }
      function toggle() {
        wrap.classList.toggle("is-tooltip-visible");
      }

      link.addEventListener("click", function (e) {
        if (!isCoarsePointer()) return;
        if (!wrap.classList.contains("is-tooltip-visible")) {
          e.preventDefault();
          show();
        }
      });

      document.addEventListener("click", function (e) {
        if (!wrap.classList.contains("is-tooltip-visible")) return;
        if (wrap.contains(e.target)) return;
        hide();
      });
      document.addEventListener("touchend", function (e) {
        if (!wrap.classList.contains("is-tooltip-visible")) return;
        if (wrap.contains(e.target)) return;
        hide();
      }, { passive: true });

      link.addEventListener("keydown", function (e) {
        if (e.key === "Escape") hide();
      });
    });
  }

  // ---------------------------------------------------------------------------
  // Touch class — coarse pointer / mobile interaction hints
  // ---------------------------------------------------------------------------
  function initTouchClass() {
    var mq = window.matchMedia(COARSE_POINTER);
    function apply() {
      document.documentElement.classList.toggle("is-touch", mq.matches);
    }
    apply();
    if (mq.addEventListener) mq.addEventListener("change", apply);
    else if (mq.addListener) mq.addListener(apply);
  }

  // ---------------------------------------------------------------------------
  // App icons — swap to SVG fallback when App Store artwork fails
  // ---------------------------------------------------------------------------
  function initAppIcons() {
    document.querySelectorAll("[data-app-icon]").forEach(function (root) {
      var img = root.querySelector(".app-icon__img");
      if (!img) return;

      function showLoaded() {
        root.classList.add("is-loaded");
        root.classList.remove("is-fallback");
      }

      function showFallback() {
        root.classList.remove("is-loaded");
        root.classList.add("is-fallback");
        if (img.parentNode) img.parentNode.removeChild(img);
      }

      if (img.complete && img.naturalWidth > 0) {
        showLoaded();
        return;
      }

      img.addEventListener("load", showLoaded, { once: true });
      img.addEventListener("error", showFallback, { once: true });
    });
  }

  // ---------------------------------------------------------------------------
  // App switcher rail expand/collapse
  // ---------------------------------------------------------------------------
  function initAppSwitcher() {
    var rail = document.querySelector(".app-switcher");
    if (!rail) return;
    var chev = rail.querySelector(".app-switcher__chevron");
    if (!chev) return;
    var viewport = rail.querySelector("[data-app-switcher-viewport]");
    var items = rail.querySelector("[data-app-switcher-items]");
    var RAIL_MARGIN = 12;

    function headerHeight() {
      var v = getComputedStyle(document.documentElement).getPropertyValue("--header-height");
      return parseFloat(v) || 56;
    }

    function syncRailPosition() {
      var margin = RAIL_MARGIN;
      var minTop = headerHeight() + margin;
      var maxBottom = window.innerHeight - margin;
      var h = rail.offsetHeight;
      if (!h) return;
      var idealTop = (window.innerHeight - h) * 0.5;
      var top = Math.max(minTop, Math.min(idealTop, maxBottom - h));
      rail.style.top = top + "px";
    }

    function updateScrollFades() {
      if (!viewport || !items) return;
      var maxScroll = items.scrollHeight - items.clientHeight;
      var hasOverflow = maxScroll > 2;
      rail.classList.toggle("has-overflow", hasOverflow);
      viewport.classList.toggle("is-scrolled", hasOverflow && items.scrollTop > 2);
      viewport.classList.toggle("has-more-below", hasOverflow && items.scrollTop < maxScroll - 2);
      syncRailPosition();
    }

    function scheduleLayoutSync() {
      requestAnimationFrame(function () {
        updateScrollFades();
      });
    }

    chev.addEventListener("click", function () {
      rail.classList.toggle("is-expanded");
      chev.setAttribute("aria-expanded", rail.classList.contains("is-expanded") ? "true" : "false");
      scheduleLayoutSync();
    });
    document.addEventListener("click", function (e) {
      if (!rail.contains(e.target) && rail.classList.contains("is-expanded")) {
        rail.classList.remove("is-expanded");
        chev.setAttribute("aria-expanded", "false");
        scheduleLayoutSync();
      }
    });

    if (items && viewport) {
      items.addEventListener("scroll", updateScrollFades, { passive: true });

      // Desktop: wheel over the rail scrolls the list instead of the page.
      rail.addEventListener("wheel", function (e) {
        if (items.scrollHeight <= items.clientHeight + 1) return;
        var dy = e.deltaY;
        if (!dy) return;
        var atTop = items.scrollTop <= 0;
        var atBottom = items.scrollTop + items.clientHeight >= items.scrollHeight - 1;
        if ((dy < 0 && atTop) || (dy > 0 && atBottom)) return;
        e.preventDefault();
        items.scrollTop += dy;
      }, { passive: false });

      // Touch (iPad/iOS Safari): drive the list scroll directly so the gesture
      // never leaks to the page behind the fixed rail. Native touch scrolling is
      // unreliable here (fixed container + flex height + overflow-x hidden), so
      // we scroll manually and add a light momentum flick.
      var touchLastY = 0, touchPrevY = 0, touchPrevT = 0, touchVel = 0, momentumRAF = 0;

      function stopMomentum() {
        if (momentumRAF) { cancelAnimationFrame(momentumRAF); momentumRAF = 0; }
      }

      items.addEventListener("touchstart", function (e) {
        stopMomentum();
        if (!e.touches || e.touches.length !== 1) return;
        touchLastY = touchPrevY = e.touches[0].clientY;
        touchPrevT = e.timeStamp;
        touchVel = 0;
      }, { passive: true });

      items.addEventListener("touchmove", function (e) {
        if (!e.touches || e.touches.length !== 1) return;
        var max = items.scrollHeight - items.clientHeight;
        if (max <= 0) return; // nothing to scroll → let the page move naturally
        var y = e.touches[0].clientY;
        var before = items.scrollTop;
        var next = Math.max(0, Math.min(before + (touchLastY - y), max));
        if (next !== before) {
          items.scrollTop = next;
          if (e.cancelable) e.preventDefault(); // keep the page still
        }
        var dt = e.timeStamp - touchPrevT;
        if (dt > 0) touchVel = (touchPrevY - y) / dt; // px per ms
        touchLastY = y;
        touchPrevY = y;
        touchPrevT = e.timeStamp;
      }, { passive: false });

      items.addEventListener("touchend", function () {
        var max = items.scrollHeight - items.clientHeight;
        if (max <= 0 || Math.abs(touchVel) < 0.03) return;
        var v = touchVel * 16; // approx px per frame
        function step() {
          v *= 0.95;
          var before = items.scrollTop;
          var next = Math.max(0, Math.min(before + v, max));
          items.scrollTop = next;
          if (next === before || Math.abs(v) < 0.5) { momentumRAF = 0; return; }
          momentumRAF = requestAnimationFrame(step);
        }
        momentumRAF = requestAnimationFrame(step);
      }, { passive: true });

      window.addEventListener("resize", scheduleLayoutSync, { passive: true });
      window.addEventListener("orientationchange", function () {
        setTimeout(scheduleLayoutSync, 120);
      });

      if ("ResizeObserver" in window) {
        var ro = new ResizeObserver(scheduleLayoutSync);
        ro.observe(rail);
        ro.observe(viewport);
        ro.observe(items);
      }

      scheduleLayoutSync();
    } else {
      syncRailPosition();
      window.addEventListener("resize", syncRailPosition, { passive: true });
    }
  }

  // ---------------------------------------------------------------------------
  // Homepage app grid — compact cards, accordion, expand/collapse all
  // ---------------------------------------------------------------------------
  function initCollectionsPage() {
    var root = document.querySelector("[data-collections-page]");
    if (!root) return;

    var chips = root.querySelector("[data-collections-chips]");
    var buttons = chips ? Array.prototype.slice.call(chips.querySelectorAll("[data-collection-filter]")) : [];
    var blocks = Array.prototype.slice.call(root.querySelectorAll("[data-collection-block]"));
    var emptyEl = root.querySelector("[data-collections-empty]");
    var validIds = {};
    blocks.forEach(function (block) {
      validIds[block.getAttribute("data-collection-block")] = true;
    });

    function syncChipAria() {
      if (!chips) return;
      var lang = document.documentElement.getAttribute("data-lang") || "en";
      var label = chips.getAttribute("data-aria-label-" + lang) || chips.getAttribute("data-aria-label-en");
      if (label) chips.setAttribute("aria-label", label);
    }

    function applyFilter(id, opts) {
      var filter = id && validIds[id] ? id : "all";
      var visible = 0;

      buttons.forEach(function (btn) {
        var active = btn.getAttribute("data-collection-filter") === filter;
        btn.classList.toggle("is-active", active);
        btn.setAttribute("aria-selected", active ? "true" : "false");
      });

      blocks.forEach(function (block) {
        var blockId = block.getAttribute("data-collection-block");
        var show = filter === "all" || blockId === filter;
        block.hidden = !show;
        if (show) visible += 1;
      });

      if (emptyEl) emptyEl.hidden = visible > 0;

      document.dispatchEvent(new CustomEvent("ihtc:collections-filter"));

      if (opts && opts.updateHash) {
        var nextHash = filter === "all" ? "" : "#" + filter;
        if ((window.location.hash || "") !== nextHash) {
          if (nextHash) {
            history.replaceState(null, "", nextHash);
          } else {
            history.replaceState(null, "", window.location.pathname + window.location.search);
          }
        }
      }

      if (opts && opts.scroll && filter !== "all") {
        var target = root.querySelector('[data-collection-block="' + filter + '"]');
        if (target) {
          requestAnimationFrame(function () {
            target.scrollIntoView({ behavior: "smooth", block: "start" });
          });
        }
      }
    }

    function filterFromHash() {
      var raw = (window.location.hash || "").replace(/^#/, "");
      applyFilter(raw || "all", { updateHash: false, scroll: !!raw });
    }

    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        applyFilter(btn.getAttribute("data-collection-filter"), { updateHash: true, scroll: true });
      });
    });

    window.addEventListener("hashchange", filterFromHash);
    syncChipAria();
    filterFromHash();
  }

  function initAppGrid() {
    var grid = document.querySelector("[data-app-grid]");
    if (!grid) return;

    var STORAGE_MODE = "ihtc.appGridMode";
    var cards = Array.prototype.slice.call(grid.querySelectorAll("[data-app-card]"));
    if (!cards.length) return;

    var toolbar = document.querySelector("[data-app-grid-toolbar]");
    var expandAllBtn = document.querySelector("[data-app-expand-all]");
    var collapseAllBtn = document.querySelector("[data-app-collapse-all]");
    var mode = "compact"; // compact = accordion; expanded = all open

    function currentLang() {
      return document.documentElement.getAttribute("data-lang") ||
        document.documentElement.getAttribute("lang") ||
        "en";
    }

    function syncToolbarGroupLabel() {
      if (!toolbar) return;
      var group = toolbar.querySelector(".app-grid-toolbar__actions");
      if (!group) return;
      var lang = currentLang();
      var label = group.getAttribute("data-aria-label-" + lang) ||
        group.getAttribute("data-aria-label-en");
      if (label) group.setAttribute("aria-label", label);
    }

    function syncToggleLabel(btn, expanded) {
      if (!btn) return;
      var lang = currentLang();
      var key = expanded ? "data-label-collapse-" : "data-label-expand-";
      var label = btn.getAttribute(key + lang) ||
        btn.getAttribute(key + "en") ||
        (expanded ? "Hide details" : "Show details");
      btn.setAttribute("aria-label", label);
      btn.setAttribute("title", label);
    }

    function setCardExpanded(card, expanded) {
      var btn = card.querySelector("[data-app-card-toggle]");
      var details = card.querySelector("[data-app-card-details]");
      card.classList.toggle("is-expanded", expanded);
      if (btn) {
        btn.setAttribute("aria-expanded", expanded ? "true" : "false");
        syncToggleLabel(btn, expanded);
      }
      if (details) {
        details.setAttribute("aria-hidden", expanded ? "false" : "true");
        if ("inert" in details) details.inert = !expanded;
      }
    }

    function countExpanded() {
      return cards.filter(function (c) {
        return c.classList.contains("is-expanded") && isCardVisible(c);
      }).length;
    }

    function isCardVisible(card) {
      var block = card.closest("[data-collection-block]");
      if (block && block.hidden) return false;
      return true;
    }

    function visibleCards() {
      return cards.filter(isCardVisible);
    }

    function syncToolbarButtons() {
      var visible = visibleCards();
      var n = visible.filter(function (c) { return c.classList.contains("is-expanded"); }).length;
      var total = visible.length;
      if (expandAllBtn) {
        var allOpen = total > 0 && n === total;
        expandAllBtn.disabled = allOpen || total === 0;
        expandAllBtn.setAttribute("aria-disabled", expandAllBtn.disabled ? "true" : "false");
      }
      if (collapseAllBtn) {
        var noneOpen = n === 0;
        collapseAllBtn.disabled = noneOpen;
        collapseAllBtn.setAttribute("aria-disabled", noneOpen ? "true" : "false");
      }
    }

    function expandAll() {
      mode = "expanded";
      visibleCards().forEach(function (card) { setCardExpanded(card, true); });
      safeSet(STORAGE_MODE, "expanded");
      syncToolbarButtons();
    }

    function collapseAll() {
      mode = "compact";
      cards.forEach(function (card) { setCardExpanded(card, false); });
      safeSet(STORAGE_MODE, "compact");
      syncToolbarButtons();
    }

    function toggleCard(card) {
      var willOpen = !card.classList.contains("is-expanded");
      if (willOpen) {
        if (mode === "compact") {
          visibleCards().forEach(function (other) {
            if (other !== card) setCardExpanded(other, false);
          });
        }
        setCardExpanded(card, true);
        if (isCoarsePointer() || isNarrowViewport()) {
          scrollIntoViewIfNeeded(card);
        }
      } else {
        setCardExpanded(card, false);
        // Leaving expand-all mode when user collapses one card.
        if (mode === "expanded" && countExpanded() < visibleCards().length) {
          mode = "compact";
          safeSet(STORAGE_MODE, "compact");
        }
      }
      syncToolbarButtons();
    }

    cards.forEach(function (card) {
      setCardExpanded(card, false);
      var btn = card.querySelector("[data-app-card-toggle]");
      if (!btn) return;
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        toggleCard(card);
      });
    });

    if (expandAllBtn) expandAllBtn.addEventListener("click", expandAll);
    if (collapseAllBtn) collapseAllBtn.addEventListener("click", collapseAll);

    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      var openCards = visibleCards().filter(function (c) { return c.classList.contains("is-expanded"); });
      if (!openCards.length) return;
      // Prefer collapsing the card that contains focus.
      var focused = document.activeElement;
      var host = focused && focused.closest ? focused.closest("[data-app-card]") : null;
      if (host && host.classList.contains("is-expanded") && isCardVisible(host)) {
        setCardExpanded(host, false);
      } else if (mode === "expanded") {
        collapseAll();
        return;
      } else {
        setCardExpanded(openCards[openCards.length - 1], false);
      }
      if (mode === "expanded" && countExpanded() < visibleCards().length) {
        mode = "compact";
        safeSet(STORAGE_MODE, "compact");
      }
      syncToolbarButtons();
    });

    document.addEventListener("ihtc:collections-filter", syncToolbarButtons);

    var langObserver = new MutationObserver(function () {
      syncToolbarGroupLabel();
      cards.forEach(function (card) {
        var btn = card.querySelector("[data-app-card-toggle]");
        syncToggleLabel(btn, card.classList.contains("is-expanded"));
      });
    });
    langObserver.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-lang", "lang"]
    });

    syncToolbarGroupLabel();

    var stored = safeGet(STORAGE_MODE);
    if (stored === "expanded") expandAll();
    else {
      mode = "compact";
      syncToolbarButtons();
    }
  }

  // ---------------------------------------------------------------------------
  // Toast
  // ---------------------------------------------------------------------------
  function showToast(text, dur) {
    if (!text) return;
    var toast = document.querySelector(".toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "toast";
      document.body.appendChild(toast);
    }
    toast.textContent = text;
    requestAnimationFrame(function () { toast.classList.add("is-visible"); });
    clearTimeout(showToast._timer);
    showToast._timer = setTimeout(function () { toast.classList.remove("is-visible"); }, dur || 1800);
  }

  // ---------------------------------------------------------------------------
  // Helpers
  // ---------------------------------------------------------------------------
  function safeGet(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function safeSet(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  // ---------------------------------------------------------------------------
  // Boot
  // ---------------------------------------------------------------------------
  function boot() {
    applyLang(detectLang(), { persist: false });
    applyTheme(detectTheme(), { persist: false });
    initDropdowns();
    initLangToggles();
    initThemeToggles();
    initMobileDrawer();
    initReveal();
    initHeadingAnchors();
    initGuideNav();
    initAppIcons();
    initAppSwitcher();
    initTouchClass();
    initAppStoreTooltips();
    initHeroStats();
    initFeatureCards();
    initAppGrid();
    initCollectionsPage();
    document.documentElement.classList.add("is-ready");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
