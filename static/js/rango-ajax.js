'use strict'
/**
 * Created by eon on 4/28/16.
 */
$(document).ready(function () {
    var first_currency;
    var second_currency;
    var second_name;
    var units;

    $('.calc').change(function () {
        units = $('#units_form').val();
        first_currency = $('#first_form option:selected').val();
        second_currency = $('#second_form option:selected').val();
        second_name = $('#second_form').find(":selected").text();
        calc_result(units, first_currency, second_currency, second_name)
    });

    function calc_result(units, first_currency, second_currency,second_name) {
        if (first_currency !== 0 || second_currency !== 0) {
            var result  = Math.round(units * first_currency * second_currency*100000)/100000;
            $('#final_result').text(result);
            $('#final_result_name').text(second_name)
        }
    }
});


