jQuery(document).ready(function ($) {
    "use strict";
    fc_StickyHeader();
    fc_ScrollAction();
    fc_MenuMobile();
    fc_ToolTip();
    fc_ToggleClass();
    fc_CardNumber();
    fc_Quantity();
    fc_List();
    fc_DarkMode();
    fc_HoverSRC();
    fc_Counter();
    fc_SwiperSlider_CustomData();
    fc_YoutubeBackground();
    fc_Mansony();
    function fc_ScrollAction() {
        $(window).on('scroll', function () {
            if ($(document).scrollTop() > 1000) {

                $('.js-back-to-top').addClass('active');
            } else {
                $('.js-back-to-top').removeClass('active');
            }
        });

    }

    $('body').imagesLoaded(function() {
        fc_Aos();
    });
    function fc_Mansony() {
        var $grid = $('.js-mansony').masonry();
        $grid.imagesLoaded(function () {
            $grid.masonry({
                itemSelector: '.itemMansony',
                columnWidth: '.itemMansony'
            });
        });
    }
    setInterval(function () {
        fc_countdown();
    }, 1000);

    function fc_Aos() {
        AOS.init({
            easing: 'ease',
            duration: 1000,
            once: true
        });
    }

    function fc_YoutubeBackground() {
        $('[data-vbg]').youtube_background();
    }

    function fc_StickyHeader() {
        const body = $('body');
        const scrollUp = 'scroll-up';
        const scrollDown = 'scroll-down';
        let lastScroll = 0;

        var navbar = $('header');
        const scroll = $(window).scrollTop();
        if (scroll > navbar.outerHeight()) {
            body.addClass(scrollDown).removeClass(scrollUp);
        }

        $(window).on('scroll', () => {
            const currentScroll = $(window).scrollTop();
            if (currentScroll <= 0) {
                body.removeClass(scrollUp);
                return;
            }
            if (currentScroll > lastScroll && !body.hasClass(scrollDown)) {
                body.removeClass(scrollUp).addClass(scrollDown);
            } else if (currentScroll < lastScroll && body.hasClass(scrollDown)) {
                body.removeClass(scrollDown).addClass(scrollUp);
            }
            lastScroll = currentScroll;
        });
    }

    function fc_Counter() {
        $('.js-count').each(function () {
            $(this).prop('Counter', 0).animate({
                Counter: $(this).text()
            }, {
                duration: $(this).data('duration'),
                easing: 'swing',
                step: function (now) {
                    $(this).text(Math.ceil(now));
                }
            });
        });
    }

    function fc_countdown() {
        $('.js-time').each(function () {
            var endTime = new Date($(this).data('time'));
            endTime = (Date.parse(endTime) / 1000);

            var now = new Date();
            now = (Date.parse(now) / 1000);

            var timeLeft = endTime - now;

            var days = Math.floor(timeLeft / 86400);
            var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
            var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600)) / 60);
            var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));

            if (hours < "10") {
                hours = "0" + hours;
            }
            if (minutes < "10") {
                minutes = "0" + minutes;
            }
            if (seconds < "10") {
                seconds = "0" + seconds;
            }

            $(this).find('.days').html(days + "<span class='fs-xs letter-spacing-2 text-uppercase mt-1'>Days</span>");
            $(this).find('.hours').html(hours + "<span class='fs-xs letter-spacing-2 text-uppercase mt-1'>Hrs</span>");
            $(this).find('.minutes').html(minutes + "<span class='fs-xs letter-spacing-2 text-uppercase mt-1'>Mins</span>");
            $(this).find('.seconds').html(seconds + "<span class='fs-xs letter-spacing-2 text-uppercase mt-1'>Secs</span>");
        });
    }

    function fc_HoverSRC() {
        var bigItem = $('.bigitem');
        var smallItem = $('.smallitem');
        smallItem.on('mouseenter', function () {
            bigItem.removeClass('active');
            smallItem.removeClass('active');
            bigItem.eq($(this).index()).addClass('active');
            smallItem.eq($(this).index()).addClass('active');
        });
    }

    function fc_DarkMode() {
        var body = $('body');
        $('.js-settings').on('click', function (even) {
            even.preventDefault();
            $(this).parent().parent().toggleClass('active');

        });
        $('.settings-option').each(function () {

            $(this).on('click', function (e) {
                switch ($(this).data('settings')) {
                    case 'layout':
                        var layout = $(this).data('layout');
                        body.removeClass('boxed').addClass(layout);
                        break;
                    default:
                }
            })
        });

    }

    function fc_SwiperSlider_CustomData() {
        var sliderSelector = '.hero-slider .swiper-container',
            dataDefault = {};

        var eachSlider = document.querySelectorAll(sliderSelector);

        [].forEach.call(eachSlider, function (slider, index, arr) {
            var data = slider.getAttribute('data-slide') || {};
            if (data) {
                var dataOptions = JSON.parse(data);
                var thumbsOptions = dataOptions.thumb;
                var thumbsInit;
                if (thumbsOptions) {

                    var thumbImages = slider.querySelectorAll("img");
                    var slides = '';
                    thumbImages.forEach(function (img) {
                        slides += "\n          <div class='swiper-slide '>\n            <img class='img-fluid' src=".concat(img.src, " alt='img'/>\n          </div>\n        ");
                    });
                    var thumbs = document.createElement('div');
                    thumbs.setAttribute('class', 'swiper js-thumb');
                    thumbs.innerHTML = "<div class='swiper-wrapper'>".concat(slides, "</div>");
                    if (thumbsOptions.parent) {
                        var parent = document.querySelector(thumbsOptions.parent);
                        parent.parentNode.appendChild(thumbs);
                    } else {
                        slider.parentNode.appendChild(thumbs);
                    }
                    thumbsOptions.options = Object.assign(
                        {
                            navigation: {
                                nextEl: thumbs.querySelector(".cs-swiper-button-next"),
                                prevEl: thumbs.querySelector(".cs-swiper-button-prev"),
                            },
                        }, thumbs, thumbsOptions);

                    thumbsInit = new window.Swiper(thumbs, thumbsOptions.options);

                    slider.options = Object.assign(
                        {
                            thumbs: {
                                swiper: thumbsInit
                            },
                        }, dataDefault, dataOptions);

                    var swiper = new Swiper(slider, slider.options);
                } else {
                    slider.options = Object.assign({}, dataDefault, dataOptions);

                    var swiper = new Swiper(slider, slider.options);

                }
            }
        });
    }


    function fc_List() {
        $('.js-search-list-input').on('keyup', function () {
            var value = $(this).val().toLowerCase();
            $('.js-list li > div').filter(function () {
                $(this).toggle($(this).attr('data-label').toLowerCase().indexOf(value) > -1)
            });
        });
    }

    function fc_CardNumber() {
        $('.credit-card').each(function () {
            var card = new Card({
                form: '.credit-card',
                container: '.card-wrapper',

                messages: {
                    validDate: 'expire\ndate',
                    monthYear: 'mm/yy'
                }
            });
        });

    }

    function fc_MenuMobile() {

        $('.navbar-nav-canvas li:has(ul)').append("<i class='bi bi-chevron-right icon-nav-canvas'></i>");
        if ($('.navbar-nav-canvas li.active').length) {
            var this_active = $('.ul-collapse li.active');
            $(this_active).find('.icon-nav-canvas').addClass('active');
            $(this_active).find('ul').slideDown();
        }

        $('.navbar-nav-canvas .icon-nav-canvas').on('click', function (e) {
            $(this).prev('ul').slideToggle(300);
            $(this).parent().toggleClass('active');
            $(this).toggleClass('active');
            e.preventDefault();
        });

    }

    function fc_ToolTip() {
        var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
        var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl)
        })
    }

    function fc_ToggleClass() {
        $('.js-class-toggle').on('click', function (e) {
            e.preventDefault();
            $(this).toggleClass('active');
        });
    }

    function fc_Quantity() {
        $('.js-quantity').each(function () {
            var t = $(this).find('.quantity-field');
            var value = 1
            $(t).val(value);
            $(this).find('.button-plus').on('click', function () {
                value = parseInt(value + 1);
                $(t).val(value);
            });
            $(this).find('.button-minus').on('click', function () {
                if (value > 1) {
                    value = parseInt(value - 1);
                    $(t).val(value);
                } else {
                    value = 1;
                    $(t).val(value);
                }
            });
        });
    }

});
