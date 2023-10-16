// Post Office JavaScript

function main() {
    // Get the values entered by the user
    var length = document.getElementById("l").value;
    var height = document.getElementById("h").value;
    var thickness = document.getElementById("t").value;
    var zipto = document.getElementById("zipto").value;
    var zipfrom = document.getElementById("zipfrom").value;

    // Send messages in the console showing the values of each submitted value
    console.log("DEBUG: " + length);
    console.log("DEBUG: " + height);
    console.log("DEBUG: " + thickness);
    console.log("DEBUG: " + zipto);
    console.log("DEBUG: " + zipfrom);

  
    // Display an alert with the submitted values
    alert("\nLength: " + length + "\nEmail: " + height + "\nThickness: " + thickness);
}
function calculate() {

}