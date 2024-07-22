// Set cloud name for Cloudinary
cloudinary.setCloudName("dy1xfelbe");
// Gets 'Choose file' button from upload field
let uploadButton = document.getElementById("button-addon1");

// Create the widget for profile picture upload
let profilePicWidget = cloudinary.createUploadWidget({
    uploadPreset: "profile_img",
    cropping: true
}, (error, result) => {
    console.log(error, result)
});


// Create event listener to open the widget when the button is clicked
uploadButton.addEventListener("click", () => {
    profilePicWidget.open();
    }, false);

