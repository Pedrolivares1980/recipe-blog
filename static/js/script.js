$(document).ready(function() {
  // Smooth scrolling for internal links
  $("a[href^='#']").on("click", function(e) {
    e.preventDefault();
    var target = this.hash;
    if ($(target).length) { // Check if the target element exists
      $("html, body").animate({
        scrollTop: $(target).offset().top
      }, 800);
    }
  });

  // Scroll to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 200) {
      $('#scroll-to-top').fadeIn();
    } else {
      $('#scroll-to-top').fadeOut();
    }
  });

  $('#scroll-to-top').click(function() {
    $('html, body').animate({ scrollTop: 0 }, 100);
    return false;
  });

  // Translucent navbar on scroll down
  $(window).scroll(function() {
    if ($(this).scrollTop() > 50) {
      $('.navbar').addClass('navbar-scroll');
    } else {
      $('.navbar').removeClass('navbar-scroll');
    }
  });
});

// Dynamic Copyright Year
document.addEventListener('DOMContentLoaded', function () {
  var year = new Date().getFullYear();
  document.getElementById('copyright-year').textContent = year;
});

