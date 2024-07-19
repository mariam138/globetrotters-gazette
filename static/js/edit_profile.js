// Set cloud name for Cloudinary
cloudinary.setCloudName("dy1xfelbe");

// Create the widget for profile picture upload
let profilePicWidget = cloudinary.createUploadWidget({
    uploadPreset: 'profile_img',
    cropping: true
}, (error, result) => {
    console.log(error, result)
})