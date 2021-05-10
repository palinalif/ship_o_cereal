from django import forms
from django.utils.safestring import mark_safe

#TODO: Replace with database connection
user_info = {
    'id': 1,
    'name': 'Test user',
    'email': 'user@testuser.com',
    'phone': '123-4567',
    'password': 'dfjajfauwr89428934d',
    'streetName': 'Eitthvaðstræti',
    'houseNumber': '69',
    'city': 'Reykjavík',
    'country': 'Iceland',
    'postalCode': 109
}

#and let's say that these are their cards
cards = [
    {
        'userId':1,
        'cardHolderName':'Test user',
        'cardNumber':377337278995056,
        'expDate':"0122",
        'cvc':123
    },
    {
        'userId':1,
        'cardHolderName':'Test user',
        'cardNumber':342935602344123,
        'expDate':"1125",
        'cvc':456
    }
]

class PayForm(forms.Form):
    CHOICES = []
    counter = 1
    for card in cards:
        print(card)
        CHOICES.append((f'card{counter}', mark_safe(f'<div class = "card-set"><p>Card ending with:</p><p>******** {str(card["cardNumber"])[-4:]}<p></div><div class = "card-set"><p>Expiry date:</p><p>{card["expDate"][:2]}/{card["expDate"][-2:]}</p></div>')))
        counter += 1
    CHOICES.append(('new-card', 'New Card...'))
    card_select = forms.CharField(label='Choose a card...', widget=forms.RadioSelect(choices=CHOICES))

class NewCardForm(forms.Form):
    card_number = forms.CharField(label='Card Number:', max_length=100)
    MONTH_CHOICES = [('01','January'),
                     ('02','February'),
                     ('03','March'),
                     ('04','April'),
                     ('05','May'),
                     ('06','June'),
                     ('07','July'),
                     ('08','August'),
                     ('09','September'),
                     ('10','October'),
                     ('11','November'),
                     ('12','December')]
    YEAR_CHOICES = [('21','21'),
                    ('22','22'),
                    ('23','23'),
                    ('24','24'),
                    ('25','25')
    ]
    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    cvv = forms.CharField(label='CVV:', max_length=3)
    holder_name = forms.CharField(label='Card Holder Name:', max_length=100)
    save_card = forms.BooleanField()