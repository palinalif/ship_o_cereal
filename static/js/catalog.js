let cereals = {}

function decrement(cerealName) {
    if (cereals[cerealName] > 0) cereals[cerealName]--;
    updateAmount(cerealName);
}

function increment(cerealName) {
    cereals[cerealName]++;
    updateAmount(cerealName);
}

function updateAmount(cerealName) {
    document.getElementById(cerealName + " amount").textContent = cereals[cerealName];
}

function sendToCart(cerealName) {
    $.ajax({
        method: 'POST',
        url: "{ % url 'cart-index' % }",
        data: {'name': cerealName, 'amount': document.getElementById(cerealName + " amount").textContent},
        success: function (data) {
             //this gets called when server returns an OK response
             alert("it worked!");
             updateAmount(cerealName);
        },
        error: function (data) {
             alert("it didnt work\n" + data);
        }
    });
}