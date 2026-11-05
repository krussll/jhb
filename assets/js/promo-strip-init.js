/**
 * Synchronous promo strip pre-render initializer.
 * Runs in <head> before <body> is painted to prevent cumulative layout shift (CLS).
 */
(function () {
  'use strict';
  try {
    if (localStorage.getItem('jhb_promo_strip_dismissed') === 'true') {
      document.documentElement.classList.add('promo-dismissed');
    }
  } catch (e) {
    // localStorage might be unavailable or restricted
  }
})();

