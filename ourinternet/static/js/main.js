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
    Hammer($slides[0]).on("swipeleft", function(e) {
      $slides.data('superslides').animate('next');
    });

    Hammer($slides[0]).on("swiperight", function(e) {
      $slides.data('superslides').animate('prev');
    });
  };

  Slider.initialize = function(){
    $slides.superslides({
        hashchange: true,
        pagination: false
    });
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
    $('#slides').on('animated.slides', highligtMenuHandler);
  };


})();

Video = {};
(function(){

  Video.initialize = function(){
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

  ContactFormHandler.hookupSubmit = function (){
    $(".contact-form").submit(submit_function);
  };

})();

ResponsiveMenu = {};

(function(){
  var menu = $("#top-menu");
  var responsiveMenuToggle = $("#responsive-menu-toggle");
  var responsiveMenuList = $("#responsive-menu ul");

  var copyCollapsedLinks = function(){
    menu.children("a:not(.home)").each(function(){
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
  };

  var hookupToggle = function(){
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
  }

  ResponsiveMenu.initialize = function(){
    copyCollapsedLinks();
    enableHomeLink();
    hookupToggle();
  };

})();

SubPageHandler = {};

(function(){
  var previousMainHash = "";
  var previousSubHash = "";
  var lastLoadedSubPages = {};

  var splitHash = function(hash){
    var slash_position = hash.indexOf("/")
    if (slash_position != -1){
      var subpage = hash.substr(slash_position + 1);
      var mainpage = hash.substr(0, slash_position);

      return [mainpage, subpage]
    } else {
      return [hash, ""]
    }
  }

  var showPressRelease = function(slug){
    $("#" + slug).show();
  }

  var resetAddressBar = function(baseHash, subHash){
    window.location = baseHash + "/" + subHash;
  };

  var load_press_release = function(release){
    SubPageHandler.hideAllPressReleases();
    showPressRelease(release);
    resetAddressBar("#press", release)
  };

  var load_subpage = function(storedHash){
    hashParts = splitHash(storedHash);

    if (hashParts[1] != ""){
        var subpage = hashParts[1];
        var mainpage = hashParts[0];

        if (mainpage == "#press"){
            load_press_release(subpage);
        }
    } else {
        if (lastLoadedSubPages[hashParts[0]] != "" && lastLoadedSubPages[hashParts[0]] != undefined){
            window.location = hashParts[0] + "/" + lastLoadedSubPages[hashParts[0]]
        } else {
            if (hashParts[0] == "#press"){
                $("#press-release-content").html("");
            }

        }
    }
    hashParts = splitHash(window.location.hash)
    lastLoadedSubPages[hashParts[0]] = hashParts[1];
  }

  SubPageHandler.hookupBasics = function(){
    $(window).on('hashchange', function() {
      hashParts = splitHash(window.location.hash);
      if (previousMainHash != hashParts[0]){
        previousMainHash = hashParts[0];
        load_subpage(window.location.hash);
      } else  if (previousSubHash != hashParts[1] && hashParts[1] != ""){
        previousSubHash = hashParts[1];
        load_subpage(window.location.hash);
      }
    });

    $(window).on('load' , function(){
        var storedHash = window.location.hash;
        load_subpage(storedHash);
    });
  };



  SubPageHandler.hookupReleaseListItems = function(){
    $(".press-release-link").click( function(){
       var release = $(this).data("release-id");
       load_press_release(release)
    });
  };

  SubPageHandler.hideAllPressReleases = function(){
    $(".press-release").hide();
  };
})();



$(function(){
  GoogleAnalyticsExtension.hookupSubmit();

  var touch_support = $('html').hasClass("touch");
  if (touch_support){
    Slider.setupTouch();
  }

  Slider.initialize();
  Slider.hookupMenu()

  var is_ie7 = $('html').hasClass("lt-ie8");
  if (!Modernizr.touch & !is_ie7) {
    Video.initialize();
  }

  ResponsiveMenu.initialize();

  TwitterLinkHandler.updateiTwitterLinks();

  ContactFormHandler.hookupSubmit();

  SubPageHandler.hookupBasics();
  SubPageHandler.hookupReleaseListItems();
  SubPageHandler.hideAllPressReleases();
});
