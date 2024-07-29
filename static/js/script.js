// Allow DOM to fully load before executing click event
document.addEventListener('DOMContentLoaded', (event) => {

    // Get back button on post detail page
    let backButton = document.getElementById('back-btn');

    if (backButton) {
        backButton.addEventListener('click', () => {
            history.back();
        });
    }


    let cloudinaryWidget = cloudinary.createUploadWidget({
            cloudName: "dy1xfelbe",
            uploadPreset: "blog_image"
        },
        function (error, result) {
            if (!error && result && result.event === "success") {
                // Gets the hidden input field from the create post form
                let imageUrl = document.getElementById('image_url');
                // Sets the value of the hidden input form as the url of the picture uploaded
                imageUrl.value = result.info.secure_url;
            }
        });

    // Gets upload button from post creation page
    let uploadBlogImg = document.getElementById('upload-img');
    uploadBlogImg.addEventListener('click', () => {
        cloudinaryWidget.open();
    }, false);
});

// Get the button to generate the tooltip
let emailInfoButton = document.getElementById('email-tooltip');
let emailTooltip = new bootstrap.Tooltip(emailInfoButton);
