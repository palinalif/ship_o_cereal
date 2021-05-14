let cereals = {}

function decrement(cerealID) {
    if (cereals[cerealID] > 0) cereals[cerealID]--;
    updateAmount(cerealID);
}

function increment(cerealID) {
    cereals[cerealID]++;
    updateAmount(cerealID);
}

function updateAmount(cerealID) {
    document.getElementById(cerealID + " amount").textContent = cereals[cerealID];
}

function sendToCart(cerealID) {
    let amount = parseInt(document.getElementById(cerealID + " amount").textContent);
    if (amount > 0) {
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url: cartIndex,
            data: {'id': cerealID, 'amount': amount},
            success: function (data) {
                 //this gets called when server returns an OK response
                 $(".alert-success").show();
                 cereals[cerealID] = 0;
                 updateAmount(cerealID);
                 $(".alert-success").delay(1000).fadeOut(500);
            },
            error: function (data) {
                window.location.href = 'user/login';
            }
        });
    }
}

$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search').val();
        $.ajax({
            url: '?searchFilter=' + searchText,
            type: 'GET',
            success: function(resp) {
                if (!availableTags.includes(searchText)){availableTags.push(searchText)}
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal-container">
                        <a class="border-button" href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline; font-weight: bold">${d.price}</p>
                            <button class="button roundbutton" onClick="decrement('${d.id}')">-</button>
                            <p class="cereal-amount" id="${d.id} amount">${cereals[d.id]}</p>
                            <button class="button roundbutton" onClick="increment('${d.id}')">+</button>
                            <button class="button" onClick="sendToCart('${d.id}')"><i class="bi bi-basket"></i></button>
                        </div>
                    </div>`
                });
                $('.catalog-container').html(newHtml.join(''));
                $('#search').val('');

            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});

$(document).ready(function() {
    $('.sortBtn').on('click', function(e) {
        e.preventDefault();
        var searchText = $(this).val();
        $.ajax({
            url: '?sort=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal-container">
                        <a class="border-button" href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline; font-weight: bold">${d.price}</p>
                            <button class="button roundbutton" onClick="decrement('${d.id}')">-</button>
                            <p class="cereal-amount" id="${d.id} amount">${cereals[d.id]}</p>
                            <button class="button roundbutton" onClick="increment('${d.id}')">+</button>
                            <button class="button" onClick="sendToCart('${d.id}')"><i class="bi bi-basket"></i></button>
                        </div>
                    </div>`
                });
                $('.catalog-container').html(newHtml.join(''));
                $('#search').val('');

            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});

$(document).ready(function() {
    $('.filterBtn').on('click', function(e) {
        e.preventDefault();
        var searchText = $(this).val();
        console.log(searchText)
        $.ajax({
            url: '?filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal-container">
                        <a class="border-button" href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline; font-weight: bold">${d.price}</p>
                            <button class="button roundbutton" onClick="decrement('${d.id}')">-</button>
                            <p class="cereal-amount" id="${d.id} amount">${cereals[d.id]}</p>
                            <button class="button roundbutton" onClick="increment('${d.id}')">+</button>
                            <button class="button" onClick="sendToCart('${d.id}')"><i class="bi bi-basket"></i></button>
                        </div>
                    </div>`
                });
                $('.catalog-container').html(newHtml.join(''));
                $('#search').val('');

            },
            error: function(xhr, status, error) {
                console.log(error);
            }
        })
    });
});