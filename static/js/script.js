// Allow DOM to fully load before executing click event
document.addEventListener('DOMContentLoaded', (event) => {

    // Get back button on post detail page
    let backButton = document.getElementsByClassName('back-btn');

    if (backButton) {
        backButton.addEventListener('click', () => {
            history.back();
        });
    }

});

