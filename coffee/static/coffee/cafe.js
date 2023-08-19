document.addEventListener('DOMContentLoaded', function () {

//    const editLinks = document.querySelectorAll('.img-cafe');
//    editLinks.forEach(post => {
//        post.addEventListener('click', event => {
//            edit_post(event);
//        })
//    })

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