// Get the button to generate the tooltip
let emailInfoButton = document.getElementById('email-tooltip');
let emailTooltip = new bootstrap.Tooltip(emailInfoButton);

// Get back button from post detail page
let backButton = document.getElementById('back-btn');

console.log('Script is running');

if (backButton){
    backButton.addEventListener('click', () => {
        console.log('back');
    })
} else {
    console.log('Button not found');
}