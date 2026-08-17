$(function () {
  $('[data-toggle="tooltip"]').tooltip()

  var $postBody = $('.post-article__body')
  var $drillFeature = $('#drill-pack-feature')
  var $gettingStarted = $('.getting-started')

  if ($postBody.length && $drillFeature.length) {
    var $paragraphs = $postBody.find('h2')

    if ($paragraphs.length >= 5) {
      $drillFeature.insertBefore($paragraphs.eq(4))
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

  var $newsletterModal = $('[data-newsletter-modal]')

  if ($newsletterModal.length) {
    var cookieName = 'jhbNewsletterModalSeen'
    var cookieDurationDays = 60

    var getCookie = function (name) {
      var nameEQ = name + '='
      var ca = document.cookie.split(';')
      for (var i = 0; i < ca.length; i += 1) {
        var c = ca[i]
        while (c.charAt(0) === ' ') {
          c = c.substring(1, c.length)
        }
        if (c.indexOf(nameEQ) === 0) {
          return c.substring(nameEQ.length, c.length)
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
      document.cookie = name + '=' + value + expires + '; path=/'
    }

    if (!getCookie(cookieName)) {
      var $secondHeading = $('.post-article__body').find('h2').eq(1)

      if ($secondHeading.length) {
        var hasTriggered = false
        var $closeButtons = $newsletterModal.find('[data-newsletter-modal-close]')
        var $overlay = $newsletterModal.find('[data-newsletter-modal-overlay]')
        var $focusTarget = $newsletterModal.find('[data-newsletter-modal-heading]')
        var checkScroll

        var escHandler = function (event) {
          if (event.key === 'Escape' || event.key === 'Esc' || event.keyCode === 27) {
            closeModal()
          }
        }

        var closeModal = function () {
          if ($newsletterModal.attr('hidden') !== undefined) {
            return
          }
          $newsletterModal.attr('hidden', 'hidden')
          $('body').removeClass('newsletter-modal-open')
          $(document).off('keydown.newsletterModal', escHandler)
        }

        var openModal = function () {
          if (hasTriggered) {
            return
          }
          hasTriggered = true
          setCookie(cookieName, 'seen', cookieDurationDays)
          $newsletterModal.removeAttr('hidden')
          $('body').addClass('newsletter-modal-open')
          if ($focusTarget.length) {
            $focusTarget.focus()
          }
          $(document).on('keydown.newsletterModal', escHandler)
          $(window).off('scroll.newsletterModal', checkScroll)
        }

        checkScroll = function () {
          if (hasTriggered) {
            return
          }

          var scrollTop = $(window).scrollTop() || 0
          var headingOffset = $secondHeading.offset().top

          if (scrollTop > headingOffset) {
            openModal()
          }
        }

        $(window).on('scroll.newsletterModal', checkScroll)

        $closeButtons.on('click', function (event) {
          event.preventDefault()
          closeModal()
        })

        $overlay.on('click', function () {
          closeModal()
        })

        checkScroll()
      }
    }
  }
})
