document.addEventListener("DOMContentLoaded", function (event) {
    fetch(`${window.origin}/hero`)
    .then(response => response.json())
    .then(data => console.log(data));
});


