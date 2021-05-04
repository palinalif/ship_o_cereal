from django.shortcuts import render

# Create your views here.
cereals = [
    {'name': 'Cheerios',
     'price': 700,
     'image': 'https://images-na.ssl-images-amazon.com/images/I/81VQIHQ0-CL._SL1500_.jpg'},

    {'name': 'Honey Nut Cheerios',
     'price': 800,
     'image': 'https://d3d71ba2asa5oz.cloudfront.net/12026801/images/honeynutcheeriosce_e780e_generalmills_alwaysfre_128__1.jpg'},

    {'name': 'Cocoa Puffs',
     'price': 850,
     'image': 'https://i5.walmartimages.com/asr/e78f3d25-baed-4d09-bb70-ea2ea8e3f594.93489774c0a84ad9c0170cb59ef27bc0.jpeg'},
]

def index(request):
    return render(request, 'description/index.html')