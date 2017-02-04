$(document).ready(function () {

    //calendar
    addEventListener('DOMContentLoaded', function () {
        pickmeup.defaults.locales['ua'] = {
            days: ['Неділя', 'Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П' + "'" + 'ятница', 'Субота'],
            daysShort: ['Нд', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
            daysMin: ['Нд', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
            months: ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень'],
            monthsShort: ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер', 'Лип', 'Сер', 'Вер', 'Жов', 'Лис', 'Гру']
        };
        pickmeup('.calendar', {
            flat : true,
            select_day : true,
            select_month : false,
            select_year : false,
            locale : 'ua'

        });

    });

    //Slider-mini
    $('.slider-mini').slick({
        dots: false,
        infinite: true,
        speed: 300,
        prevArrow: "<img class='a-left control-c prev slick-prev shape-left' src='img/Shape-left.png'>",
        nextArrow: "<img class='a-right control-c next slick-next shape-right' src='img/Shape-right.png'>",
        slidesToShow: 3,
        slidesToScroll: 1,
        responsive: [

            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }

        ]
    });
});