GoogleAnalyticsExtension = {};

(function(){
  var customPageViewHandler = function(){
      ga('send', 'pageview', window.location.hash);
  };

  GoogleAnalyticsExtension.hookupSubmit = function(){
    $(window).on('hashchange', customPageViewHandler);
  };

})();

Slider = {};

(function(){
  var $slides = $('#slides');

  Slider.setupTouch = function(){
    if ($slides.length === 0){
      return;
    }

    Hammer($slides[0]).on("swipeleft", function(e) {
      $slides.data('superslides').animate('next');
    });

    Hammer($slides[0]).on("swiperight", function(e) {
      $slides.data('superslides').animate('prev');
    });
  };

  var hideScrollBarsWhileSliding = function(){
    $('#slides').on('animating.slides', function(){
      $('.slides-container li').addClass('no-scroll');
    });
    $('#slides').on('animated.slides', function(){
      $('.slides-container li').removeClass('no-scroll');
    });
  };

  Slider.initialize = function(){
    if ($slides.length === 0){
      return;
    }
    $slides.superslides({
      hashchange: true,
      pagination: false
    });

    hideScrollBarsWhileSliding();

  };

  var highligtMenuHandler = function(){
    var current_index = $(this).superslides('current');
    $('.custom-slides-pagination a').removeClass('current');
    $('.custom-slides-pagination a').eq(current_index).addClass('current');
    if (current_index == 0){
      $('.compressed.custom-slides-pagination a').eq(current_index).addClass('current');
    }else {
      $('.compressed.custom-slides-pagination a').eq(current_index + 1).addClass('current');
    }
  };

  Slider.hookupMenu = function(){
    if ($slides.length === 0){
      return;
    }
    $slides.on('animated.slides', highligtMenuHandler);
  };

})();

