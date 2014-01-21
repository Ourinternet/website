

$(function() {

      var $slides = $('#slides');

      var touch_support = $('html').hasClass("touch");
      if (touch_support){
          Hammer($slides[0]).on("swipeleft", function(e) {
            $slides.data('superslides').animate('next');
          });

          Hammer($slides[0]).on("swiperight", function(e) {
            $slides.data('superslides').animate('prev');
          });
      }


      $slides.superslides({
        hashchange: true,
        pagination: false
      });

      $('#slides').on('animated.slides', function() {
          var current_index = $(this).superslides('current');
          $('.custom-slides-pagination a').removeClass('current');
          $('.custom-slides-pagination a').eq(current_index).addClass('current');
          if (current_index == 0){
            $('.compressed.custom-slides-pagination a').eq(current_index).addClass('current');
          }else {
            $('.compressed.custom-slides-pagination a').eq(current_index + 1).addClass('current');
          }

        });

    });

$(function(){

    var is_ie7 = $('html').hasClass("lt-ie8");
    if (!Modernizr.touch & !is_ie7) {
        var BV;
        BV = new $.BigVideo();
        BV.init();

        BV.getPlayer().on("error", function(){
                $("#background").show();
                $("#big-video-wrap").hide();
        });

        BV.getPlayer().on("playing", function(){
            $("#background").hide();
            $("#pause-video").show();
            $("#big-video-wrap").addClass("big-video-wrap-faded");
            $("#big-video-wrap").show();
        });


        BV.show(videoBaseUrl + "/video_" + videoNumber + ".m4v", {

            ambient:true,
            useFlashForFirefox:false,
            altSource: videoBaseUrl + "/video_" + videoNumber + ".webm"
        });
        $("#pause-video").bind("click", function(){
        BV.getPlayer().pause();
        $(this).hide();
        $("#play-video").show();
        });
        $("#play-video").bind("click", function(){
        BV.getPlayer().play();
        $(this).hide();
        $("#pause-video").show();
        });

        function playPauseVideo(hash){
            if (hash == "#home"){
                BV.getPlayer().play();
                $("#play-video").hide();
                $("#pause-video").show();
            } else {
                BV.getPlayer().pause();
                $("#pause-video").hide();
                $("#play-video").show();
            }
        }

        playPauseVideo(window.location.hash);



    }




});


$(function(){
    var menu = $("#top-menu");
    var responsiveMenuToggle = $("#responsive-menu-toggle");
    var responsiveMenuList = $("#responsive-menu ul");

    menu.children("a:not(.home)").each(function(){
        var li = $('<li/>')
            .appendTo(responsiveMenuList);
        var link = $(this).clone();
        link.appendTo(li);
        link.on('click', function(e){
            toggleMenu(responsiveMenuList);
        });
    });
    $("#responsive-menu a.home").each(function(){
        $(this).on('click', function(e){
            if (!responsiveMenuList.is(":hidden")){
                toggleMenu(responsiveMenuList);
            }
        });
    });


    responsiveMenuToggle.on('click', function(e){
        e.preventDefault();
        toggleMenu(responsiveMenuList);

    });

    var onToggle = function(){
        toggleMenu(responsiveMenuList);
    };

    function toggleMenu(responsiveMenuList){

        if (responsiveMenuList.is(":hidden")){
                $("ul.slides-container").fadeOut(200);
                $("#slides").bind("click", onToggle)
            } else{
                $("ul.slides-container").fadeIn(200);
                $("#slides").unbind("click", onToggle);
            }
        responsiveMenuList.slideToggle(200, function(){

        });
    }

});

$(function(){
    var agent   = navigator.userAgent;

    if ( agent.match(/(iPhone|iPod|iPad)/) ) {
        twitter_links = $(".twitter-link a");
        twitter_links.each(function(){
            link_value = $(this).data("twitter-href");
            $(this).attr("href", link_value);
        });
    }
});

$(function(){
   if ("onhashchange" in window) { // event supported?
            window.onhashchange = function () {
                playPauseVideo(window.location.hash);
                ga('send', 'pageview', window.location.hash);
            }
        } else { // event not supported:
            var storedHash = window.location.hash;
            window.setInterval(function () {
                if (window.location.hash != storedHash) {
                    storedHash = window.location.hash;
                    playPauseVideo(storedHash);
                    ga('send', 'pageview', storedHash);
                }
            }, 100);
        }
});

$(function(){
//    localShowCaptcha("recap");

    var submit_function = function(e){
        var form_parent = $(this).parent();
        var postData = $(this).serializeArray();
        var formURL = $(this).attr("action");

        $.ajax(
        {
            url : formURL,
            type: "POST",
            data : postData,
            success:function(data, textStatus, jqXHR)
            {
                form_parent.html(data);

                $(".contact-form").submit(submit_function);

                $(".messages .success").prepend("<i class='fa fa-check'></i>");

                errors = $(".messages .error");

                if (errors.length > 0){
                    errors.prepend("<i class='fa fa-times-circle'></i>");
                }

                if ($(".errorlist").length > 0) {
                    $(".errorlist").addClass("fa-ul");
                    $(".errorlist li").prepend("<i class='fa-li fa fa-times-circle'></i>");
                }

//                localShowCaptcha("recap");

            },
            error: function(jqXHR, textStatus, errorThrown)
            {
                //if fails
//                localShowCaptcha("recap");
            }
        });
        e.preventDefault(); //STOP default action
    }

    $(".contact-form").submit(submit_function);
});