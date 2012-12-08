;(function ($, window, undefined) {

  /* Javascript masterminded by Kevin Xu <kevin@imkevinxu.com> */
  $('#username_form').submit(function() {
    var input = $('input#username');
    if (input.val()) {
      return true;
    } else {
      input.addClass("error animated shake");
      return false;
    }
  });

  $('#minutes_form').submit(function() {
    var input = $('input#minutes');
    if (isNumber(input.val())) {
      return true;
    } else {
      input.addClass("error animated shake");
      return false;
    }
  });

  function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
  }




  /* ZURB Foundation Javascript Initialization */
  var $doc = $(document);
  var Modernizr = window.Modernizr;

  $.fn.foundationAccordion        ? $doc.foundationAccordion() : null;
  $.fn.foundationAlerts           ? $doc.foundationAlerts() : null;
  $.fn.foundationButtons          ? $doc.foundationButtons() : null;
  $.fn.foundationCustomForms      ? $doc.foundationCustomForms() : null;
  $.fn.foundationMediaQueryViewer ? $doc.foundationMediaQueryViewer() : null;
  $.fn.foundationNavigation       ? $doc.foundationNavigation() : null;
  $.fn.foundationTabs             ? $doc.foundationTabs() : null;
  $.fn.foundationTooltips         ? $doc.foundationTooltips() : null;
  $.fn.foundationTopBar           ? $doc.foundationTopBar() : null;

  $("#featured").orbit();
  $('input, textarea').placeholder();

  // UNCOMMENT THE LINE YOU WANT BELOW IF YOU WANT IE8 SUPPORT AND ARE USING .block-grids
  // $('.block-grid.two-up>li:nth-child(2n+1)').css({clear: 'both'});
  // $('.block-grid.three-up>li:nth-child(3n+1)').css({clear: 'both'});
  // $('.block-grid.four-up>li:nth-child(4n+1)').css({clear: 'both'});
  // $('.block-grid.five-up>li:nth-child(5n+1)').css({clear: 'both'});

  // Hide address bar on mobile devices
  if (Modernizr.touch) {
    $(window).load(function () {
      setTimeout(function () {
        window.scrollTo(0, 1);
      }, 0);
    });
  }

})(jQuery, this);
