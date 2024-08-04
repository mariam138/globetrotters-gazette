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

let url = document.getElementById('url').getAttribute('data-url');
let cancelCommentUrl = document.getElementById('cancel-comment-url').getAttribute('data-url');

for (let button of editButtons){
    button.addEventListener('click', (e) => {
        let commentId = e.target.getAttribute('comment_id');
        let commentContent = document.getElementById(`comment-${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = 'Update';
        // Set form action to url set for edit comment view
        commentForm.setAttribute('action', `${url}edit_comment/${commentId}/`);

        // Creates a cancel button which appears next to the 'Update' button
        let cancelEditBtn = document.createElement('a');
        // Sets html for link
        cancelEditBtn.innerHTML = `<a class="btn btn-danger btn-text ms-1" href="${cancelCommentUrl}" role="button">Cancel</a>`;
        // Appends anchor element after the submit/update button
        // After method adapted from:
        // https://developer.mozilla.org/en-US/docs/Web/API/Element/after
        submitButton.after(cancelEditBtn);
    })
}
