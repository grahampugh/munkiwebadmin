// Javascript for catalogs views

$(document).ready(function() {
   $('#catalog_items').dataTable({
        "sDom": "<'row'<'span6'l><'span6'f>r>t<'row'<'span6'i><'span6'p>>",
        "bPaginate": false,
        "sScrollY": "480px",
        "bScrollCollapse": true,
        "bInfo": false,
        "bFilter": true,
        "bStateSave": true,
        "aaSorting": [[0,'asc']]
    });
} );

function getCatalogItem(catalog_name, catalog_index, item_name, item_version)     {
    var catalogItemURL = '/catalog/' + catalog_name + '/' + catalog_index + '/';
    $.get(catalogItemURL, function(data) {
        $('#catalog_item_detail').html(data);
    });
    $('.catalog_item[name="' + item_name + '"]').addClass('selected');
    $('.catalog_item[name!="' + item_name + '"]').removeClass('selected');
}

// copied from manifests.js

function cleanDetailPane() {
  // unbind any existing event handlers for the detail pane
    $('.editable').off('dblclick');
    $('.lineitem_delete').off('click');

    // destroy sortability for existing elements
    //$('.catalogs_section').sortable('destroy');
    //$('.included_manifests_section').sortable('destroy');
    //$('.section').sortable('destroy');
    
    // clear detail pane
    // $('#detail').html('<div></div>')
}


var inEditMode = false;
function makeEditableItems(catalog_item_name) {
    // grab autocomplete data from document
    var autocomplete_data = $('#data_storage').data('autocomplete_data');
    // make sections sortable and drag/droppable
    $('.catalogs_section').sortable();
    $('.section').sortable({
        connectWith: '.section'
    });
    //replace <a> links with 'editable' divs
    $('.lineitem').children($('a')).each(function(){
        var item = "<div class='editable'>" + $(this).parent().attr('id') + "</div>";
        $(this).replaceWith(item);
    });
    $('.lineitem').append("<a href='#' class='btn btn-danger btn-mini lineitem_delete'><i class='icon-minus icon-white'></i><a>");
    $('.catalog_item_section').on('dblclick', '.editable', function() {
        makeEditableItem(manifest_name, autocomplete_data, $(this));
    });
    $('.catalog_item_section').on('click', '.lineitem_delete', function() {
      if ($(this).parent().attr('id')) {    
        var r = confirm("Really delete " + $(this).parent().attr('id') + " from " + $(this).parent().parent().attr('id') + "?");
        if (r == true){ $(this).parent().remove(); };
      } else {
          $(this).parent().remove();
      }
    });
    $('.section_label').append("<a class='btn btn-success btn-mini add_item' href='#'><i class='icon-plus icon-white'></i></a>");
    $('.add_item').click(function() {
        var list_item = $("<li class='lineitem'><div class='editable'></div><a href='#' class='btn btn-danger btn-mini lineitem_delete'><i class='icon-minus icon-white'></i><a></li>");
        $(this).parent().siblings($('ul')).append(list_item);
        makeEditableItem(
            catalog_item_name, autocomplete_data, list_item.children(".editable"));
    });
    $('.edit').val('Save').unbind('click').click(function() {
        getItemDetailFromDOMAndSave();
    });
    $('#save_and_cancel').append("<input type='button' class='cancel btn' value='Cancel' onClick='cancelEdit()'></input>");
    $(window).bind('beforeunload', function(){
        return "Changes will be lost!";
    });
    inEditMode = true;
}

function updateLineItem(item) {
    var text_value = item.val();
    if (text_value.length) {
        item.parent().attr('id', text_value);
        var new_div = $("<div class='editable'>" + text_value + "</div>")
        item.replaceWith(new_div);
    } else {
        item.parent().remove();
    }
}

function makeEditableItem(catalog_item_name, autocomplete_data, editable_div) {
    // commit any existing active lineiteminput
    $('.lineiteminput').each(function(){updateLineItem($(this))});

    var text_value = editable_div.text();
    var input_box = $("<input type='text' id='" + text_value + "' class='lineiteminput' value='" + text_value + "' />");
    var grandparent_id = editable_div.parent().parent().attr('id');
    var kind = 'items';
    if (grandparent_id == 'catalogs') {
      kind = 'catalogs';
    }
    editable_div.replaceWith(input_box);
    input_box.typeahead({source: autocomplete_data[kind]})
    input_box.focus();
    input_box.bind('keyup', function(event) {
        if (event.which == '13' || event.which == '9') {
            event.preventDefault();
            updateLineItem($(this));
        } else if (event.which == '27') {
            event.preventDefault();
            $(this).val($(this).attr('id'));
            updateLineItem($(this));
        }
    });
}

function cancelEdit() {
    inEditMode = false;
    $(window).unbind("beforeunload");
    getItemDetail();
}


