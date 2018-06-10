$(document).ready(function(){
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var numb = $('#number').val();
        console.log(numb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        var product_image = submit_btn.data("name");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        var data = {};
        data.product_id = product_id;
        data.numb = numb;

        var carf_token = $('#form_buying_product [name = "csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = carf_token;

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_numb)
                if (data.products_total_numb){
                    $('#basket_total_number').text("(" + data.products_total_numb + ")")
                }
            },
            error: function() {
                console.log("ERROR");
            }
        })


        $('.basket-items ul').append('<li>'+ product_name + ', ' + numb
            + ' itm. for ' + product_price + ' €  ' + '<a href="" class="delete-item">' +  'X'  + '</a>' + '</li>');
    })

    function shownigBasket() {
        $('.basket-items').removeClass('hidden');
    }

    $('.basket-container').on('click', function(e){
        e.preventDefault();
        shownigBasket();
    })

    $('.basket-container').mouseover(function(){
        shownigBasket();
    })


    // $('.basket-container').mouseout(function(){
    //     shownigBasket();
    // })

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        $(this).closest('li').remove();
    })

})