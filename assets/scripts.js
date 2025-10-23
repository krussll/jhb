$(function () {
  $('[data-toggle="tooltip"]').tooltip()

  var $postBody = $('.post-article__body')
  var $drillFeature = $('#drill-pack-feature')
  var $gettingStarted = $('.getting-started')

  if ($postBody.length && $drillFeature.length) {
    var $paragraphs = $postBody.find('p')

    if ($paragraphs.length >= 4) {
      $drillFeature.insertAfter($paragraphs.eq(3))
    } else {
      $postBody.append($drillFeature)
    }
  }

  if ($gettingStarted.length) {
    $gettingStarted.on('click', 'a[href^="#"]', function (event) {
      var targetSelector = this.getAttribute('href')

      if (!targetSelector || targetSelector === '#') {
        return
      }

      var $target = $(targetSelector)

      if (!$target.length) {
        return
      }

      event.preventDefault()

      $('html, body').animate(
        {
          scrollTop: $target.offset().top,
        },
        500,
        'swing',
        function () {
          $target.attr('tabindex', '-1').focus()
          $target.one('blur', function () {
            $(this).removeAttr('tabindex')
          })
        }
      )
    })
  }

  var modalElement = document.getElementById('post-newsletter-modal')
  var $postArticleBody = $('.post-article__body')

  if (modalElement && $postArticleBody.length) {
    var cookieName = modalElement.getAttribute('data-cookie-name') || 'jhb_post_modal_seen'

    var getCookie = function (name) {
      var cookieString = document.cookie || ''
      var cookies = cookieString.split('; ')

      for (var i = 0; i < cookies.length; i++) {
        var parts = cookies[i].split('=')
        var key = parts.shift()
        var value = parts.join('=')

        if (key === name) {
          return decodeURIComponent(value)
        }
      }

      return null
    }

    var setCookie = function (name, value, days) {
      var expires = ''

      if (days) {
        var date = new Date()
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000)
        expires = '; expires=' + date.toUTCString()
      }

      document.cookie = name + '=' + encodeURIComponent(value) + expires + '; path=/'
    }

    if (!getCookie(cookieName)) {
      var $headings = $postArticleBody.find('h2')
      var $secondHeading = $headings.eq(1)

      if ($secondHeading.length) {
        var hasTriggeredModal = false
        var previousActiveElement = null
        var dialogElement = modalElement.querySelector('.post-newsletter-modal__dialog')

        var getFocusableElements = function () {
          return modalElement.querySelectorAll(
            'a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])'
          )
        }

        var handleKeydown = function (event) {
          if (event.key === 'Escape' || event.key === 'Esc') {
            event.preventDefault()
            closeModal()
            return
          }

          if (event.key === 'Tab') {
            var focusable = getFocusableElements()

            if (!focusable.length) {
              return
            }

            var first = focusable[0]
            var last = focusable[focusable.length - 1]

            if (event.shiftKey) {
              if (document.activeElement === first) {
                event.preventDefault()
                last.focus()
              }
            } else if (document.activeElement === last) {
              event.preventDefault()
              first.focus()
            }
          }
        }

        var closeModal = function () {
          if (!modalElement.classList.contains('is-active')) {
            return
          }

          modalElement.classList.remove('is-active')
          modalElement.setAttribute('aria-hidden', 'true')
          document.body.classList.remove('newsletter-modal-open')

          var finalizeClose = function () {
            modalElement.hidden = true
            modalElement.removeEventListener('transitionend', finalizeClose)
          }

          modalElement.addEventListener('transitionend', finalizeClose)
          setTimeout(finalizeClose, 300)

          document.removeEventListener('keydown', handleKeydown)

          if (previousActiveElement && typeof previousActiveElement.focus === 'function') {
            previousActiveElement.focus()
          }
        }

        var openModal = function () {
          if (hasTriggeredModal) {
            return
          }

          hasTriggeredModal = true
          $(window).off('scroll.newsletterModal', onScroll)

          previousActiveElement = document.activeElement
          modalElement.hidden = false
          modalElement.classList.add('is-active')
          modalElement.setAttribute('aria-hidden', 'false')
          document.body.classList.add('newsletter-modal-open')
          setCookie(cookieName, 'seen', 365)

          var focusable = getFocusableElements()

          if (focusable.length) {
            focusable[0].focus()
          } else if (dialogElement) {
            dialogElement.focus()
          }

          document.addEventListener('keydown', handleKeydown)
        }

        Array.prototype.forEach.call(
          modalElement.querySelectorAll('[data-modal-dismiss]'),
          function (dismissButton) {
            dismissButton.addEventListener('click', function (event) {
              event.preventDefault()
              closeModal()
            })
          }
        )

        var onScroll = function () {
          if (hasTriggeredModal) {
            return
          }

          var headingTop = $secondHeading.offset().top
          var scrollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop

          if (scrollPosition + 100 >= headingTop) {
            openModal()
          }
        }

        $(window).on('scroll.newsletterModal', onScroll)
        onScroll()
      }
    }
  }
})