Video = {};
(function(){

  Video.initialize = function(){
    if (typeof $.BigVideo === "undefined"){
      return;
    }
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
      if (hash == "#home" || hash == ""){
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

    $(window).on('hashchange', function() {
      playPauseVideo(window.location.hash);
    });
  };
})();

TwitterLinkHandler = {};

(function(){

  TwitterLinkHandler.updateiTwitterLinks = function(){
    var agent   = navigator.userAgent;

    if ( agent.match(/(iPhone|iPod|iPad)/) ) {
        twitter_links = $(".twitter-link a");
        twitter_links.each(function(){
            link_value = $(this).data("twitter-href");
            $(this).attr("href", link_value);
        });
    }
  }

})();


ContactFormHandler = {};

(function(){
  var submit_function = function(e){
    var postData = $(this).serializeArray();
    var formURL = $(this).attr("action");
    $(this).find("input[type=submit]").attr('disabled', true);

    $.ajax(
    {
      url : formURL,
      type: "POST",
      data : postData,
      success:function(data, textStatus, jqXHR)
      {
          $(".contact-page-contents").html(data);

          $(".contact-form").submit(submit_function);

          if ($(".errorlist").length > 0) {
              $(".errorlist").addClass("fa-ul");
              $(".errorlist li").prepend("<i class='fa-li fa fa-times-circle'></i>");
          }

          $(this).find("input[type=submit]").removeAttr('disabled');

      },
      error: function(jqXHR, textStatus, errorThrown)
      {
        $(this).find("input[type=submit]").removeAttr('disabled');
      }
    });
    e.preventDefault(); //STOP default action
  };

  ContactFormHandler.hookupSubmit = function (){
    $(".contact-form").submit(submit_function);
  };

})();

ResponsiveMenu = {};

(function(){
  var menu = $("#top-menu");
  var responsiveMenuToggle = $("#responsive-menu-toggle");
  var responsiveMenuList = $("#responsive-menu ul");

  var onToggle = function(){
      toggleMenu(responsiveMenuList);
  };

  var toggleMenu = function (responsiveMenuList){
    if (responsiveMenuList.is(":hidden")){
      $("ul.slides-container").fadeOut(200);
      $("#slides").bind("click", onToggle)
    } else{
      $("ul.slides-container").fadeIn(200);
      $("#slides").unbind("click", onToggle);
    }
    responsiveMenuList.slideToggle(200, function(){

    });
  };

  var copyCollapsedLinks = function(){
    menu.children("a:not(.home):not(.icon)").each(function(){
        var li = $('<li/>')
            .appendTo(responsiveMenuList);
        var link = $(this).clone();
        link.appendTo(li);
        link.on('click', function(e){
            toggleMenu(responsiveMenuList);
        });
    });
  };

  var enableHomeLink = function(){
    $("#responsive-menu a.home").each(function(){
        $(this).on('click', function(e){
            if (!responsiveMenuList.is(":hidden")){
                toggleMenu(responsiveMenuList);
            }
        });
    });

    $("#responsive-menu a.icon").each(function(){
        $(this).on('click', function(e){
            if (!responsiveMenuList.is(":hidden")){
                toggleMenu(responsiveMenuList);
            }
        });
    });
  };

  var hookupToggle = function(){
    responsiveMenuToggle.on('click', function(e){
        e.preventDefault();
        toggleMenu(responsiveMenuList);
    });
  };

  ResponsiveMenu.initialize = function(){
    copyCollapsedLinks();
    enableHomeLink();
    hookupToggle();
  };

})();

SubPageHandler = {};

(function(){

  var splitHash = function(hash){
    var slash_position = hash.indexOf("/")
    if (slash_position != -1){
      var subpage = hash.substr(slash_position + 1);
      var mainpage = hash.substr(0, slash_position);

      return [mainpage, subpage]
    } else {
      return [hash, ""]
    }
  };

  var load_subpage = function(mainPage, subPage){
    if (subPage != ""){
      if (mainPage == "#press"){
        window.location.replace("/press/" + subPage);
      } else if (mainPage == "#event"){
        window.location.replace("/event/" + subPage);
      } else if (mainPage == "#publications"){
        window.location.replace("/publication/" + subPage);
      } else if (mainPage == "#videos"){
        window.location.replace("/video/" + subPage);
      }
    } else {
      if (mainPage == "#about"){
        document.title = "About - OurInternet";
      } else if (mainPage == "#partners"){
        document.title = "Partners & Sponsors - OurInternet";
      } else if (mainPage == "#commission"){
        document.title = "Commission - OurInternet";
      } else if (mainPage == "#research_advisers"){
        document.title = "Research Advisers - OurInternet";
      } else if (mainPage == "#press"){
        document.title = "Press - OurInternet";
      } else if (mainPage == "#publications"){
        document.title = "Publications - OurInternet";
      } else if (mainPage == "#event"){
        document.title = "Events - OurInternet";
      } else if (mainPage == "#videos"){
        document.title = "Videos - OurInternet";
      } else if (mainPage == "#contact"){
        document.title = "Contact - OurInternet";
      } else if (mainPage == "#faq"){
        document.title = "FAQ - OurInternet";
      }

    }
  };

  var pageLoadHandler = function() {
      var hashParts = splitHash(window.location.hash);

      var mainPage = hashParts[0];
      var subPage = hashParts[1];
      load_subpage(mainPage, subPage);
  };

  SubPageHandler.hookupBasics = function(){
    $(window).on('hashchange', pageLoadHandler);
    $(window).on('load' , pageLoadHandler);
  };


})();



$(function(){
  GoogleAnalyticsExtension.hookupSubmit();

  var touch_support = $('html').hasClass("touch");
  if (touch_support) {
    Slider.setupTouch();
  }

  Slider.initialize();
  Slider.hookupMenu();



  var is_ie7 = $('html').hasClass("lt-ie8");
  if (!Modernizr.touch && !is_ie7) {
    Video.initialize();
  }

  ResponsiveMenu.initialize();

  TwitterLinkHandler.updateiTwitterLinks();

  ContactFormHandler.hookupSubmit();

  SubPageHandler.hookupBasics();
});
