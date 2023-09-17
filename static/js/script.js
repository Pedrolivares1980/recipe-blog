$(document).ready(function() {
  // Smooth scrolling for internal links
  $("a[href^='#']").on("click", function(e) {
    e.preventDefault();
    var target = this.hash;
    $("html, body").animate({
      scrollTop: $(target).offset().top
    }, 800);
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

  // Smooth scrolling when scrolling with mouse
  $(window).on("wheel", function(event) {
    const isScrollingDown = event.originalEvent.deltaY > 0;
    const scrollAmount = isScrollingDown ? 800 : -800;
    
    $("html, body").stop().animate({
      scrollTop: $(window).scrollTop() + scrollAmount
    }, 600);

    event.preventDefault();
  });
});
