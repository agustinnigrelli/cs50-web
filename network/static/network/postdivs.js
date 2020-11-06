document.addEventListener('DOMContentLoaded', function() {

    // Toggle between the views
    document.querySelector('#edit').addEventListener('click', () => post_edit(event.target.dataset.id))
    document.querySelector('#comment').addEventListener('click', () => post_comment(event.target.dataset.id))
    document.querySelector('#show-comments').addEventListener('click', () => show_comments(event.target.dataset.id))

    // By default show the post_view of all elements (Selected by class)
    var i;
    var postedit = document.querySelectorAll('div.post-edit');
    for(i = 0; i < postedit.length; i++) {
        postedit[i].style.display = 'none';
    }

    var postcomment = document.querySelectorAll('div.post-comment');
    for(i = 0; i < postedit.length; i++) {
        postcomment[i].style.display = 'none';
    }

    var commentview = document.querySelectorAll('div.comment-view');
    for(i = 0; i < postedit.length; i++) {
        commentview[i].style.display = 'none';
    }
    
    var postview = document.querySelectorAll('div.post-view');
    for(i = 0; i < postedit.length; i++) {
        postview[i].style.display = 'block';
    }
});

function post_edit(id) {

    event.preventDefault();

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