$('#deleteModal').on('show.bs.modal', function(event){
    let button = event.relatedTarget;
    let user_id = $(button).attr('data-bs-user');
    let url = $(button).attr('data-bs-url');
    $('#deleteModal .modal-user-id').text(user_id);
    $('#deleteModal .btn-delete').prop('href', url)
});
