// Function to open the delete modal
function openDeleteModal() {
    var deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    deleteModal.show();
  }
  
  // Function to confirm deletion
  function confirmDelete() {
    // Select the form with the class 'delete-form'
    var deleteForm = document.querySelector('.delete-form');
    if (deleteForm) {
        deleteForm.submit(); // Submit the form
    } else {
        console.error("Form element with class 'delete-form' not found.");
    }
  }
  
  // Ensure the cancel button in the modal hides the modal properly
  document.querySelector('#deleteModal .btn-secondary').addEventListener('click', function() {
    var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
    deleteModal.hide();
  });
  
  // Handle the confirm delete button
  document.getElementById('deleteConfirm').addEventListener('click', confirmDelete);
