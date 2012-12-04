
function get_channel(){
    new Ajax.Request('/auto/ajax_purpose_staff/', { 
    method: 'post',
    parameters: $H({'repId':$('id_repId').getValue()}),
    onSuccess: function(transport) {
        var e = $('id_channel')
        if(transport.responseText)
            e.update(transport.responseText)
    }
    }); // end new Ajax.Request
}