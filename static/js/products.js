let index = 0;

function decrement() {
    if (index > 0) index--;
    updateAmount(index);
    checkHowManyExist();
}

function increment() {
    index++;
    updateAmount(index);
    checkHowManyExist();
}

function updateAmount(index) {
    document.getElementById("amount").textContent = index;
}