// Get the text field
var copyText = document.getElementById("short-url-link");

function copyLink() {
    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.value);
    // Alert the copied text
    alert("Copied the text: " + copyText.value);
  }

  function copyToClipBoard() {
    navigator.clipboard.writeText(copyText);
    alert("Copied the text");
}