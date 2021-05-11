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
                console.log($(this).parent());
                $(this).parent().remove();
            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});