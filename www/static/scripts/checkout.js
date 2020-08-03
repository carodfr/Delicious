//insert the cart to the checkout form and submit it
function placeOrder(){
    if(sessionStorage.getItem('cart')===null){
        //$('<div class="alert alert-danger mb-0" role="alert">No products were selected</div>').appendTo("#msgContainer");
        alert("The cart is empty!")
        return;
    }
    $("#cart").val(sessionStorage.getItem('cart'));
    sessionStorage.removeItem('cart')
    $("#checkoutForm").submit();
}
