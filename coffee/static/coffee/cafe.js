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

    // Add event listener to Edit Button in Modal
    const editButton = document.querySelector('.save-edit');
    editButton.addEventListener('click', event => {
        save_edit(event);
    })    
})

function get_rating() {
    // Get cafe rating from the Cafe model and then update the rating in Stars
    const cafe_id = document.getElementById(`cafeId`).value;
    
    fetch(`/rating/${cafe_id}`)
    .then(response => response.json())
    .then(data => {
        draw_stars(data['rating'])
        update_rating_tooltip(data['rating'])
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

function update_rating_tooltip(rating) {
    // Update the numeric rating displayed when hovering over stars after the rating changes
    const numeric_rating = document.getElementById(`numericRatingTooltip`);
    numeric_rating.setAttribute("data-bs-original-title", rating);
    console.log(numeric_rating);
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
            display_haiku();
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

  function display_haiku() {
    // Redisplay the haiku
    const cafe_id = document.getElementById(`cafeId`).value;
    
    fetch(`/haiku/${cafe_id}`)
    .then(response => response.json(
        console.log(response)
    ))
    .then(data => {
        const line_1 = document.getElementById('haikuLine1');
        const line_2 = document.getElementById('haikuLine2');
        const line_3 = document.getElementById('haikuLine3');
        line_1.innerText = data['line_1'];
        line_2.innerText = data['line_2'];
        line_3.innerText = data['line_3'];
    })
    .catch(error => {
        console.log('Error:', error);
    });    
}

function save_edit(event) {
    // Save cafe description
    event.preventDefault();
    const csrftoken = Cookies.get('csrftoken');
    const cafe_id = document.getElementById(`cafeId`).value;
    const text = document.getElementById('descriptionText').value

    fetch(`/save_edit/${cafe_id}`, {
        credentials: 'include',
        method: 'PUT',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            text: text
        })
    })
        .then(response => response.json())
        .then(data => {
            refresh_description(data['description']);
        })        
        .catch(error => {
            console.log('Error:', error);
        });

        save_additional_images(event, csrftoken)
  }

  function save_additional_images(event, csrftoken) {
    // Save cafe images   
    // https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#uploading_multiple_files 
    const cafe_id = document.getElementById(`cafeId`).value;
    const photos = document.querySelector('input[type="file"][multiple]');
    const formData = new FormData();

    for (const [i, photo] of Array.from(photos.files).entries()) {
        formData.append(`images_${i}`, photo);
      }   

      fetch(`/save_edit/${cafe_id}`, {
        credentials: 'include',
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: formData,
    })
        .then(response => response.json())
        .catch(error => {
            console.log('Error:', error);
        });
      
  }

  function refresh_description(text) {
    // Refreshes description in the cafe page to match the one saved after editing
    current_text = document.getElementById('cardTextDescription').parentNode.children[3];
    const haikuLines = text.split("\n");
    const replacement_p = document.createElement('p');

    haikuLines.forEach(line => {
        replacement_p.innerHTML += line + "<br />";
    })    

    // Remove final line break
    last_line_break = replacement_p.lastChild;
    last_line_break.remove();

    current_text.replaceWith(replacement_p);
  }