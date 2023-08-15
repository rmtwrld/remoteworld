from django.shortcuts import render, redirect
from .models import Space, Location
from .forms import AddSpaceForm

# Show poplular destinations and when user clicks on the popular Locations call get_spaces
# Will have a search feature when user can enter destination name

def index(request):
    destination = request.GET.get('destination')
    if destination != None:
        destination = destination.capitalize()
        spaces = Space.objects.filter(location__location_name__contains=destination)
        form =  AddSpaceForm()
        return render(request, "spaces.html", {"destination":destination, "spaces":spaces, "form":form})
    return render(request, "index.html")

def add_space(request):
    form = AddSpaceForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request,"space-submission.html")
    return redirect('index')

def contribute(request):
    return render(request, "contribute.html")