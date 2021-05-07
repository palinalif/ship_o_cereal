from django.shortcuts import render
from django.http import JsonResponse

from products.views import getCereals, getSortedBy, getFilterBy

# Create your views here.
def index(request):
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        cereals = [{
            'id': c.id,
            'name': c.name,
            'price': c.price,
            'image': c.productimage_set.first().image
        } for c in getCereals().filter(name__icontains = searchFilter)]
        return JsonResponse({'data': cereals})
    elif 'sort' in request.GET:
        return "sort"
    elif 'filter' in request.GET:
        filter = request.GET['filter']
        print(filter)
        if filter == 'healthy':
            print(getCereals().filter(tag_id=1))
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().filter(tag_id=1)]
        else:
            print(getCereals().filter(tag_id=2))
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().filter(tag_id=2)]

        return JsonResponse({'data': cereals})
    return render(request, 'catalog/index.html', context=({'cereals': getCereals()}))

def sortedBy(request, att):
    return render(request, 'catalog/index.html', context=({'cereals': getSortedBy(att)}))

def filterBy(request, label):
    return render(request, 'catalog/index.html', context=({'cereals': getFilterBy(label)}))
