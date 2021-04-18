$('.multiple-items').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 3,
    arrows:false,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 1000,
    dots:true,
    centerMode:true,
    centerPadding:'10px',    
  });

  $(document).ready(function() {
    $('#subir').click(function(){
      $('html, body').animate({scrollTop:0}, 'slow');
      return false;
    });
  });


  $("a.page-link").each(function(){
    if ($(this).attr("data-page")== window.location.search.replace("?page=","")){
        $ (this).addClass("active")
    }
});

/* fade preloader */
$(window).on("load",function(){
  $(".loader-wrapper").fadeOut("slow");
});
