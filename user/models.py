from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    country = CountryField()
    city = models.CharField(max_length=255)
    houseNumber = models.IntegerField()
    streetName = models.CharField(max_length=255)
    postNumber = models.IntegerField()

    def __str__(self):
        return str(self.country)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    photo = models.CharField(max_length=999)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class PaymentInfo(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    cardHolder = models.CharField(max_length=255)
    cardNumber = models.IntegerField()
    expDate = models.IntegerField()
    cvc = models.IntegerField()

class SearchHistory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add= True, blank= True)

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length = 255)
    dateCreated = models.DateTimeField(auto_now_add = True)

def profile1(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)})

def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            address_instance = Address()
            address_instance.country = request.POST['country']
            address_instance.city = request.POST['city']
            address_instance.houseNumber = request.POST['houseNumber']
            address_instance.streetName = request.POST['streetName']
            address_instance.postNumber = request.POST['postNumber']
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    if profile is None:
        return render(request, 'user/profile.html', {
            'form': ProfileForm(instance=profile)})
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile, initial={
            'country': request.user.profile.address.country,
            'city': request.user.profile.address.city,
            'houseNumber': request.user.profile.address.houseNumber,
            'streetName': request.user.profile.address.streetName,
            'postNumber': request.user.profile.address.postNumber
        })
    })