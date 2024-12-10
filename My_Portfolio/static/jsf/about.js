const openButton = document.getElementById("openButton");
const slider = document.getElementById("slider");
const closeIcon = document.getElementById("closeIcon");
const hide = document.getElementById("hide");
const seek = document.getElementById("seek");
const bt = document.getElementById("bt");

        // Open the slider when the button is clicked
openButton.addEventListener("click", () => {
    slider.style.display = "flex"; // Show the popup
    openButton.style.display = "none"; 
    hide.style.display = "none"; 
    seek.style.display = "none"; 
    bt.style.display = "none"; 
    document.body.style.overflow = 'hidden'; // Disable scrolling

});

        // Close the slider when the close icon is clicked
closeIcon.addEventListener("click", () => {
        slider.style.display = "none"; // Hide the popup
        openButton.style.display = "block";
        document.body.style.overflow = '';
        hide.style.display = ""; 
        seek.style.display = ""; 
        bt.style.display = ""; 
});

// Remove message

setTimeout(() => {
        const messageContainer = document.getElementById('message-container');
        if (messageContainer) {
            messageContainer.remove();
        }
    }, 2000);