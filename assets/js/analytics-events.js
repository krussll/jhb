/**
 * Promotional and Core Pathway Click Tracking for Jack High Bowls.
 * Dispatches 'promo_click' events with placement and destination URL
 * to Google Analytics 4 (gtag) via event delegation.
 */
(function () {
  'use strict';

  function initAnalyticsTracking() {
    document.addEventListener(
      'click',
      function (event) {
        var target = event.target;
        if (!target || typeof target.closest !== 'function') {
          return;
        }

        var trackElement = target.closest('[data-track]');
        if (!trackElement) {
          return;
        }

        var placement = trackElement.getAttribute('data-track');
        if (!placement) {
          return;
        }

        var link =
          target.closest('a') ||
          (trackElement.tagName === 'A'
            ? trackElement
            : trackElement.querySelector('a'));

        var linkUrl = '';
        if (trackElement.hasAttribute('data-track-url')) {
          linkUrl = trackElement.getAttribute('data-track-url') || '';
        } else if (link) {
          linkUrl = link.getAttribute('href') || link.href || '';
        }

        if (typeof window.gtag === 'function') {
          window.gtag('event', 'promo_click', {
            placement: placement,
            link_url: linkUrl
          });
        }
      },
      { passive: true }
    );
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnalyticsTracking);
  } else {
    initAnalyticsTracking();
  }
})();
