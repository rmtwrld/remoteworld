from django.shortcuts import render
from .models import Space, Location

# Show poplular destinations and when user clicks on the popular Locations call get_spaces
# Will have a search feature when user can enter destination name

def index(request):
    destination = request.GET.get('destination')
    if destination != None:
        destination = destination.capitalize()
        spaces = Space.objects.filter(location__location_name__contains=destination)
        return render(request, "spaces.html", {"destination":destination, "spaces":spaces})
    return render(request, "index.html")

# Accepts a location name and if the location name matches DB then show spaces present in location
# User can filter the type of spaces as per all the boolean fields and add a new space
# If location returns zero spaces, ask the user to add as primary action
    