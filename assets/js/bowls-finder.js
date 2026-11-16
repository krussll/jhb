/**
 * Jack High Bowls - Interactive Bowls Finder & Bias Spectrum Widget
 * Real-time client-side faceted filtering for lawn bowls models.
 * Vanilla JavaScript (zero external dependencies).
 */
(function () {
  "use strict";

  function initBowlsFinder() {
    var widgets = document.querySelectorAll('[data-component="bowls-finder"]');
    if (!widgets.length) return;

    widgets.forEach(function (widget) {
      if (widget.dataset.initialized === "true") return;
      widget.dataset.initialized = "true";

      var surfaceSelect = widget.querySelector('[data-filter="surface"]');
      var positionSelect = widget.querySelector('[data-filter="position"]');
      var biasSelect = widget.querySelector('[data-filter="bias"]');
      var smallHandsCheckbox = widget.querySelector(
        '[data-filter="small-hands"]',
      );
      var resetButtons = widget.querySelectorAll('[data-action="reset"]');
      var countEl = widget.querySelector("[data-finder-count]");
      var statusEl = widget.querySelector("[data-finder-status]");
      var chipsEl = widget.querySelector("[data-finder-chips]");
      var noResultsEl = widget.querySelector("[data-finder-no-results]");
      var cards = widget.querySelectorAll(".finder-card");
      var markers = widget.querySelectorAll(".spectrum-marker");
      var totalCount = cards.length;

      // Check URL query parameters for initial filter overrides
      var urlParams = new URLSearchParams(window.location.search);
      var initialSurface =
        urlParams.get("surface") || widget.dataset.initialSurface || "all";
      var initialPosition =
        urlParams.get("position") || widget.dataset.initialPosition || "all";
      var initialBias =
        urlParams.get("bias") || widget.dataset.initialBias || "all";
      var initialSmallHands =
        urlParams.get("small_hands") === "true" ||
        widget.dataset.initialSmallHands === "true";

      if (surfaceSelect && initialSurface !== "all") {
        surfaceSelect.value = initialSurface;
      }
      if (positionSelect && initialPosition !== "all") {
        positionSelect.value = initialPosition;
      }
      if (biasSelect && initialBias !== "all") {
        biasSelect.value = initialBias;
      }
      if (smallHandsCheckbox && initialSmallHands) {
        smallHandsCheckbox.checked = true;
      }

      function isModelMatching(element, filters) {
        var surfaces = element.getAttribute("data-surfaces") || "";
        var positions = element.getAttribute("data-positions") || "";
        var bias = parseFloat(element.getAttribute("data-bias") || "0");
        var smallHands = element.getAttribute("data-small-hands") === "true";

        // 1. Surface filter
        if (filters.surface !== "all") {
          if (filters.surface === "indoor") {
            if (surfaces.indexOf("indoor") === -1) return false;
          } else if (filters.surface === "fast-outdoor") {
            if (
              surfaces.indexOf("fast") === -1 &&
              surfaces.indexOf("synthetic") === -1
            ) {
              return false;
            }
          } else if (filters.surface === "slow-outdoor") {
            var matchesSlow =
              surfaces.indexOf("slow") !== -1 ||
              surfaces.indexOf("heavy") !== -1 ||
              surfaces.indexOf("holding") !== -1 ||
              surfaces.indexOf("outdoor grass") !== -1 ||
              surfaces.indexOf("medium grass") !== -1 ||
              surfaces.indexOf("medium/slow") !== -1;
            if (!matchesSlow) return false;
          } else if (filters.surface === "crown-green") {
            if (surfaces.indexOf("crown") === -1) return false;
          }
        }

        // 2. Position filter
        if (filters.position !== "all") {
          var isAllPositions = positions.indexOf("all positions") !== -1;
          if (!isAllPositions) {
            if (filters.position === "lead") {
              if (positions.indexOf("lead") === -1) return false;
            } else if (filters.position === "second") {
              if (positions.indexOf("second") === -1) return false;
            } else if (filters.position === "third") {
              if (positions.indexOf("third") === -1) return false;
            } else if (filters.position === "skip") {
              if (
                positions.indexOf("skip") === -1 &&
                positions.indexOf("back-end") === -1
              ) {
                return false;
              }
            } else if (filters.position === "singles") {
              if (positions.indexOf("singles") === -1) return false;
            }
          }
        }

        // 3. Bias profile filter
        if (filters.bias !== "all") {
          if (filters.bias === "narrow") {
            if (bias > 3.5) return false;
          } else if (filters.bias === "mid") {
            if (bias <= 3.5 || bias > 6.0) return false;
          } else if (filters.bias === "wide") {
            if (bias <= 6.0) return false;
          }
        }

        // 4. Small hands filter
        if (filters.smallHands && !smallHands) {
          return false;
        }

        return true;
      }

      function updateActiveChips(filters) {
        if (!chipsEl) return;
        chipsEl.innerHTML = "";

        var filterMap = [
          {
            key: "surface",
            active: filters.surface !== "all",
            label:
              surfaceSelect &&
                surfaceSelect.options[surfaceSelect.selectedIndex]
                ? surfaceSelect.options[surfaceSelect.selectedIndex].text
                : filters.surface,
            reset: function () {
              if (surfaceSelect) surfaceSelect.value = "all";
            },
          },
          {
            key: "position",
            active: filters.position !== "all",
            label:
              positionSelect &&
                positionSelect.options[positionSelect.selectedIndex]
                ? positionSelect.options[positionSelect.selectedIndex].text
                : filters.position,
            reset: function () {
              if (positionSelect) positionSelect.value = "all";
            },
          },
          {
            key: "bias",
            active: filters.bias !== "all",
            label:
              biasSelect && biasSelect.options[biasSelect.selectedIndex]
                ? biasSelect.options[biasSelect.selectedIndex].text
                : filters.bias,
            reset: function () {
              if (biasSelect) biasSelect.value = "all";
            },
          },
          {
            key: "smallHands",
            active: filters.smallHands === true,
            label: "Small Hands",
            reset: function () {
              if (smallHandsCheckbox) smallHandsCheckbox.checked = false;
            },
          },
        ];

        filterMap.forEach(function (item) {
          if (!item.active) return;
          var chip = document.createElement("button");
          chip.type = "button";
          chip.className = "finder-chip";
          chip.innerHTML =
            item.label +
            ' <span class="finder-chip-remove" aria-hidden="true">&times;</span>';
          chip.setAttribute("aria-label", "Remove " + item.label + " filter");
          chip.addEventListener("click", function () {
            item.reset();
            applyFilters();
          });
          chipsEl.appendChild(chip);
        });
      }

      function applyFilters() {
        var filters = {
          surface: surfaceSelect ? surfaceSelect.value : "all",
          position: positionSelect ? positionSelect.value : "all",
          bias: biasSelect ? biasSelect.value : "all",
          smallHands: smallHandsCheckbox ? smallHandsCheckbox.checked : false,
        };

        var visibleCount = 0;

        // Filter Model Cards
        cards.forEach(function (card) {
          var matched = isModelMatching(card, filters);
          if (matched) {
            card.classList.remove("is-hidden");
            card.removeAttribute("aria-hidden");
            visibleCount++;
          } else {
            card.classList.add("is-hidden");
            card.setAttribute("aria-hidden", "true");
          }
        });

        // Filter Bias Spectrum Markers
        markers.forEach(function (marker) {
          var matched = isModelMatching(marker, filters);
          if (matched) {
            marker.classList.remove("is-dimmed");
            marker.removeAttribute("aria-hidden");
          } else {
            marker.classList.add("is-dimmed");
            marker.setAttribute("aria-hidden", "true");
          }
        });

        // Update count text
        if (countEl) {
          countEl.textContent = visibleCount;
        }

        // Update accessible status text
        if (statusEl) {
          statusEl.setAttribute(
            "aria-label",
            "Showing " +
            visibleCount +
            " of " +
            totalCount +
            " lawn bowls models matching your filters",
          );
        }

        // Toggle No Results element
        if (noResultsEl) {
          if (visibleCount === 0) {
            noResultsEl.classList.remove("d-none");
          } else {
            noResultsEl.classList.add("d-none");
          }
        }

        // Update active chips
        updateActiveChips(filters);
      }

      // Event listeners for controls
      if (surfaceSelect) {
        surfaceSelect.addEventListener("change", applyFilters);
      }
      if (positionSelect) {
        positionSelect.addEventListener("change", applyFilters);
      }
      if (biasSelect) {
        biasSelect.addEventListener("change", applyFilters);
      }
      if (smallHandsCheckbox) {
        smallHandsCheckbox.addEventListener("change", applyFilters);
      }

      // Reset action
      resetButtons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          if (surfaceSelect) surfaceSelect.value = "all";
          if (positionSelect) positionSelect.value = "all";
          if (biasSelect) biasSelect.value = "all";
          if (smallHandsCheckbox) smallHandsCheckbox.checked = false;
          applyFilters();
          if (surfaceSelect) surfaceSelect.focus();
        });
      });

      // Clicking a spectrum marker smoothly scrolls to that card in the grid below
      markers.forEach(function (marker) {
        marker.addEventListener("click", function (e) {
          e.preventDefault();
          var modelId = marker.getAttribute("data-marker-id");
          if (!modelId) return;

          var targetCard = widget.querySelector("#card-" + modelId);
          if (targetCard) {
            targetCard.scrollIntoView({
              behavior: "smooth",
              block: "center",
            });
            targetCard.classList.add("finder-card--highlighted");
            setTimeout(function () {
              targetCard.classList.remove("finder-card--highlighted");
            }, 1800);
          }
        });
      });

      // Run initial filter pass
      applyFilters();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initBowlsFinder);
  } else {
    initBowlsFinder();
  }
})();
