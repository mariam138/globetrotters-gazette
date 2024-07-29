// Allow DOM to fully load before executing click event
document.addEventListener('DOMContentLoaded', (event) => {

    // Get back button on post detail page
    let backButton = document.getElementById('back-btn');

    if (backButton) {
        backButton.addEventListener('click', () => {
            history.back();
        });
    }
});

// Get the button to generate the tooltip
let emailInfoButton = document.getElementById('email-tooltip');
let emailTooltip = new bootstrap.Tooltip(emailInfoButton);

// Cloudinary Uploader Widget
// Initialises and creates widget
let cloudinaryWidget = cloudinary.createUploadWidget(
    {cloudName: "dy1xfelbe", uploadPreset: "blog_image" },
    function (error, result) {
        if (!error && result && result.event === "success") { 
            console.log(result.info.secure_url); 
     }});


  widget.open();