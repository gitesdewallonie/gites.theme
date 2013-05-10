jQuery(document).ready(function($) {

    $('#package-carousel.carousel').carousel({  
      interval: 5000
      , pause: 'hover'
    })  

    $('#splashvideo img').click(function(){
        var videoUrl = $(this).attr('data-video');
        var frame = '<iframe width="100%" height="539" src="' + videoUrl + '?rel=0&autoplay=1" frameborder="0" allowfullscreen></iframe>';
        $(this).replaceWith(frame);
    });

});
