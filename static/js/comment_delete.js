const myDeleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
console.log(myDeleteModal)
const deleteButtons = document.getElementsByClassName("btn-delete");
console.log(deleteButtons)
const deleteConfirm = document.getElementById("deleteConfirm");


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        myDeleteModal.show();
    });
}
