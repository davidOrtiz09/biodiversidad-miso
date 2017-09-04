$('.verDetalle').on('click', function (event) {
    var id = $(this).attr('name');
    $.ajax({
        url: "/especie/"+id,
        context: document.body
    }).done(function(response) {
        $("#detalleEspecie").html(response);
        $("#detalleEspecie").modal('show');
    });

});


$('.closeDetalle').on('click', function(event){
    $("#detalleEspecie").modal('hide');
    $(".modal-backdrop").remove();
});


