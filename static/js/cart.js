function useCard(cardID) {
    $.ajax({
        headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
        url: ".",
        type: 'POST',
        data: {'cardID': cardID},
        success: function(resp) {
            window.location.href = '../review';
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
};

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
                document.getElementById('total-header').innerText = "Total: " + resp['totalPrice'] + "kr.";
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});