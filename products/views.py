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

    {'name': 'Lucky Charms',
     'price': 900,
     'image': 'https://i5.walmartimages.com/asr/66e3fc3d-32ef-41b4-9aa3-2852b3c17f19_1.f19a53b164c8a56d749fb11670983422.jpeg'},

    {'name': 'Havre Fras',
     'price': 750,
     'image': 'https://cdn.shopify.com/s/files/1/1518/6272/products/To-1.01_Flingorhavrefrasoriginal_1024x1024.jpg?v=1520345667'},

    {'name': 'Cinnamon Toast Crunch',
     'price': 800,
     'image': 'https://www.usa-drinks.de/media/image/product/12475/lg/cinnamon-toast-crunch-1-x-340g.jpg'},

    {'name': 'Trix',
     'price': 850,
     'image': 'https://i5.walmartimages.com/asr/20011f44-8b7e-4750-a37a-236fbba4e54c_1.9b22a7ddf3a4198b5e8f2a7cc7836557.jpeg'},

    {'name': 'Fruit Loops',
     'price': 800,
     'image': 'https://www.frajosfood.com/img/p/3/7/0/0/8/37008-thickbox_default.jpg'},

    {'name': 'Rice Krispies',
     'price': 650,
     'image': 'https://images-na.ssl-images-amazon.com/images/I/91EbJNh%2BkuL._SL1500_.jpg'},
]

def getCereals():
    return cereals

def product(request, id):
    # TODO: make id check and if invalid goto 404 page
    return render(request, 'products/index.html', context=({'cereal': cereals[id]}))