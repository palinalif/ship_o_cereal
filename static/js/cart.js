// function newCardCheck(cardID) {
//     if (cardID > 0) {
//         currentCard = cardID
//         document.getElementById('register-card').style.display = 'none';
//         document.getElementById('use-card').style.display = 'block';
//     }
//     for (let item of radioButtonList) {
//         if (item.value === "new-card" && item.checked) {
//             document.getElementById('register-card').style.display = 'block';
//             document.getElementById('buttonFormSubmit').style.display = 'none';
//         } else {
//             document.getElementById('register-card').style.display = 'none'
//             document.getElementById('buttonFormSubmit').style.display = 'block';
//         }
//     }
// }

function useCard(cardID) {
    console.log(cardID)
    $.ajax({
        headers: {'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value},
        url: ".",
        type: 'POST',
        data: {'cardID': cardID},
        success: function(resp) {
            console.log("yeet");
            window.location.href = reviewSite;
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
};

// document.addEventListener('DOMContentLoaded', function() {
//     let radioButtonList = document.getElementsByName("card_select");
//     for (let item of radioButtonList) {
//         item.setAttribute("onclick","newCardCheck()");
// }
//     newCardCheck(); //initial check
// });

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