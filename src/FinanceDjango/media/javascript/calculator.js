form_count = $("[name=extra_field_count");
// get extra form count so we know what index to use for the next item.
$("#add-another").click(function() {
    element = $('<input type="text"/>');
    element.attr('name', 'extra_field_' + form_count);
    $("#forms").append(element);
    // build element and append it to our forms container

    form_count ++;
    $("[name=extra_field_count]").val(form_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
})