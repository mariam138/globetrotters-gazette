// Initialise carousel
// Code adapted from: https://getbootstrap.com/docs/5.3/components/carousel/#methods
const indexCarousel = document.querySelector('#indexCarousel');

const carousel = new bootstrap.Carousel(indexCarousel, {
    interval: 3000,
    ride: true,
});