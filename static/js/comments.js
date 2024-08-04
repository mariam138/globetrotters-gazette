/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/

// Gets all edit buttons on page by their class name
let editButtons = document.getElementsByClassName('edit-btn');
// Gets text of the comment where the id is the id of the form's text area
let commentText = document.getElementById('id_body');
// Gets comment form
let commentForm = document.getElementById('comment-form');
// Gets comment form's submit button
let submitButton = document.getElementById('submit-btn');

for (let button of editButtons){
    button.addEventListener('click', (e) => {
        let commentId = e.target.getAttribute('comment_id');
        let commentContent = document.getElementById(`comment-${commentId}`).innerText;
        // let commentBody = commentContent.getElementById('comment-body').innerText;
        commentText.value = commentContent;
        submitButton.innerText = 'Update';
        // Gets the current url for the page
        let url = window.location.href;
        commentForm.setAttribute('action', `${url}/edit_comment/${commentId}/`);
    })
}
