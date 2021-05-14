function printReceipt() {
    let cartItems = JSON.parse(document.getElementById('cart-items').textContent);
    let userInfo = JSON.parse(document.getElementById('user-info').textContent);
    let txtString = "Order ID: " + cartItems[0]['order_id'] + "\n" + "Name: " + userInfo['name'] + "\n\n";
    for (let i = 0; i < cartItems.length; i++) {
        txtString += i+1 + ". " + cartItems[i]['product']['name'] + "\nQuantity: " + cartItems[i]['quantity'] +
            "\nPrice:" + cartItems[i]['product']['price'] + "\n\n";
    }
    txtString += "Total: " + totalAmount;
    return txtString;
}

var textFile = null,
  makeTextFile = function (text) {
    var data = new Blob([text], {type: 'text/plain'});

    // If we are replacing a previously generated file we need to
    // manually revoke the object URL to avoid memory leaks.
    if (textFile !== null) {
      window.URL.revokeObjectURL(textFile);
    }

    textFile = window.URL.createObjectURL(data);

    return textFile;
  };


  var create = document.getElementById('receipt-button');

  create.addEventListener('click', function () {
    var link = document.createElement('a');
    link.setAttribute('download', 'receipt.txt');
    link.href = makeTextFile(printReceipt());
    document.body.appendChild(link);

    // wait for the link to be added to the document
    window.requestAnimationFrame(function () {
      var event = new MouseEvent('click');
      link.dispatchEvent(event);
      document.body.removeChild(link);
		});

  }, false);