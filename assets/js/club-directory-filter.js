/**
 * Jack High Bowls - Club Directory Instant Filter & Search Component
 * Enables live client-side filtering by surface type (Indoor/Outdoor/Beginner) and instant text search.
 */
(function () {
  'use strict';

  function initClubDirectory() {
    var components = document.querySelectorAll('[data-component="club-directory"]');
    if (!components.length) return;

    components.forEach(function (container) {
      var searchInput = container.querySelector('#club-directory-search');
      var clearBtn = container.querySelector('#club-search-clear');
      var filterPills = container.querySelectorAll('.club-filter-pill');
      var grid = container.querySelector('#club-directory-grid');
      var countCurrent = container.querySelector('.club-count-current');
      var noResults = container.querySelector('#club-directory-no-results');
      var resetBtn = container.querySelector('#club-reset-filters');

      if (!grid) return;
      var cards = grid.querySelectorAll('.club-card');
      var activeFilter = 'all';

      function applyFilter() {
        var query = searchInput ? searchInput.value.trim().toLowerCase() : '';
        var visibleCount = 0;

        // Toggle clear button visibility
        if (clearBtn) {
          if (query.length > 0) {
            clearBtn.classList.remove('d-none');
          } else {
            clearBtn.classList.add('d-none');
          }
        }

        cards.forEach(function (card) {
          var name = card.getAttribute('data-name') || '';
          var area = card.getAttribute('data-area') || '';
          var postcode = card.getAttribute('data-postcode') || '';
          var city = card.getAttribute('data-city') || '';
          var isIndoor = card.getAttribute('data-indoor') === 'true';
          var isOutdoor = card.getAttribute('data-outdoor') === 'true';
          var isBeginner = card.getAttribute('data-beginner') === 'true';

          var matchesPill = true;
          if (activeFilter === 'indoor') {
            matchesPill = isIndoor;
          } else if (activeFilter === 'outdoor') {
            matchesPill = isOutdoor;
          } else if (activeFilter === 'beginner') {
            matchesPill = isBeginner;
          }

          var matchesQuery = true;
          if (query.length > 0) {
            matchesQuery =
              name.indexOf(query) !== -1 ||
              area.indexOf(query) !== -1 ||
              postcode.indexOf(query) !== -1 ||
              city.indexOf(query) !== -1;
          }

          if (matchesPill && matchesQuery) {
            card.style.display = '';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        // Update counter
        if (countCurrent) {
          countCurrent.textContent = visibleCount;
        }

        // Toggle no-results message
        if (noResults) {
          if (visibleCount === 0) {
            noResults.classList.remove('d-none');
            grid.classList.add('d-none');
          } else {
            noResults.classList.add('d-none');
            grid.classList.remove('d-none');
          }
        }
      }

      // Search input listener
      if (searchInput) {
        searchInput.addEventListener('input', applyFilter);
      }

      // Clear search button listener
      if (clearBtn) {
        clearBtn.addEventListener('click', function () {
          if (searchInput) {
            searchInput.value = '';
            searchInput.focus();
            applyFilter();
          }
        });
      }

      // Filter pill buttons
      filterPills.forEach(function (pill) {
        pill.addEventListener('click', function () {
          filterPills.forEach(function (p) {
            p.classList.remove('club-filter-pill--active');
            p.setAttribute('aria-pressed', 'false');
          });
          pill.classList.add('club-filter-pill--active');
          pill.setAttribute('aria-pressed', 'true');
          activeFilter = pill.getAttribute('data-filter') || 'all';
          applyFilter();
        });
      });

      // Reset filters button in no-results container
      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          if (searchInput) {
            searchInput.value = '';
          }
          filterPills.forEach(function (p) {
            if (p.getAttribute('data-filter') === 'all') {
              p.classList.add('club-filter-pill--active');
              p.setAttribute('aria-pressed', 'true');
            } else {
              p.classList.remove('club-filter-pill--active');
              p.setAttribute('aria-pressed', 'false');
            }
          });
          activeFilter = 'all';
          applyFilter();
          if (searchInput) {
            searchInput.focus();
          }
        });
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initClubDirectory);
  } else {
    initClubDirectory();
  }
})();

