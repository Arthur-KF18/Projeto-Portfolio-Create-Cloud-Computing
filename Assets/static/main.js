window.scroll({
    top: 0,
    behavior: 'smooth',
})

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
      breakpoints: {
        1192: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
      }
    }
  });