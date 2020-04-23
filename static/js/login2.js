$(function () {
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
    }).on('success.form.fv', function(e) {
        e.preventDefault();
        var $form = $(e.target);
        var fv = $form.data('formValidation');
        var data = {
            username : $('#id_username').val().trim(),
            password : $('#id_password').val().trim()
        };
        $('#btnLogin').attr('disabled',true);
        $.ajax({
                 dataType: 'JSON',
                 type: 'POST',
                 url : '/connect/',
                 data: data,
                 beforeSend : function(){
                    $('#id_password').val('');
                    $('#id_username').val('').focus();
                 },
                 success : function(data){
                     if(data.resp  == true){
                        $.isLoading({
                             text: "<strong>Iniciando sesión...</strong>",
                             tpl: '<span class="isloading-wrapper %wrapper%"><i class="fa fa-circle-o-notch fa-2x fa-spin"></i><br>%text%</span>',
                        });
                        setTimeout( function(){
                          $.isLoading("hide");
                            window.location = '/';
                        },2000);
                        return false;
                     }
                     message(data.error);
                 },
                 error: function(jqXHR, textStatus, errorThrown){
                     message(errorThrown + ' ' + textStatus);
                 }
            }).done(setTimeout(function(){
                $('#btnLogin').attr('disabled',false);
            },2000));
    });

});
