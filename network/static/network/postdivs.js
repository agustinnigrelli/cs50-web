document.addEventListener('DOMContentLoaded', function() {

    
    // Perfom specific functions
    document.querySelectorAll('.edit').forEach( function (button) {
        button.addEventListener('click', () => post_edit(event.target.dataset.id))
    })
        
    document.querySelectorAll('.comment').forEach( function (button) {
        button.addEventListener('click', () => post_edit(event.target.dataset.id))
    })

    document.querySelectorAll('.showcomments').forEach( function (button) {
        button.addEventListener('click', () => post_edit(event.target.dataset.id))
    })

    document.querySelectorAll('.like').forEach( function (button) {
        button.addEventListener('click', () => like(event.target.dataset.id))
    })

    // By default show the post_view of all elements (Selected by class)
    reset_views();

});

function reset_views() {

    document.querySelectorAll('div.post-edit').forEach( function(div) {
        div.style.display = 'none';
    })

    document.querySelectorAll('div.post-comment').forEach( function(div) {
        div.style.display = 'none';
    })

    document.querySelectorAll('div.comment-view').forEach( function(div) {
        div.style.display = 'none';
    })
    
    document.querySelectorAll('div.post-view').forEach( function(div) {
        div.style.display = 'block';
    })

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function post_edit(id) {

    event.preventDefault();

    // Hide all previous visible divs of post-edit
    reset_views();

    // Show the edit div and hyde the post_view
    document.querySelector(`#post-edit-${id}`).style.display = 'block';
    document.querySelector(`#post-comment-${id}`).style.display = 'none';
    document.querySelector(`#post-view-${id}`).style.display = 'none';

    // Get the current text from the post
    const body = document.querySelector(`#body-${id}`).innerHTML;

    // Create elements for append in the displaying div
    const div1 = document.createElement("div");
    const div2 = document.createElement("div");
    const label = document.createElement("p");
    const textarea = document.createElement("textarea");
    const save = document.createElement("button");

    // Configure the created elements
    div1.className = "form-group"
    div2.className = "form-group"
    
    label.innerHTML = "Edit this post:"

    Object.assign(textarea, {
        name: "edit-body",
        max_length: "300",
        rows: "2",
        className: `form-control edit-body-${id}`,
        value: `${body}`
    })

    save.className = 'btn btn-primary';
    save.innerHTML = 'Save';

    // Append the elements to the displaying divs
    document.querySelector(`#post-edit-${id}`).append(div1);
    div1.append(label);
    div1.append(textarea);
    document.querySelector(`#post-edit-${id}`).append(div2);
    div2.append(save);
    
    // Send the data to views.py
    save.addEventListener('click', function () {

        event.preventDefault();

        const editbody = textarea.value;
        const post_id = id;
        
        fetch('/edit', {
            credentials: 'include',
            method: 'PUT',
            mode: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify({
                editbody: editbody,
                post_id: post_id
            })
        })
        .then(response => response.text())
        .then(result => {
            // Print result
            console.log(result);
            document.querySelector(`#body-${id}`).innerHTML = editbody;
        })
        // Hide edit view and show post view
        div1.remove();
        div2.remove();
        label.remove();
        textarea.remove();
        save.remove();
        reset_views();
    })
}

function like(id) {

    // Inicialize counter with the current count
    const post_id = id;
    let counter = document.querySelector(`#count-${id}`).innerHTML;
    let like = document.querySelector(`#like-status-${id}`).value;

    if (like === "false") {
        counter++;
        like = "true";
        document.querySelector(`#like-${id}`).className = 'fa fa-heart like'
    } else {
        counter--;
        like = "false";
        document.querySelector(`#like-${id}`).className = 'fa fa-heart-o like'
    }

    document.querySelector(`#like-status-${id}`).value = like;
    document.querySelector(`#count-${id}`).innerHTML = counter;

    fetch('/like', {
        credentials: 'include',
            method: 'POST',
            mode: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify({
                like: like,
                post_id: post_id
            })
        })
        .then(response => response.text())
        .then(result => {
            // Print result
            console.log(result);
    })
        
}

function post_comment(id) {

    event.preventDefault();

    // Show a textarea to leave a comment
    document.querySelector(`#post-edit-${id}`).style.display = 'none';
    document.querySelector(`#post-comment-${id}`).style.display = 'block';
    document.querySelector(`#post-view-${id}`).style.display = 'block';

    // Function pending...
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

