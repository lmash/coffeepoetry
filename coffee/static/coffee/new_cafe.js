document.addEventListener('DOMContentLoaded', function () {

    const editLinks = document.querySelectorAll('.new-cafe');
    editLinks.forEach(post => {
        post.addEventListener('click', event => {
            edit_post(event);
        })
    })
})