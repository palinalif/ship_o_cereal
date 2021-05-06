function yesnoCheck() {
        if (document.getElementById('new-card').checked) {
            document.getElementById('register-card').style.display = 'block';
        }
        else document.getElementById('register-card').style.display = 'none';

    }
function testingSubmit() {
    console.log("Hello?");
    if (document.getElementById('new-card').checked) {
        // The user is using a new card
        if (document.getElementById('save-card').checked) {
            //save the new card
            //TODO: Save card info
        }
    }

}