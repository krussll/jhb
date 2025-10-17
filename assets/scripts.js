$(function () {
  $('[data-toggle="tooltip"]').tooltip()

  var $postBody = $('.post-article__body')
  var $drillFeature = $('#drill-pack-feature')

  if ($postBody.length && $drillFeature.length) {
    var $paragraphs = $postBody.find('p')

    if ($paragraphs.length >= 4) {
      $drillFeature.insertAfter($paragraphs.eq(3))
    } else {
      $postBody.append($drillFeature)
    }
  }
})
