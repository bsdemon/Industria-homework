'use strict';
/**
 * Created by eon on 4/28/16.
 */
$(document).ready(function () {
        
    $('#calc').on('submit', function (event) {
        event.preventDefault();
        calculate();
    });

    function calculate() {
        var from_currency, to_currency, units, result = 0;

        from_currency = $('#from-currency').val();
        to_currency = $('#to-currency').val();
        units = $('#units').val();
        var currency_name = $('#to-currency option:selected').text();
        
        if (from_currency != 0 && to_currency != 0 && units != 0){
            result  = Math.round(units * from_currency * to_currency*100000)/100000;
        }

        $('#calc-result').html(result);
        $('#calc-result-currency').text(currency_name+'и')
    }
});


