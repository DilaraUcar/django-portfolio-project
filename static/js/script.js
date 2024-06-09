document.addEventListener('DOMContentLoaded', function() {
    const postFormContainer = document.getElementById('post-form-container');
    const postingButton = document.getElementById('posting-button');
    const closeButton = document.getElementById('close-form');
    
    if (postFormContainer && postingButton) {
        postingButton.addEventListener('click', function() {
            // Toggle the visibility of post-form-container
            if (postFormContainer.style.display === 'none') {
                postFormContainer.style.display = 'block';
            } else {
                postFormContainer.style.display = 'none';
            }
        });
    }
    
    if (closeButton) {
        closeButton.addEventListener('click', function() {
            postFormContainer.style.display = 'none';
        });
    }
});