cereals = {}

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