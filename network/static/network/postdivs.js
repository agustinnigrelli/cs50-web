document.addEventListener('DOMContentLoaded', function() {

    // Toggle between the views
    document.querySelector('#edit').addEventListener('click', () => post_edit())
    document.querySelector('#comment').addEventListener('click', () => post_comment())
    document.querySelector('#show-comments').addEventListener('click', () => show_comments())

    // By default show the post_view
    document.querySelector('#post-edit').style.display = 'none';
    document.querySelector('#post-comment').style.display = 'none';
    document.querySelector('#comment-view').style.display = 'none';
    document.querySelector('#post-view').style.display = 'block';
});

function post_edit() {

    event.preventDefault();

    // Show the edit textarea and hyde the post_view
    document.querySelector('#post-edit').style.display = 'block';
    document.querySelector('#post-comment').style.display = 'none';
    document.querySelector('#post-view').style.display = 'none';
}

function post_comment() {

    event.preventDefault();

    // Show a textarea to leave a comment
    document.querySelector('#post_edit').style.display = 'none';
    document.querySelector('#post_comment').style.display = 'block';
    document.querySelector('#post_view').style.display = 'block';
}

function show_comments() {

    event.preventDefault();

    document.querySelector('#post_edit').style.display = 'none';
    document.querySelector('#post_comment').style.display = 'none';
    document.querySelector('#post_view').style.display = 'block';

    // Toggle comment section
    if (document.querySelector('#comment_view').style.display = 'none') {
        document.querySelector('#comment_view').style.display = 'block';
    } else {
        document.querySelector('#comment_view').style.display = 'none';
    }

}