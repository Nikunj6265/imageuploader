from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Image
#from django.urls import reverse
# Create your views here.
def home(request):
    if request.method=="POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
         form.save()
         #return redirect(reverse('my_app:thank_you'))
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img':img,'form':form})


def thank_you(request):
   return render(request,'myapp/thank_you.html')