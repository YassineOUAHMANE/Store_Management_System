var productModal = $("#productModal");
$(function () {
    // JSON data by API call
    $.get(productListApiUrl, function (response) {
        if(response) {
            var table = '';
            $.each(response, function(index, product) {
                table += '<tr data-id="'+ product.product_id +'" data-name="'+ product.name +'" data-unit="'+ product.uom_id +'" data-price="'+ product.price_per_unit +'">' +
                    '<td class="editable-name">'+ product.name +'</td>'+
                    '<td class="editable-unit">'+ product.uom_name +'</td>'+
                    '<td class="editable-price">'+ product.price_per_unit +'</td>'+
                    '<td><button class="edit btn btn-primary">Edit</button></td>'+
                    '<td><span class="btn btn-xs btn-danger delete-product">Delete</span></td>'+
                    '</tr>';
            });
            $("table").find('tbody').empty().html(table);
        }
    });

    // Handle the "Edit" button click
    $(document).on('click', '.edit', function () {
        var tr = $(this).closest('tr');
        var isEditable = tr.find('.editable-name').attr('contenteditable') === "true";

        if (!isEditable) {
            // Enable editing
            tr.find('.editable-name, .editable-unit, .editable-price').attr('contenteditable', 'true').addClass('editable-highlight');
            $(this).text('Save');
        } else {
            // Disable editing and save changes
            tr.find('.editable-name, .editable-unit, .editable-price').attr('contenteditable', 'false').removeClass('editable-highlight');
            $(this).text('Edit');

            // Get updated values
            var productId = tr.data('id');
            var newName = tr.find('.editable-name').text();
            var newUnit = tr.find('.editable-unit').text();
            var newPrice = tr.find('.editable-price').text();

            // Save the updated values to the database
            callApi("POST", producteditnameApiUrl, {product_id: productId, name: newName});
            callApi("POST", producteditunitApiUrl, {product_id: productId, uom: newUnit});
            callApi("POST", producteditpriceApiUrl, {product_id: productId, price: newPrice});
        }
    });
});


    // Save Product
    $("#saveProduct").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#productForm").serializeArray();
        var requestPayload = {
            product_name: null,
            uom_id: null,
            price_per_unit: null
        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'name':
                    requestPayload.product_name = element.value;
                    break;
                case 'uoms':
                    requestPayload.uom_id = element.value;
                    break;
                case 'price':
                    requestPayload.price_per_unit = element.value;
                    break;
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });

    $(document).on("click", ".delete-product", function (){
        var tr = $(this).closest('tr');
        var data = {
            product_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", productDeleteApiUrl, data);
        }
    });


    $(document).on("click", ".edit", function () {
        var tr = $(this).closest('tr');
        var productId = tr.data('id');
        
        // Populate the modal with the existing data
        $('#editProductId').val(productId);
        $('#editProductName').val(tr.find('td:eq(0)').text());
        $('#editProductUnit').val(tr.find('td:eq(1)').text());
        $('#editProductPrice').val(tr.find('td:eq(2)').text());
    
        // Show the modal
        $('#editModal').modal('show');
    });
    
    $('#saveChanges').on('click', function() {
        var productId = $('#editProductId').val();
        var data = {
            product_id: productId,
            name: $('#editProductName').val(),
            unit: $('#editProductUnit').val(),
            price: $('#editProductPrice').val()
        };
    
        // Update product name
        callApi("POST", producteditnameApiUrl, {product_id: data.product_id, name: data.name});
    
        // Update product unit
        callApi("POST", producteditunitApiUrl, {product_id: data.product_id, uom: data.unit});
    
        // Update product price
        callApi("POST", producteditpriceApiUrl, {product_id: data.product_id, price: data.price});
    
        // Close the modal
        $('#editModal').modal('hide');
    });
    
    $('#editModal').on('show.bs.modal', function(){
        // Fetch UOM options when the modal is shown
        $.get(uomListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.uom_id +'">'+ uom.uom_name +'</option>';
                });
                $("#editProductUnit").empty().html(options);
            }
        });
    });
    
    

    productModal.on('hide.bs.modal', function(){
        $("#id").val('0');
        $("#name, #unit, #price").val('');
        productModal.find('.modal-title').text('Add New Product');
    });

    productModal.on('show.bs.modal', function(){
        //JSON data by API call
        $.get(uomListApiUrl, function (response) {
            if(response) {
                var options = '<option value="">--Select--</option>';
                $.each(response, function(index, uom) {
                    options += '<option value="'+ uom.uom_id +'">'+ uom.uom_name +'</option>';
                });
                $("#uoms").empty().html(options);
            }
        });
    });