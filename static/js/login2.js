window.$(function () {
    $('#frm-login').formValidation({
        message: 'This value is not valid',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            username: {
                validators: {
                    notEmpty: {},
                    stringLength: {
                        min: 3,
                        max: 25
                    }
                }
            },
            password: {
                validators: {
                    notEmpty: {},
                    stringLength: {
                        min: 3,
                        max: 15
                    }
                }
            }
        }
    }).on('success.form.fv', function (e) {
        e.preventDefault();
        var $form = window.$(e.target);
        var fv = $form.data('formValidation');
        var data = {
            username: window.$('#id_username').val().trim(),
            password: window.$('#id_password').val().trim(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
        };
        $('#btnLogin').attr('disabled', true);
        $.ajax({
            dataType: 'JSON',
            type: 'POST',
            url: '/connect/',
            data: data,

            beforeSend: function () {
                $('#id_password').val('');
                $('#id_username').val('').focus();
            },
            success: function (data) {
                if (data.resp === true) {
                    window.$.isLoading({
                        text: "<strong>Iniciando sesión...</strong>",
                        tpl: '<span class="isloading-wrapper %wrapper%"><i class="fa fa-circle-o-notch fa-2x fa-spin"></i><br>%text%</span>',
                    });
                    setTimeout(function () {
                        window.$.isLoading("hide");
                        window.location = '/';
                    }, 2000);
                    return false;
                } else {
                    window.bootbox.dialog({
                    title: "<i class='fa fa-exclamation-circle' aria-hidden='true'></i> Error",
                    message: data.error,
                    buttons: {
                        success: {
                            label: "<i class='fa fa-check'>OK</i>",
                            className: "btn btn-primary btn-flat",
                        }
                    }
                });
                }
            },
            error: function (jqXHR, textStatus, errorThrown) {
                window.message(errorThrown + ' ' + textStatus);
            }
        }).done(setTimeout(function () {
            window.$('#btnLogin').attr('disabled', false);
        }, 2000));
    });

});
