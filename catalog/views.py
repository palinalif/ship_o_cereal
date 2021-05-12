from django.shortcuts import render
from django.http import JsonResponse

from products.views import getCereals
from user.models import Profile, SearchHistory

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        searchHistory = SearchHistory.objects.filter(profile=profile)
    if 'searchFilter' in request.GET:
        searchFilter = request.GET['searchFilter']
        cereals = [{
            'id': c.id,
            'name': c.name,
            'price': c.price,
            'image': c.productimage_set.first().image
        } for c in getCereals().filter(name__icontains = searchFilter)]
        if request.user.is_authenticated and searchFilter is not "" and searchHistory.filter(query=searchFilter).first() is None:
            new_query = SearchHistory()
            new_query.profile = profile
            new_query.query = searchFilter
            new_query.save()
        return JsonResponse({'data': cereals})
    elif 'sort' in request.GET:
        sort = request.GET['sort']
        if sort == 'name':
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().order_by('name')]
        else:
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().order_by('price')]
        return JsonResponse({'data': cereals})
    elif 'filter' in request.GET:
        filter = request.GET['filter']
        if filter == 'healthy':
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().filter(tag_id=1)]
        else:
            cereals = [{
                'id': c.id,
                'name': c.name,
                'price': c.price,
                'image': c.productimage_set.first().image
            } for c in getCereals().filter(tag_id=2)]

        return JsonResponse({'data': cereals})
    if request.user.is_authenticated:
        return render(request, 'catalog/index.html', context=({'cereals': getCereals(), 'searchHistory': searchHistory}))
    return render(request, 'catalog/index.html', context=({'cereals': getCereals()}))