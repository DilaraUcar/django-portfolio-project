function editAbout() {
    document.getElementById("about").style.display = "none";
    document.getElementById("edit-about").style.display = "block";
}

function cancelEdit() {
    document.getElementById("edit-about").style.display = "none";
    document.getElementById("about").style.display = "block";
}

// Ensure the edit form is hidden by default
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("edit-about").style.display = "none";
});
