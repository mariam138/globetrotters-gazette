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
// Gets all delete buttons by class name
let deleteButtons = document.getElementsByClassName('delete-btn');
// Get delete button from modal by id name
let confirmDelete = document.getElementById('confirm-delete');

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
* Code adapted from https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+4/courseware/713441aba05441dfb3a7cf04f3268b3f/21a16093c0084895a6073422447c3f7d/
*/
for (let button of editButtons) {
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

// Create modal using javascript
const delCommentModal = new bootstrap.Modal(document.getElementById('deleteCommentModal'))


for (let button of deleteButtons) {
    button.addEventListener('click', (e) => {
        let commentId = e.target.getAttribute('comment_id');
        // Opens modal when button is clicked
        delCommentModal.show();
        // button.href = `${url}delete_comment/${commentId}/`;
    })
}
