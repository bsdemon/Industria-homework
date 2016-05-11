'use strict';

$(document).ready(function () {

    $('#calc-form').on('submit', function (event) {
        event.preventDefault();
        calculate();
    });

    function calculate() {
        console.log('Calculate working!');
        var csrftoken = getCookie('csrftoken');
        
        var from_currency = $('#id_from_currency').find('option:selected').val();
        var to_currency = $('#id_to_currency').find('option:selected').val();
        var units = $('#id_units').val();
        
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: "calc/",
            type: "POST",
            data: {
                from_currency : from_currency,
                to_currency : to_currency,
                units : units
            },

            success: function (data) {
                $('#calc-result').text(data);
            },

            error: function (xhr, errmsg) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            }
        });
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
});


