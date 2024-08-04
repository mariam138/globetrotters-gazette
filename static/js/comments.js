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
// Gets text of the comment
let commentText = document.getElementById('comment-text');
// Gets comment form
let commentForm = document.getElementById('comment-form');
// Gets comment form's submit button
let submitButton = document.getElementById('submit-btn');

for (let button of editButtons){
    button.addEventListener('click', (e) => {
        let commentId = e.target.getAttribute('comment_id');
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = 'Update';
        commentForm.setAttribute('action', `edit_comment/${commentId}`);
    })
}
