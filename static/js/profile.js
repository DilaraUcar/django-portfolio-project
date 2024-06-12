document.addEventListener('DOMContentLoaded', function() {
    console.log("I'm attached")
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
    function confirmDelete() {
        console.log("confirm delete called");
        // Submit the hidden delete form
        document.getElementById('delete-form').submit();
    }

    // Ensure that the edit button is properly linked to the editAbout function
    document.getElementById('edit-btn').addEventListener('click', editAbout);
    console.log("edit button = ", document.getElementById('edit-btn'));

    // Ensure that the cancel button is properly linked to the cancelEdit function
    document.querySelector('#edit-about .btn-secondary').addEventListener('click', cancelEdit);

    // Ensure that the delete button shows the delete confirmation modal
    document.getElementById('btn-delete').addEventListener('click', function() {
        // Show the delete confirmation modal
        var deleteModal = new bootstrap.Modal(document.getElementById('deleteAccountModal'));
        deleteModal.show();
    });

    // Ensure that the confirm delete button is properly linked to the confirmDelete function
    document.getElementById('confirmDelete').addEventListener('click', confirmDelete);

    // Ensure the cancel button in the modal hides the modal properly
    document.querySelector('#deleteAccountModal .btn-secondary').addEventListener('click', function() {
        var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteAccountModal'));
        deleteModal.hide();
    });

    const closeButtons = document.querySelectorAll(".clear-bd")

    closeButtons.forEach((button) => {
        button.addEventListener('click', () => {
            let backdrops = document.querySelectorAll('div.modal-backdrop')
            setTimeout(() => {
                backdrops.forEach((backdrop) => {
                    backdrop.remove()
                })
            }, 1000)
        })
    })
});