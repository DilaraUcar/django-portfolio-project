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



  //document.addEventListener("DOMContentLoaded", function() {
    //let editButtons = document.getElementsByClassName("btn-edit");
    //const commentText = document.getElementById("id_body");
    //const commentForm = document.getElementById("commentForm");
    //const submitButton = document.getElementById("submitButton");

    //const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    //const deleteButtons = document.getElementsByClassName("btn-delete");
    //const deleteConfirm = document.getElementById("deleteConfirm");

    //function getPostSlug() {
        //const currentUrl = window.location.href;
        //const urlParts = currentUrl.split('/');
        //return urlParts[urlParts.length - 2];
    //}

    //for (let button of editButtons) {
        //button.addEventListener("click", (e) => {
            //let commentId = e.target.getAttribute("data-comment_id");
            //let commentContent = document.getElementById(`comment${commentId}`).innerText;
            //commentText.value = commentContent;
            //submitButton.innerText = "Update";
            //commentForm.setAttribute("action", `${getPostSlug()}/edit_comment/${commentId}`);
        //});
    //}

    //for (let button of deleteButtons) {
        //button.addEventListener("click", (e) => {
            //let commentId = e.target.getAttribute("data-comment_id");
            //const confirmDeleteButton = document.getElementById("deleteConfirm");
            //confirmDeleteButton.setAttribute("data-comment_id", commentId);
            //deleteModal.show();
        //});
    //}

    // Add event listener for the cancel button
    //document.querySelector('#deleteModal .btn-secondary').addEventListener('click', function() {
        //deleteModal.hide();
    //});

    // Ensure the "x" button in the modal header hides the modal properly
    //document.querySelector('#deleteModal .btn-close').addEventListener('click', function() {
        //var deleteModal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
        //deleteModal.hide();
    //});

    //deleteConfirm.addEventListener("click", function() {
        //let commentId = this.getAttribute("data-comment_id");
        //console.log("Delete comment with ID:", commentId);

        // Fetch CSRF token from the cookie
        //const csrftoken = getCookie('csrftoken');

        //fetch(`/${getPostSlug()}/delete_comment/${commentId}`, {
            //method: 'DELETE',
            //headers: {
                //'Content-Type': 'application/json',
                //'X-CSRFToken': csrftoken, // Include CSRF token in the request headers
            //},
        //})
        //.then(response => {
            //if (response.ok) {
                //console.log('Comment deleted successfully.');
                //deleteModal.hide(); // Close the modal
                //location.reload(); // Reload the page to reflect the deletion
            //} else {
                //console.error('Failed to delete comment.');
                // Optionally, display an error message to the user
            //}
        //})
        //.catch(error => {
            //console.error('Error:', error);
            // Optionally, display an error message to the user
        //});
    //});

    // Function to extract CSRF token from the cookie
    //function getCookie(name) {
        //let cookieValue = null;
        //if (document.cookie && document.cookie !== '') {
            //const cookies = document.cookie.split(';');
            //for (let i = 0; i < cookies.length; i++) {
                //const cookie = cookies[i].trim();
                // Check if the cookie name matches the one we're looking for
                //if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    //cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    //break;
                //}
            //}
        //}
        //return cookieValue;
    //}

//});