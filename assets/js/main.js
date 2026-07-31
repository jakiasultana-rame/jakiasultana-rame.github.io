/* ============================================================
   Jakia Sultana — Academic Portfolio JS
   ============================================================ */

(function () {
  'use strict';

  // --- Mobile nav toggle ---
  const toggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
      toggle.classList.toggle('active');
    });

    // Close menu on link click
    navLinks.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        navLinks.classList.remove('open');
        toggle.classList.remove('active');
      });
    });
  }

  // --- Navbar background on scroll ---
  const nav = document.getElementById('navbar');
  if (nav) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 60) {
        nav.style.background = 'rgba(245,246,247,0.98)';
        nav.style.boxShadow = '0 1px 8px rgba(0,0,0,0.04)';
      } else {
        nav.style.background = 'rgba(245,246,247,0.92)';
        nav.style.boxShadow = 'none';
      }
    });
  }

  // --- Scroll fade-in animations ---
  var fadeElements = document.querySelectorAll(
    '.section-title, .section-label, .about-text, .stat-card, ' +
    '.project-card, .pub-item, .field-project, .timeline-item, ' +
    '.award-group, .contact-grid, .cv-block'
  );

  fadeElements.forEach(function (el) {
    el.classList.add('fade-in');
  });

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
  );

  fadeElements.forEach(function (el) {
    observer.observe(el);
  });

  // --- Active nav link on scroll ---
  var sections = document.querySelectorAll('section[id]');
  var navItems = document.querySelectorAll('.nav-links a');

  window.addEventListener('scroll', function () {
    var scrollPos = window.scrollY + 100;

    sections.forEach(function (section) {
      var top = section.offsetTop;
      var height = section.offsetHeight;
      var id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navItems.forEach(function (item) {
          item.style.color = '';
          if (item.getAttribute('href') === '#' + id) {
            item.style.color = '#3D7A8A';
          }
        });
      }
    });
  });

})();
