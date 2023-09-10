document.addEventListener('DOMContentLoaded', function () {

    const reviewRanges = document.querySelectorAll('input[type=range]')

    // Set Stars Text when page first loaded
    reviewRanges.forEach(range => {
        const num_stars = range.getAttribute('value')
        const stars_element = range.nextElementSibling

        update_stars_text(num_stars, stars_element)
    })

    // Set Stars Text after range changed
    reviewRanges.forEach(range => {
        range.addEventListener('input', event => {
            call_stars_text_update(event);
        })
    })

    // Set first image as active in Carousel
    let carousel_items = document.getElementsByClassName('carousel-item');
    carousel_items[0].setAttribute("class", "carousel-item active");

    get_rating();

    // Add event listener to Save Button in Modal
    const saveButton = document.querySelector('.save-review');
    saveButton.addEventListener('click', event => {
        save_review(event);
    })
})

function get_rating() {
    // Get cafe rating from the Cafe model and then update the rating in Stars
    const cafe_id = document.getElementById(`cafeId`).value;
    
    fetch(`/rating/${cafe_id}`)
    .then(response => response.json())
    .then(data => {
        draw_stars(data['rating'])
    })
    .catch(error => {
        console.log('Error:', error);
    });    
}

function draw_stars(rating) {
    // Draw the stars as the rating out of 5
    // Code originally from https://webdesign.tutsplus.com/a-simple-javascript-technique-for-filling-star-ratings--cms-29450t
    const starTotal = 5;
    const class_name = "star";

    const starPercentage = (rating / starTotal) * 100;
    const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
    document.querySelector(`.${class_name} .stars-inner`).style.width = starPercentageRounded;
}

function update_stars_text(num_stars, stars_element) {
    // Stars text should have value of "Star" if range input is 1 and "Stars" for all other values
    let span = stars_element.getElementsByTagName('span');

    if (num_stars === "1") {
        span[0].innerText = " Star ";
    }
    else {
        span[0].innerText = " Stars";
    }    

  }

  function call_stars_text_update(event) {
    // Get number of stars and the element to update after range value changed
    const num_stars = event.target.value;
    const stars_element = event.target.nextElementSibling;

    update_stars_text(num_stars, stars_element);
  }

  function save_review(event) {
    // Save a review
    event.preventDefault();
    const csrftoken = Cookies.get('csrftoken');

    const cafe_id = document.getElementById('cafeId').value;
    let quality = parseInt(document.getElementById('qualityOutputId').value);
    let latte_art = parseInt(document.getElementById('artOutputId').value);
    let barrista_friendliness = parseInt(document.getElementById('barristaOutputId').value);
    let price = parseInt(document.getElementById('priceOutputId').value);
    let opening_hours = parseInt(document.getElementById('openOutputId').value);

    const coffee_description = document.getElementById('coffeeDescription').value

    console.log(cafe_id);

    fetch(`/review/${cafe_id}`, {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            quality: quality,
            latte_art: latte_art,
            barrista_friendliness: barrista_friendliness,
            price: price,
            opening_hours: opening_hours,
            coffee_description: coffee_description
        })
    })
        .then(response => response.json())
        .then(data => {
            reset_after_save(data);
        })
        .catch(error => {
            console.log('Error:', error);
        });
  }

  function reset_after_save(data) {
    // Refresh the star rating and reset the review criteria and description
    get_rating()
    reset_review()
  }

  function reset_review() {
    const outputCriteria = document.querySelectorAll('output');

    // Reset criteria slider component to default of 4
    const reviewRanges = document.querySelectorAll('input[type=range]');
    reviewRanges.forEach(range => {
        range.value = "4";
    })    

    // Reset criteria output component to default of 4
    outputCriteria.forEach(output => {
        output.innerText = "4";
    })

    // Reset description text to empty
    const coffeeDescription = document.getElementById('coffeeDescription');
    coffeeDescription.value = '';
  }