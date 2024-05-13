// ========= cart object =====================  

if(localStorage.getItem('cart')==null) {
    var cart= {};
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
}

// =================== add to cart button ================

$(document).on('click','.atc', function() {
    var item_id = this.id.toString();

    if(cart[item_id]!=undefined) {
        quantity = cart[item_id][0] + 1;
        cart[item_id][0] = quantity;
        cart[item_id][2] += parseFloat(document.getElementById("pp"+item_id).innerHTML);
    }
    else {
        quantity = 1;
        Name = document.getElementById("pt"+item_id).innerHTML;
        Price = parseFloat(document.getElementById("pp"+item_id).innerHTML);
        Image = document.getElementById("pi"+item_id).src;
        cart[item_id] = [quantity,Name,Price,Image];
    }
    localStorage.setItem('cart',JSON.stringify(cart));
    
    // ==== snackbar =======
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
});

// ======================== navbar's cart popover string =====================

DisplayCart(cart);

function DisplayCart(cart) {
    var cartString = '';
    cartString += '<h5>This is your cart:</h5>';
    var cartIndex = 1;
    for (var x in cart) {
        cartString += cartIndex + " Name : " + cart[x][1] +  " : Qty : " + cart[x][0] + "<br>";
        cartIndex +=1;
    }
    cartString += '<a href="/checkout/" class="btn btn-warning mt-2">Checkout</a>';
 
    $(function () {
        $('[data-bs-toggle="popover"]').popover(
            document.getElementById('cart').setAttribute('data-bs-content', cartString)
        );
    });
};

// =============== checkout page =================
var total = 0;
var sr_no = 1;
for (item in cart) {
    let qty = cart[item][0];
    let name = cart[item][1];
    let price = cart[item][2];
    let image = cart[item][3];
    total += price; 
    checkout_list = `<tr id="${sr_no}">
                        <th scope="row" style="line-height: 40px;background-color: transparent;">${sr_no}</th>
                        <th><img src="${image}" width="50px" /></th>
                        <td  style="color: var(--color);">${name}</td>
                        <td  style="line-height: 40px;">${qty}</td>
                        <td class="text-success"  style="line-height: 40px;">&#x20B9;${price}</td>
                        <td class="trci" onclick="removeCartItem(item)"><i class="fa-solid fa-xmark rci"  style="line-height: 40px;color: var(--color);"></i></button></td>
                    </tr>`;
    sr_no +=1;
    $('#checkout').append(checkout_list); 
    $('#total').val(total);
}
let total_price =`<tr>
                    <td style="background-color: #cfbee626;"></td>
                    <th scope="row" colspan=1 style="background-color: #cfbee626;color: var(--color);">Total</th>
                    <td style="background-color: #cfbee626;"></td>
                    <td style="background-color: #cfbee626;"></td>
                    <td class="text-success" style="background-color: #cfbee626;"><b>&#x20B9;${total}</b></td>
                    <td style="background-color: #cfbee626;"></td>
                  </tr>`;
$('#checkout_table').append(total_price); 

// ============== Remove Cart Item =====================

function removeCartItem(item) {
    let d = JSON.parse(localStorage.getItem('cart'));

    if (d && d[item]) {
        delete d[item];
        localStorage.setItem('cart', JSON.stringify(d));
    }
    location.reload();
}
console.log("ok")