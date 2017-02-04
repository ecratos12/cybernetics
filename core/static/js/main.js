$(document).ready(function () {

    //Navbar animation
    var options = {
        offset: 200
    };

    new Headhesive('.nav-cybernetics', options);

    // Search button
    $('#search').on('click', function () {
        var btn_search = $('.btn-search');
        var input_search = $('.input-search');

        if (btn_search.hasClass('active-btn') && input_search.hasClass('active-input')) {

            btn_search.removeClass('active-btn');
            input_search.removeClass('active-input');

            return true;
        }

        btn_search.addClass('active-btn');
        input_search.addClass('active-input');
    });

    //Search mobile btn

    var search_mobile = $('#search-mobile');

    search_mobile.on('click', function () {

        var btn_search = $('.btn-search');
        var input_search = $('.input-search');

        if (btn_search.hasClass('active-btn') && input_search.hasClass('active-input')) {

            btn_search.removeClass('active-btn');
            input_search.removeClass('active-input');
            $('#search-mobile').css('left', '-3px');

            return true;
        }

        btn_search.addClass('active-btn');
        input_search.addClass('active-input');
        search_mobile.css('left', '-225px');
    });


    //Accordion
    var accordionsMenu = $('.cd-accordion-menu');

    if (accordionsMenu.length > 0) {

        accordionsMenu.each(function () {
            var accordion = $(this);
            //detect change in the input[type="checkbox"] value
            accordion.on('change', 'input[type="checkbox"]', function () {
                var checkbox = $(this);
                ( checkbox.prop('checked') ) ? checkbox.siblings('ul').attr('style', 'display:none;').slideDown(300) : checkbox.siblings('ul').attr('style', 'display:block;').slideUp(300);
            });
        });
    }

    //open and close left navbar
    var left_block = $('#left-navbar');

    $('#close-left-navbar').on('click', function () {

        $('.open-btn-block').fadeIn();

        left_block.animate({
            left: "-=+300px"
        });


    });

    $('#open-left-navbar').on('click', function () {

        left_block.animate({
            left: "-=-300px"
        });

        $('.open-btn-block').fadeOut(1000);
    });

    //Activate logo
    setInterval(activeLogo, 5000);

    var logo_header = $('.logo-header');
    var logo_image  = $('.logo-img');

    function activeLogo() {

        if(logo_header.hasClass('active-logo')) {

            logo_header.removeClass('active-logo');
            logo_header.fadeOut();
            setTimeout(activeImageLogo, 500);
        }
        else  {

            logo_image.fadeOut();
            logo_image.removeClass('active-logo');
            setTimeout(activeHeaderLogo, 500);
        }
    }

    function activeHeaderLogo() {
        logo_header.addClass('active-logo');
        logo_header.fadeIn();
    }
    function activeImageLogo() {
        logo_image.addClass('active-logo');
        logo_image.fadeIn();
    }

    //schedule

    $('#open-schedule li').on('click', function () {
        $('.schedule-table').html('');
        $.get( "/get_schedule", { g: $(this).text()} )
        .done(function( data ) {

            for (variable in data) {
                var block = $('.schedule-table');
                var res = "<div class='weekday'><div class='name-weekday'><p>" + variable + "</p></div>";
                var para_list = data[variable];
                jQuery.each(para_list, function() {
                    res = res + "<div class='para'><p>" + this[0] + '. ' + this[1] + '</p><p>' + this[2] + '</p><p>' + this[3] + '</p></div>';
                });
                res = res + '</div>';
                block.append(res);
            }
            
        });
        $('.schedule-table').removeClass('hidden');
        $('.weekday-text').removeClass('hidden');
    });
});

$(document).ready(function () {
    $(".btn-select").each(function (e) {
        var value = $(this).find("ul li.selected").html();
        if (value != undefined) {
            $(this).find(".btn-select-input").val(value);
            $(this).find(".btn-select-value").html(value);
        }
    });
});

$(document).on('click', '.btn-select', function (e) {
    e.preventDefault();
    var ul = $(this).find("ul");
    if ($(this).hasClass("active")) {
        if (ul.find("li").is(e.target)) {
            var target = $(e.target);
            target.addClass("selected").siblings().removeClass("selected");
            var value = target.html();
            $(this).find(".btn-select-input").val(value);
            $(this).find(".btn-select-value").html(value);
        }
        ul.hide();
        $(this).removeClass("active");
    }
    else {
        $('.btn-select').not(this).each(function () {
            $(this).removeClass("active").find("ul").hide();
        });
        ul.slideDown(300);
        $(this).addClass("active");
    }
});

$(document).on('click', function (e) {
    var target = $(e.target).closest(".btn-select");
    if (!target.length) {
        $(".btn-select").removeClass("active").find("ul").hide();
    }
});


