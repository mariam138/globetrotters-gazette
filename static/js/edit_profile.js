// Set cloud name for Cloudinary
cloudinary.setCloudName("dy1xfelbe");
// Gets the input for uploading a profile picture
let originalUploadButton = document.getElementById("id_profile_pic").disabled = true;

// Create the widget for profile picture upload
let profilePicWidget = cloudinary.createUploadWidget({
    uploadPreset: "profile_img",
    cropping: true
}, (error, result) => {
    console.log(error, result)
});

// let uploadButtonDiv = originalUploadButton.parentNode;
let uploadButtonDiv = document.getElementById("id_profile_pic").parentNode;


// Create event listener to open the widget when the button is clicked
uploadButtonDiv.addEventListener("click", () => {
    console.log('Click!');
    // profilePicWidget.open();
    });
    // false);
