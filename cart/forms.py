from django import forms
from django.utils.safestring import mark_safe
from user.models import Profile, Address, PaymentInfo


def construct_card_dict(request):
    profile = Profile.objects.filter(user=request.user).first()
    cardQueries = PaymentInfo.objects.filter(profile=profile)
    cards = []
    for card in cardQueries:
        c = {
            'cardHolderName': card.cardHolder,
            'cardNumber': card.cardNumber,
            'expDate': card.expDate,
            'cvc': card.cvc
        }
        cards.append(c)
    return cards


class PayForm(forms.Form):
    # https://stackoverflow.com/questions/8841502/how-to-use-the-request-in-a-modelform-in-django
    # TODO: Get this working, pls help
    def __init__(self, request, *args, **kwargs):
        super(PayForm, self).__init__(*args, **kwargs)
        self.cards = construct_card_dict(request)
        CHOICES = []
        counter = 1
        for card in self.cards:
            CHOICES.append((f'card{counter}', mark_safe(
                f'<div class = "card-set"><p>Card ending with:</p><p>******** {str(card["cardNumber"])[-4:]}<p></div><div class = "card-set"><p>Expiry date:</p><p>{card["expDate"][:2]}/{card["expDate"][-2:]}</p></div>')))
            counter += 1
        CHOICES.append(('new-card', 'New Card...'))
        self.fields['card_select'] = forms.CharField(label='Choose a card...', widget=forms.RadioSelect(choices=CHOICES))


class NewCardForm(forms.Form):
    card_number = forms.CharField(label='Card Number:', max_length=100)
    MONTH_CHOICES = [('01', 'January'),
                     ('02', 'February'),
                     ('03', 'March'),
                     ('04', 'April'),
                     ('05', 'May'),
                     ('06', 'June'),
                     ('07', 'July'),
                     ('08', 'August'),
                     ('09', 'September'),
                     ('10', 'October'),
                     ('11', 'November'),
                     ('12', 'December')]
    YEAR_CHOICES = [('21', '21'),
                    ('22', '22'),
                    ('23', '23'),
                    ('24', '24'),
                    ('25', '25')
                    ]
    month = forms.ChoiceField(choices=MONTH_CHOICES)
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    cvv = forms.CharField(label='CVV:', max_length=3)
    holder_name = forms.CharField(label='Card Holder Name:', max_length=100)
    save_card = forms.BooleanField(required=False)
