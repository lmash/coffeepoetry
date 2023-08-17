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
})