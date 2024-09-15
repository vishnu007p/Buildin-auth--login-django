from django.shortcuts import render, redirect
from .models import ImageUpload
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload_view(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image=request.method.POST('image')
        ImageUpload.objects.create(user=request.user, image=image)
        return redirect('gallery_view')
    return render(request,'upload.html')

@login_required
def gallery_view(request):
    