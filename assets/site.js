(function () {
  var header = document.getElementById("header");
  if (header) {
    var onScroll = function () {
      var scrolled = window.scrollY > 50;
      header.classList.toggle("bg-dark/90", scrolled);
      header.classList.toggle("backdrop-blur-xl", scrolled);
      header.classList.toggle("border-b", scrolled);
      header.classList.toggle("border-white/5", scrolled);
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  var menuBtn = document.getElementById("menu-btn");
  var mobileMenu = document.getElementById("mobile-menu");
  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener("click", function () {
      var open = mobileMenu.classList.toggle("hidden") === false;
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    mobileMenu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        mobileMenu.classList.add("hidden");
        menuBtn.setAttribute("aria-expanded", "false");
      });
    });
  }

  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    document.querySelectorAll(".reveal").forEach(function (el) { observer.observe(el); });
  } else {
    document.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("visible"); });
  }

  function track(name, params) {
    if (typeof window.gtag === "function") {
      window.gtag("event", name, params || {});
      return;
    }
    window.dataLayer = window.dataLayer || [];
    var payload = { event: name };
    if (params) {
      Object.keys(params).forEach(function (key) { payload[key] = params[key]; });
    }
    window.dataLayer.push(payload);
  }

  document.addEventListener("click", function (event) {
    var tel = event.target.closest && event.target.closest('a[href^="tel:"]');
    if (tel) {
      track("click_to_call", {
        link_url: tel.getAttribute("href"),
        page_path: location.pathname
      });
    }
    var checkout = event.target.closest && event.target.closest('a[href*="buy.stripe.com"]');
    if (checkout) {
      var value = checkout.dataset.value ? Number(checkout.dataset.value) : undefined;
      track("begin_checkout", {
        currency: "USD",
        value: value,
        page_path: location.pathname,
        items: [{
          item_name: checkout.dataset.itemName || checkout.dataset.plan || "website package",
          price: value
        }]
      });
    }
    var review = event.target.closest && event.target.closest("[data-review-link]");
    if (review) {
      track("click_review_link", {
        link_url: review.getAttribute("href"),
        link_kind: review.getAttribute("data-review-link"),
        page_path: location.pathname
      });
    }
  });

  var cfg = window.CRRE_SITE || {};
  function realUrl(value) {
    return typeof value === "string" && value && value.indexOf("TODO") !== 0;
  }

  document.querySelectorAll("[data-google-rating]").forEach(function (el) {
    if (cfg.googleRating) el.textContent = String(cfg.googleRating);
  });
  document.querySelectorAll("[data-google-review-count]").forEach(function (el) {
    if (cfg.googleReviewCount !== undefined && cfg.googleReviewCount !== null && cfg.googleReviewCount !== "") {
      el.textContent = String(cfg.googleReviewCount);
    }
  });

  document.querySelectorAll("[data-review-link]").forEach(function (link) {
    var kind = link.getAttribute("data-review-link");
    var url = kind === "profile" ? cfg.googleBusinessProfileUrl : cfg.googleReviewsUrl;
    if (realUrl(url)) {
      link.href = url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.removeAttribute("aria-disabled");
    }
  });

  var reviewList = document.getElementById("review-list");
  if (reviewList && Array.isArray(cfg.reviews)) {
    var ready = cfg.reviews.filter(function (item) {
      return item && typeof item.quote === "string" && item.quote.indexOf("PLACEHOLDER") !== 0 && item.quote.trim();
    });
    if (ready.length) {
      reviewList.innerHTML = ready.map(function (item) {
        var quote = escapeHtml(item.quote);
        var author = escapeHtml(item.author || "");
        var detail = escapeHtml(item.detail || "");
        return '<figure class="glass rounded-2xl p-6"><blockquote class="text-gray-200 leading-relaxed">“' + quote + '”</blockquote><figcaption class="mt-4 text-sm text-gray-400">' + author + (detail ? " · " + detail : "") + "</figcaption></figure>";
      }).join("");
    }
  }

  if (realUrl(cfg.googleBusinessProfileUrl)) {
    document.querySelectorAll('script[type="application/ld+json"]').forEach(function (node) {
      try {
        var data = JSON.parse(node.textContent);
        var list = Array.isArray(data) ? data : [data];
        var changed = false;
        list.forEach(function (block) {
          if (block && Object.prototype.hasOwnProperty.call(block, "sameAs")) {
            block.sameAs = [cfg.googleBusinessProfileUrl];
            changed = true;
          }
        });
        if (changed) node.textContent = JSON.stringify(Array.isArray(data) ? list : list[0]);
      } catch (err) { /* leave the original block if it is not JSON */ }
    });
  }

  var serviceSelect = document.getElementById("service-select");
  if (serviceSelect) {
    var params = new URLSearchParams(window.location.search);
    var requested = params.get("plan");
    if (requested) {
      var map = { starter: "website-starter", business: "website-business", pro: "website-pro" };
      var val = map[requested] || requested;
      if ([].some.call(serviceSelect.options, function (option) { return option.value === val; })) {
        serviceSelect.value = val;
      }
    }
  }

  var formReadyAt = Date.now();
  document.querySelectorAll("form[data-lead-form]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var hp = form.querySelector('[name="company_website"]');
      if (hp && hp.value.trim()) {
        if (btn) {
          btn.textContent = "Message Sent ✓";
          btn.disabled = true;
          btn.classList.remove("bg-accent-strong");
          btn.classList.add("bg-green-700");
        }
        form.reset();
        return;
      }
      var phone = form.querySelector('[name="phone"]');
      var smsConsent = form.querySelector('[name="sms_consent"]');
      if (smsConsent && smsConsent.checked && phone && !phone.value.trim()) {
        phone.focus();
        phone.setCustomValidity("Please provide a phone number to receive marketing SMS.");
        phone.reportValidity();
        return;
      }
      if (phone) phone.setCustomValidity("");
      if (btn) {
        btn.textContent = "Sending...";
        btn.disabled = true;
      }
      var wait = 3000 - (Date.now() - formReadyAt);
      var send = function () {
        fetch(form.action, {
          method: "POST",
          body: new URLSearchParams(new FormData(form)),
          headers: { Accept: "application/json" }
        }).then(function (res) {
          if (!res.ok) throw new Error("bad status");
          track("generate_lead", {
            method: "contact_form",
            form_id: form.id || "contact-form",
            page_path: location.pathname,
            service: (form.querySelector('[name="service"]') || {}).value || ""
          });
          if (btn) {
            btn.textContent = "Message Sent ✓";
            btn.classList.remove("bg-accent-strong");
            btn.classList.add("bg-green-700");
          }
          form.reset();
        }).catch(function () {
          if (btn) {
            btn.textContent = "Error — Try Again";
            btn.disabled = false;
          }
        });
      };
      if (wait > 0) setTimeout(send, wait);
      else send();
    });
  });

  function escapeHtml(value) {
    return String(value).replace(/[&<>"']/g, function (ch) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch];
    });
  }
})();
