document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll('.bookmark').forEach( function (button) {
        button.addEventListener('click', () => bookmark(event.target.dataset.id))
    })

});

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

function bookmark(id) {

    // Inicialize counter with the current count
    const announcement_id = id;
    let bookmark = document.querySelector(`#bookmark-status-${id}`).value;

    if (bookmark === "false") {
        bookmark = "true";
        document.querySelector(`#bookmark-${id}`).className = 'fa fa-bookmark fa-2x bookmark'
    } else {
        bookmark = "false";
        document.querySelector(`#bookmark-${id}`).className = 'fa fa-bookmark-o fa-2x bookmark'
    }

    document.querySelector(`#bookmark-status-${id}`).value = bookmark;

    fetch('/bookmark', {
        credentials: 'include',
            method: 'POST',
            mode: 'same-origin',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') 
            },
            body: JSON.stringify({
                bookmark: bookmark,
                announcement_id: announcement_id
            })
        })
        .then(response => response.text())
        .then(result => {
            // Print result
            console.log(result);
    })
        
}