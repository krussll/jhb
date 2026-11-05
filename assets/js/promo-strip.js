/**
 * Interactive promo strip module for Jack High Bowls.
 * Handles carousel rotation, pause/play, keyboard controls, and dismissal.
 * WCAG 2.2.2 compliant (pause/stop/hide and prefers-reduced-motion).
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'jhb_promo_strip_dismissed';
  var ROTATION_INTERVAL = 7500; // 7.5 seconds per slide

  function initPromoStrip() {
    var strip = document.getElementById('promo-strip');
    if (!strip) {
      return;
    }

    // Double-check localStorage dismissal
    try {
      if (localStorage.getItem(STORAGE_KEY) === 'true') {
        document.documentElement.classList.add('promo-dismissed');
        return;
      }
    } catch (e) {
      // Ignore storage error
    }

    var items = strip.querySelectorAll('.promo-strip__item');
    var liveRegion = document.getElementById('promo-strip-live');
    var prevBtn = strip.querySelector('[data-promo-action="prev"]');
    var nextBtn = strip.querySelector('[data-promo-action="next"]');
    var pauseBtn = strip.querySelector('[data-promo-action="pause"]');
    var closeBtn = strip.querySelector('[data-promo-action="dismiss"]');
    var iconPause = strip.querySelector('.promo-strip__icon-pause');
    var iconPlay = strip.querySelector('.promo-strip__icon-play');

    var currentIndex = 0;
    var timerId = null;
    var isUserPaused = false;
    var isHoveredOrFocused = false;

    var prefersReducedMotion = false;
    if (window.matchMedia) {
      var motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
      prefersReducedMotion = motionQuery.matches;
      if (motionQuery.addEventListener) {
        motionQuery.addEventListener('change', function (e) {
          prefersReducedMotion = e.matches;
          if (prefersReducedMotion) {
            stopAutoRotation();
            setPauseButtonState(true);
          } else if (!isUserPaused && !isHoveredOrFocused) {
            startAutoRotation();
            setPauseButtonState(false);
          }
        });
      }
    }

    function showSlide(index, announce) {
      if (!items.length) {
        return;
      }
      var newIndex = (index + items.length) % items.length;

      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        if (i === newIndex) {
          item.classList.add('is-active');
          item.removeAttribute('hidden');
          item.removeAttribute('aria-hidden');
        } else {
          item.classList.remove('is-active');
          item.setAttribute('hidden', '');
          item.setAttribute('aria-hidden', 'true');
        }
      }

      currentIndex = newIndex;

      if (announce && liveRegion) {
        liveRegion.setAttribute('aria-live', 'polite');
        setTimeout(function () {
          liveRegion.setAttribute('aria-live', 'off');
        }, 1000);
      }
    }

    function startAutoRotation() {
      if (prefersReducedMotion || isUserPaused || isHoveredOrFocused || items.length <= 1) {
        return;
      }
      stopAutoRotation();
      timerId = setInterval(function () {
        showSlide(currentIndex + 1, false);
      }, ROTATION_INTERVAL);
    }

    function stopAutoRotation() {
      if (timerId) {
        clearInterval(timerId);
        timerId = null;
      }
    }

    function setPauseButtonState(paused) {
      if (!pauseBtn) {
        return;
      }
      if (paused) {
        if (iconPause) iconPause.style.display = 'none';
        if (iconPlay) iconPlay.style.display = 'inline-block';
        pauseBtn.setAttribute('aria-label', 'Resume announcement rotation');
        pauseBtn.setAttribute('title', 'Resume announcement rotation');
      } else {
        if (iconPause) iconPause.style.display = 'inline-block';
        if (iconPlay) iconPlay.style.display = 'none';
        pauseBtn.setAttribute('aria-label', 'Pause announcement rotation');
        pauseBtn.setAttribute('title', 'Pause announcement rotation');
      }
    }

    function dismissStrip() {
      stopAutoRotation();
      try {
        localStorage.setItem(STORAGE_KEY, 'true');
      } catch (e) {}

      document.documentElement.classList.add('promo-dismissed');

      // Shift focus to main navigation brand or content to prevent lost focus
      var nextFocus = document.querySelector('#mainNav .navbar-brand') || document.querySelector('a, button');
      if (nextFocus && typeof nextFocus.focus === 'function') {
        nextFocus.focus();
      }
    }

    // Dismiss button click handler
    if (closeBtn) {
      closeBtn.addEventListener('click', function (e) {
        e.preventDefault();
        dismissStrip();
      });
    }

    // Prev / Next button handlers
    if (prevBtn) {
      prevBtn.addEventListener('click', function (e) {
        e.preventDefault();
        showSlide(currentIndex - 1, true);
        if (!isUserPaused && !prefersReducedMotion) {
          startAutoRotation();
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function (e) {
        e.preventDefault();
        showSlide(currentIndex + 1, true);
        if (!isUserPaused && !prefersReducedMotion) {
          startAutoRotation();
        }
      });
    }

    // Pause button toggle
    if (pauseBtn) {
      pauseBtn.addEventListener('click', function (e) {
        e.preventDefault();
        isUserPaused = !isUserPaused;
        if (isUserPaused) {
          stopAutoRotation();
          setPauseButtonState(true);
        } else {
          setPauseButtonState(false);
          startAutoRotation();
        }
      });
    }

    // Pause on hover
    strip.addEventListener('mouseenter', function () {
      isHoveredOrFocused = true;
      stopAutoRotation();
    });

    strip.addEventListener('mouseleave', function () {
      isHoveredOrFocused = false;
      if (!isUserPaused && !prefersReducedMotion) {
        startAutoRotation();
      }
    });

    // Pause on focus
    strip.addEventListener('focusin', function () {
      isHoveredOrFocused = true;
      stopAutoRotation();
    });

    strip.addEventListener('focusout', function (e) {
      // Check if the newly focused element is outside the strip
      if (!strip.contains(e.relatedTarget)) {
        isHoveredOrFocused = false;
        if (!isUserPaused && !prefersReducedMotion) {
          startAutoRotation();
        }
      }
    });

    // Keyboard navigation: Escape to dismiss, Arrow keys to switch slides
    strip.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' || e.key === 'Esc') {
        e.preventDefault();
        dismissStrip();
      } else if (e.key === 'ArrowLeft') {
        if (items.length > 1) {
          e.preventDefault();
          showSlide(currentIndex - 1, true);
        }
      } else if (e.key === 'ArrowRight') {
        if (items.length > 1) {
          e.preventDefault();
          showSlide(currentIndex + 1, true);
        }
      }
    });

    // Start auto-rotation if not reduced-motion
    if (prefersReducedMotion) {
      isUserPaused = true;
      setPauseButtonState(true);
    } else {
      startAutoRotation();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPromoStrip);
  } else {
    initPromoStrip();
  }
})();

