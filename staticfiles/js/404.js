let backButton = document.getElementsByClassName('back-btn');

    if (backButton) {
        backButton.addEventListener('click', () => {
            history.back();
        });
    }