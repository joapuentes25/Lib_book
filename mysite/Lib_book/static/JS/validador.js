$("#formulario1").validate(
    {
        rules: {
            "txtUsuario": {
                required: true,
                minlength: 8
            },
            "txtContraseña": {
                required: true,
                minlength: 10
            },
            "txtNombre": {
                required: true,
                minlength: 5
            },
            "txtRut": {
                required: true
            },
            "txtEmail": {
                required: true
            },
            "datePick": {
                required: true,
                date: true
            },
            "txtTelefono": {
                required: true
            },
            "txtPregunta": {
                required: true,
                minlength: 5
            },




        },
        messages: {
            "txtUsuario": {
                required: "Ingrese Usuario",
                minlength: "mínimo 8 carácteres"
            },
            "txtContraseña": {
                required: "Ingrese Contraseña",
                minlength: "mínimo 10 carácteres"
            },
            "txtNombre": {
                required: "Ingrese Nombre",
                minlength: "mínimo 5 carácteres"
            },
            "txtRut": {
                required: "Ingrese rut"

            },
            "txtEmail": {
                required: "Ingrese correo",
                email: "El correo es invalido"
            },
            "datePick": {
                required: "Ingrese fecha de nacimiento"
            },
            "txtTelefono": {
                required: "Ingrese su numero telefonico"
            },
            "txtPregunta": {
                required: "Respuesta Incorrecta",
                minlength: "mínimo 5 carácteres"
            },

        }


    }



);

$.validator.addMethod("txtRut", function (value, element) {
    return this.optional(element) || $.Rut.validar(value);
}, "Este campo debe ser un rut valido.");

$("#jq-validation").validate();

