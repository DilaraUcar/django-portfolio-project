function openEditForm(commentId, commentContent) {
    // Close all edit forms before opening the targeted one
    closeAllEditForms();
    
    // Open the targeted edit form
    var editFormDiv = document.getElementById('edit-comment-form-' + commentId);
    editFormDiv.style.display = 'block';
    
    // Set the initial value of the textarea in the edit form
    var textarea = editFormDiv.querySelector('textarea');
    textarea.value = commentContent; 
}

function closeEditForm(commentId) {
    var editFormDiv = document.getElementById('edit-comment-form-' + commentId);
    editFormDiv.style.display = 'none';
}

function closeAllEditForms() {
    var editForms = document.getElementsByClassName('edit-comment-form');
    for (var i = 0; i < editForms.length; i++) {
        editForms[i].style.display = 'none';
    }
}

function openForm() {
    var postingForm = document.getElementById('posting-form');
    postingForm.style.display = 'block';
    
    // Ensure all edit forms are closed when opening new comment form
    closeAllEditForms();
}

function closeForm() {
    var postingForm = document.getElementById('posting-form');
    postingForm.style.display = 'none';
}
