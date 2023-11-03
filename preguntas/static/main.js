console.log('si funciono');
$(document).ready(function() {
    $("#preguntas-form").on("submit", function(event) {
        event.preventDefault(); // Prevenir la acción predeterminada del formulario

        var formData = $(this).serialize(); // Serializar los datos del formulario
        $.post("/preguntas/", formData, function(response) {
            // Manejar la respuesta del servidor aquí
            console.log(response);
        });
    });
});