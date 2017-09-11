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


function agregarFavorito(idSpecie, idUser){
    alert("BIen");
    console.log("Valores: ",idSpecie,idUser);
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/addFavorite/",
        data: JSON.stringify({user:idUser,
                                specie:idSpecie}),
        contentType: "application/json; charset=utf-8;",
        dataType: "json",
        success: function (data) {
            alert("Lo logró");
        },
        failure: function (errMsg) {
            alert("Hubo un error agregando el favorito, por favor vuelve a intentarlo")
        }
    })
    return false
}

