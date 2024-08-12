/* Gets the Profile Picture label that is rendered from Crispy Forms
* and dynamically adds an extra note stating the max file size
* which is set by Cloudinary. 
* Code to get the first item in a node list is adapted from:
* https://developer.mozilla.org/en-US/docs/Web/API/NodeList/item
* Code to find the label attached to a form input is adapted from:
* https://javascript.plainenglish.io/how-to-find-the-html-label-element-associated-with-a-given-input-with-javascript-486d15710591
*/

// Gets node list for profile picture label
let profileLabelNodes = document.querySelector('#id_profile_picture').labels;
// Selects first item in node list
let profilePictureLabel = profileLabelNodes.item(0);
// Custom HTML for max file size note
let validationText = "<p class='paragraph fs-6'><strong>Note:</strong> Max file size is 10MB</p>";
// Concatenates above text to the profile picture label
profilePictureLabel.innerHTML += validationText;