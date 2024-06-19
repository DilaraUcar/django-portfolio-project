document.addEventListener('DOMContentLoaded', function() {
    const postingButton = document.getElementById('posting-button');
    const closeButton = document.getElementById('close-form');
    
    if (postingButton) {
        postingButton.addEventListener('click', function() {
            // Toggle the visibility of the form
            const form = document.getElementById('post-form-container');
            if (form && (form.style.display === 'none' || form.style.display === '')) {
                form.style.display = 'block';
            } else if (form) {
                form.style.display = 'none';
            }
        });
    }
    
    if (closeButton) {
        closeButton.addEventListener('click', function() {
            const form = document.getElementById('post-form-container');
            if (form) {
                form.style.display = 'none';
            }
        });
    }
});

