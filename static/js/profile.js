document.addEventListener('DOMContentLoaded', function() {
    // Function to toggle between showing/hiding the edit form
    function editAbout() {
        console.log("edit about called");
        document.getElementById('about').style.display = 'none';
        document.getElementById('edit-about').style.display = 'block';
    }

    // Function to cancel editing and revert back to displaying profile information
    function cancelEdit() {
        console.log("cancel edit called");
        document.getElementById('edit-about').style.display = 'none';
        document.getElementById('about').style.display = 'block';
    }

    // Function to confirm deletion of account
    document.getElementById('btn-delete').addEventListener('click', function() {
        // Show the delete confirmation modal
        var deleteModal = new bootstrap.Modal(document.getElementById('deleteAccountModal'));
        deleteModal.show();
    });

    // Ensure that the edit button is properly linked to the editAbout function
    document.getElementById('edit-btn').addEventListener('click', editAbout);
    console.log("edit button = ", document.getElementById('edit-btn'));

    // Ensure that the cancel button is properly linked to the cancelEdit function
    document.querySelector('#edit-about .btn-secondary').addEventListener('click', cancelEdit);
});
