let cereals = {}

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

function sendToCart(cerealName) {
    $.ajax({
        method: 'POST',
        url: "{ % url 'cart-index' % }",
        data: {'name': cerealName, 'amount': document.getElementById(cerealName + " amount").textContent},
        success: function (data) {
             //this gets called when server returns an OK response
             alert("it worked!");
             updateAmount(cerealName);
        },
        error: function (data) {
             alert("it didnt work\n" + data);
        }
    });
}

$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search').val();
        $.ajax({
            url: '?searchFilter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal-container">
                        <a class="border-button" href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline">${d.price}</p>
                            <button class="button roundbutton" onClick="decrement(${d.name})">-</button>
                            <p id="${d.name} amount">${cereals[d.name]}</p>
                            <button class="button roundbutton" onClick="increment(${d.name})">+</button>
                            <button class="button" onClick="sendToCart(${d.name})">Cart</button>
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
        console.log(searchText)
        $.ajax({
            url: '?sort=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="cereal-container">
                        <a href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline">${d.price}</p>
                            <button onClick="decrement(${d.name})">-</button>
                            <p className="cereal-amount" id="${d.name} amount">${cereals[d.name]}</p>
                            <button onClick="increment(${d.name})">+</button>
                            <button onClick="sendToCart(${d.name})">Cart</button>
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
                        <a href="/products/${d.id}">
                            <img src="${d.image}" class="cereal-img"/>
                        </a>
                        <h3>${d.name}</h3>
                        <div>
                            <p style="display: inline">${d.price}</p>
                            <button onClick="decrement(${d.name})">-</button>
                            <p className="cereal-amount" id="${d.name} amount">${cereals[d.name]}</p>
                            <button onClick="increment(${d.name})">+</button>
                            <button onClick="sendToCart(${d.name})">Cart</button>
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