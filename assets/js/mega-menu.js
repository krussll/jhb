/**
 * Accessible Mega-Menu & Dropdown interactions for Jack High Bowls.
 * Enhances Bootstrap dropdown with keyboard dismiss (Esc/Tab focusout)
 * and pointer hover preview on desktop.
 */
(function () {
  'use strict';

  function initMegaMenu() {
    var $navItem = $('.choose-bowls-nav');
    if (!$navItem.length) {
      return;
    }

    var $toggle = $navItem.find('[data-toggle="dropdown"]');
    var hoverTimer = null;

    var isDesktopPointer = function () {
      return (
        window.innerWidth >= 992 &&
        window.matchMedia &&
        window.matchMedia('(hover: hover)').matches
      );
    };

    // Desktop hover enhancement
    $navItem
      .on('mouseenter', function () {
        if (isDesktopPointer()) {
          clearTimeout(hoverTimer);
          if (!$navItem.hasClass('show')) {
            $toggle.dropdown('toggle');
          }
        }
      })
      .on('mouseleave', function () {
        if (isDesktopPointer()) {
          clearTimeout(hoverTimer);
          hoverTimer = setTimeout(function () {
            if ($navItem.hasClass('show')) {
              $toggle.dropdown('toggle');
            }
          }, 150);
        }
      });

    // Close when focus leaves the dropdown completely (keyboard Tab out)
    $navItem.on('focusout', function () {
      setTimeout(function () {
        if (!$navItem.find(':focus').length && $navItem.hasClass('show')) {
          $toggle.dropdown('toggle');
        }
      }, 50);
    });

    // Close on Escape key and return focus to toggle button
    $navItem.on('keydown', function (e) {
      if (e.key === 'Escape' || e.key === 'Esc' || e.keyCode === 27) {
        if ($navItem.hasClass('show')) {
          e.preventDefault();
          e.stopPropagation();
          $toggle.dropdown('toggle');
          $toggle.focus();
        }
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMegaMenu);
  } else {
    initMegaMenu();
  }
})();

