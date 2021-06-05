var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween:0,
    centeredSlides: true,
    grabCursor: true,
    loop: true,
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        1199: {
            slidesPerView: 4,
            spaceBetween: 10,
        },
        991: {
            slidesPerView: 3.3,
            spaceBetween: 5,
        },
        767: {
            slidesPerView: 2.5,
            spaceBetween: 4,
        },
        575: {
            slidesPerView: 2,
            spaceBetween:2,
        },
        485: {
            slidesPerView: 2,
            spaceBetween:2,
        }
    }
});