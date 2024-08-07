// Allow DOM to fully load before executing click event
document.addEventListener('DOMContentLoaded', (event) => {

    // Get back button on post detail page
    let backButton = document.getElementsByClassName('back-btn');

    if (backButton) {
        backButton.addEventListener('click', () => {
            history.back();
        });
    }

    // // Code adapted from Cloudinary docs
    // // https://cloudinary.com/documentation/upload_widget_reference#initialization_methods
    // let cloudinaryWidget = cloudinary.createUploadWidget({
    //         cloudName: "dy1xfelbe",
    //         uploadPreset: "blog_image",
    //         // Allow only one picture to be uploaded to be used as the hero image for the post
    //         multiple: false,
    //         // Allow the user to crop their pictures
    //         cropping: true,
    //         // Enforces a 16:9 cropping ratio so the image is suitable to be displayed as a hero image
    //         croppingAspectRatio: 1.78,
    //         // Only allows images to be uploaded
    //         resourceType: "image",
    //         // Specifies image formats allowed to client
    //         clientAllowedFormats: ["jpg", "jpeg", "webp", "png",],
    //         // Only allows images of 5MB to be uploaded, performs validation
    //         maxImageFileSize: 5000000,
    //         // Prevents widget from automatically closing after one file upload
    //         singleUploadAutoClose: false,

    //     },
    //     function (error, result) {
    //         // Getting the image url from the uploaded photo from the widget is adapted from:
    //         // https://stackoverflow.com/questions/61153317/how-to-get-the-cloudinary-widget-image-info-on-upload
    //         if (!error && result && result.event === "success") {
    //             // Gets the hidden input field from the create post form
    //             let imageUrl = document.getElementById('image_url');
    //             // Sets the value of the hidden input form as the url of the picture uploaded
    //             imageUrl.value = result.info.secure_url;

    //             // Gets input field after upload button
    //             let imageName = document.getElementById('image-name');
    //             // Sets the placeholder text to the name of the image uploaded
    //             imageName.placeholder = result.info.public_id;
    //         }
    //     });

    // // Gets upload button from post creation page
    // let uploadBlogImg = document.getElementById('upload-img');
    // uploadBlogImg.addEventListener('click', () => {
    //     cloudinaryWidget.open();
    // }, false);
});

// Get the button to generate the tooltip
let emailInfoButton = document.getElementById('email-tooltip');
let emailTooltip = new bootstrap.Tooltip(emailInfoButton);
