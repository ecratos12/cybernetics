$(document).ready(function () {

    var md = new MobileDetect(window.navigator.userAgent);

    if (!md.mobile()) {

        $('#carousel').carousel({
            interval: 3000,
            pause: "false"
        });

        $('.stop-carousel').on('click', function () {
            $('#carousel').carousel('pause');
        });

        // //News card height change
        // $(window).load(function () {
        //     var news_text_max_height = Math.max.apply(null, $("div.news-block h3").map(function () {
        //         return $(this).height();
        //     }).get());
        //
        //     $('.news-block h3').css('height', news_text_max_height);
        // });

        // Fade animation
        $('.fade-bottom').fadeThis({
            speed: 1000
        });

        //Animated slide bar left
        var take_width = $('.main-content-block').width();
        var left_block = $('#left-navbar');

        $('#close-left-navbar').on('click', function () {

            $('.open-btn-block').fadeIn(2000);

            left_block.animate({
                left: "-=+285px"
            }, 1200);

            $('.main-content-block').animate({
                "margin-left": "-=+285px",
                width: take_width + 285
            }, 3000);

        });

        $('#open-left-navbar').on('click', function () {

            left_block.animate({
                left: "-=-285px"
            }, 1200);

            $('.main-content-block').animate({
                "margin-left": "-=-285px",
                width: take_width
            }, 3000);

            $('.open-btn-block').fadeOut(2000);
        });

        //Administration card
        $(window).load(function () {
            //Card
            var admin_card_max_height = Math.max.apply(null, $("div.card").map(function () {
                return $(this).height();
            }).get());

            $('.card').css('height', admin_card_max_height);

            //Width content block

            var height = $('.main-content-block').height();
            $('#menu').css('min-height', height);
        });

    }

    if (md.tablet()) {

        $('#carousel').carousel({
            interval: 3000,
            pause: "false"
        });

        $('.stop-carousel').on('click', function () {
            $('#carousel').carousel('pause');
        });

        // //News card height change
        // $(window).load(function () {
        //     var news_text_max_height = Math.max.apply(null, $("div.news-block h3").map(function () {
        //         return $(this).height();
        //     }).get());
        //
        //     $('.news-block h3').css('height', news_text_max_height);
        // });

        // Fade animation
        $('.fade-bottom').fadeThis({
            speed: 1000
        });

        //Administration card
        $(window).load(function () {
            //Card
            var admin_card_max_height = Math.max.apply(null, $("div.card").map(function () {
                return $(this).height();
            }).get());

            $('.card').css('height', admin_card_max_height);

            //Width content block
            var height = $('.main-content-block').height();
            $('#menu').css('min-height', height);
        });
    }

});
