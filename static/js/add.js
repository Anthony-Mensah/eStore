
  $(document).ready(function(){
    $(document).on('click', '.cart-button', function(e){
      let prodid = $(this).data('index')
      $.ajax({
      type: "POST",
      url: url,
      data: {
        productid:prodid,
        csrfmiddlewaretoken: csrf_token,
        action: "post",
      },
      success: function (response) {
        $('#cart-items').html(response.total_items)
      },
      error: function (xhr, errmsg, err) {
        alert("error")
      },
    });
    })
  })
