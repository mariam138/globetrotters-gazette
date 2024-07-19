// Set cloud name for Cloudinary
cloudinary.setCloudName("dy1xfelbe");
// Gets the input for uploading a profile picture
let uploadProfilePic = document.getElementById("id_profile_pic");

// Create the widget for profile picture upload
let profilePicWidget = cloudinary.createUploadWidget({
    uploadPreset: "profile_img",
    cropping: true
}, (error, result) => {
    console.log(error, result)
});

// Create event listener to open the widget when the button is clicked
uploadProfilePic.addEventListener("click", () => {
        profilePicWidget.open();
    },
    false);
