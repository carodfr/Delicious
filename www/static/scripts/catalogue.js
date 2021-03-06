//retrieve the from the session storage, save the new item and store it again
function addProduct(productID){
    var cart = JSON.parse(sessionStorage.getItem('cart')) || {};
    if(productID in cart)cart[productID]++;
    else cart[productID]=1
    sessionStorage.setItem('cart',JSON.stringify(cart))
}

//insert the cart to the checkout form and submit it
function checkout(){
    if(sessionStorage.getItem('cart')===null){
        //$('<div class="alert alert-danger mb-0" role="alert">No products were selected</div>').appendTo("#msgContainer");
        alert("The cart is empty!")
        return;
    }
    $("#cart").val(sessionStorage.getItem('cart'));
    $("#catalogueForm").submit();
}
