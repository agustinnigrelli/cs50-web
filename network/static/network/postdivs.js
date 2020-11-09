document.addEventListener('DOMContentLoaded', function() {

    let i;
    // Toggle between the views
    let edit = document.querySelectorAll('.edit');
    for(i = 0; i < edit.length; i++) {
        edit[i].addEventListener('click', () => post_edit(event.target.dataset.id))
    }

    let comment = document.querySelectorAll('.comment');
    for(i = 0; i < comment.length; i++) {
        comment[i].addEventListener('click', () => post_comment(event.target.dataset.id))
    }

    let showcomments = document.querySelectorAll('.showcomments');
    for(i = 0; i < showcomments.length; i++) {
        showcomments[i].addEventListener('click', () => show_comments(event.target.dataset.id))
    }

    // By default show the post_view of all elements (Selected by class)
    reset_views();

});

function reset_views() {

    let postedit = document.querySelectorAll('div.post-edit');
    for(i = 0; i < postedit.length; i++) {
        postedit[i].style.display = 'none';
    }

    let postcomment = document.querySelectorAll('div.post-comment');
    for(i = 0; i < postedit.length; i++) {
        postcomment[i].style.display = 'none';
    }

    let commentview = document.querySelectorAll('div.comment-view');
    for(i = 0; i < postedit.length; i++) {
        commentview[i].style.display = 'none';
    }
    
    let postview = document.querySelectorAll('div.post-view');
    for(i = 0; i < postedit.length; i++) {
        postview[i].style.display = 'block';
    }

}

function post_edit(id) {

    event.preventDefault();

    // Hide all previous visible divs of post-edit
    reset_views();

    // Show the edit textarea and hyde the post_view
    document.querySelector(`#post-edit-${id}`).style.display = 'block';
    document.querySelector(`#post-comment-${id}`).style.display = 'none';
    document.querySelector(`#post-view-${id}`).style.display = 'none';
}

function post_comment(id) {

    event.preventDefault();

    // Show a textarea to leave a comment
    document.querySelector(`#post-edit-${id}`).style.display = 'none';
    document.querySelector(`#post-comment-${id}`).style.display = 'block';
    document.querySelector(`#post-view-${id}`).style.display = 'block';
}

function show_comments(id) {

    event.preventDefault();

    document.querySelector(`#post-edit-${id}`).style.display = 'none';
    document.querySelector(`#post-comment-${id}`).style.display = 'none';
    document.querySelector(`#post-view-${id}`).style.display = 'block';

    // Toggle comment section
    if (document.querySelector(`#comment-view-${id}`).style.display = 'none') {
        document.querySelector(`#comment-view-${id}`).style.display = 'block';
    } else {
        document.querySelector(`#comment-view-${id}`).style.display = 'none';
    }

}