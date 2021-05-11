function yesnoCheck() {
    let radioButtonList = document.getElementsByName("card_select");
    for (let item of radioButtonList) {
        if (item.value === "new-card" && item.checked) {
            document.getElementById('register-card').style.display = 'block';
            document.getElementById('buttonFormSubmit').style.display = 'none';
        } else {
            document.getElementById('register-card').style.display = 'none'
            document.getElementById('buttonFormSubmit').style.display = 'block';
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    let radioButtonList = document.getElementsByName("card_select");
    for (let item of radioButtonList) {
        item.setAttribute("onclick","newCardCheck()");
}
    newCardCheck(); //initial check
});

function updateTotal() {
    let total = 0
    for (const [key, value] of Object.entries(prices)) {
        total += value
    }
    document.getElementById("total-header").innerText = "Total: " + total + "kr.";
}

$(document).ready(function() {
    $('.del-button').on('click', function(e) {
        e.preventDefault();
        var productID = $(this).val();
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: removeIndex,
            type: 'POST',
            data: {'id': productID},
            success: function(resp) {
                document.getElementById(productID + "container").remove();
                delete(prices[productID]);
                updateTotal();
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});