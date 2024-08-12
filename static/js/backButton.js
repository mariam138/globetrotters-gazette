// Get back button on post detail page
let backButtons = document.getElementsByClassName('back-btn');

// loop through back buttons as they are defined by class name
for (var button of backButtons) {
    button.addEventListener('click', () => history.back());
}