document.addEventListener('DOMContentLoaded', function () {

    const reviewRanges = document.querySelectorAll('input[type=range]')

    // Set Stars Text when page first loaded
    reviewRanges.forEach(range => {
        const num_stars = range.getAttribute('value')
        const stars_element = range.nextElementSibling
        let span = stars_element.getElementsByTagName('span')

        // Update text to Star/Stars depending on number
        if (num_stars === "1") {
            span[0].innerText = " Star";
        }
        else {
            span[0].innerText = " Stars";
        }
    })

    // Set Stars Text after range changed
    reviewRanges.forEach(range => {
        range.addEventListener('input', event => {
            update_stars_text(event);
        })
    })

    // let i = document.querySelectorAll('input');

    // // Set Stars Text after range changed
    // i.forEach(range => {
    //     range.addEventListener('input', event => {
    //         update_stars_text(event);
    //     })
    // })

    // Set first image as active
    let carousel_items = document.getElementsByClassName('carousel-item');
    carousel_items[0].setAttribute("class", "carousel-item active");

    // Need some code here to grab the rating from Cafe model
    // Code originally from https://webdesign.tutsplus.com/a-simple-javascript-technique-for-filling-star-ratings--cms-29450t
    const starTotal = 5;
    const class_name = "star";
    const rating = 2.5

    const starPercentage = (rating / starTotal) * 100;
    const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
    document.querySelector(`.${class_name} .stars-inner`).style.width = starPercentageRounded;

})

function update_stars_text(event) {
    // Stars text should have value of "Star" if range input is one and "Stars" for all other values
    console.log(event);
    const num_stars = event.target.value
    const stars_element = event.target.nextElementSibling

    let span = stars_element.getElementsByTagName('span')

    // Update text to Star/Stars depending on number
    if (num_stars === "1") {
        span[0].innerText = " Star";
    }
    else {
        span[0].innerText = " Stars";
    }    

  }