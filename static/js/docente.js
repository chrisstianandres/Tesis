
$(function () {
    $('#frm_objeto').formValidation({
        message: 'Esto no es un valor valido',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                validators: {
                    notEmpty: {
                        message: 'Este campo debe ser obligatorio'
                    },
                    stringLength: {
                        min: 5,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
            first_name: {
                validators: {
                    notEmpty: {
                        message: 'Este campo debe ser obligatorio'
                    },
                    stringLength: {
                        min: 7,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
            last_name: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 5,
                    },
                    regexp: {
                        regexp: /^[A-ZáéíóúÁÉÍÓÚñÑ\s]+$/i,
                        message: 'Solo introduzca letras'
                    },
                }
            },
            cedula: {
                 validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 10,
                        max: 10
                    },
                    regexp: {
                        regexp: /^[0-9]/i,
                        message: 'Solo introduzca numeros'
                    },
                }
            },
            telefono: {
                 validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 10,
                        max: 10,
                    },
                    regexp: {
                        regexp: /^[0-9]/i,
                        message: 'Solo introduzca numeros'
                    },
                }
            },
            direccion: {
                validators: {
                    notEmpty: {
                        message: 'Este campo es obligatorio'
                    },
                    stringLength: {
                        min: 5,
                    },
                }
            },
            password1: {
                    validators: {
                        notEmpty: {
                            message: 'La contraseña es Requerida'
                        }
                    }
                },
             password2: {
                    validators: {
                        identical: {
                            compare: function() {
                                return form.querySelector('[name="password1"]').value;
                            },
                            message: 'La contrseña y la confirmacion no son iguales'
                        }
                    }
                },
        }
    });

});
