function yesnoCheck() {
    let radioButtonList = document.getElementsByName("card_select");
    for (let item of radioButtonList) {
        if (item.value === "new-card" && item.checked) {
            document.getElementById('register-card').style.display = 'block';
        } else {
            document.getElementById('register-card').style.display = 'none'
        }
    }
}
function testingSubmit() {
    if (document.getElementById('new-card').checked) {
        // The user is using a new card
        if (document.getElementById('save-card').checked) {
            //save the new card
            //TODO: Save card info
        }
    }

}

document.addEventListener('DOMContentLoaded', function() {
    let radioButtonList = document.getElementsByName("card_select");
    for (let item of radioButtonList) {
        item.setAttribute("onclick","yesnoCheck()")
}
});