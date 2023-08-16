document.addEventListener('DOMContentLoaded', function () {

    const editLinks = document.querySelectorAll('.img-cafe');
    editLinks.forEach(post => {
        post.addEventListener('click', event => {
            edit_post(event);
        })
    })
})