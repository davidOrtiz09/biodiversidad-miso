function addListener(){
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

}

function agregarFavorito(idSpecie, idUser){
    console.log("Valores: ",idSpecie,idUser);
    $.ajax({
        type: "POST",
        url: "https://g2-biodiversidad-miso.herokuapp.com/addFavorite/",
        data: JSON.stringify({user:idUser,
                                specie:idSpecie}),
        contentType: "application/json; charset=utf-8;",
        dataType: "json",
        success: function (data) {
            alert("Favorito Agregado");
        },
        failure: function (errMsg) {
            alert("Hubo un error agregando el favorito, por favor vuelve a intentarlo")
        }
    })
    return false
}

