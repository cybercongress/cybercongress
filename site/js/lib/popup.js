var $ = require('jquery')
require('magnific-popup')

module.exports = function () {
  $(document).ready(function () {
    $('.popup-youtube').magnificPopup({
      disableOn: 700,
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false
    })
  })
}
