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
})
