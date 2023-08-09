from django.shortcuts import render

# Show poplular destinations and when user clicks on the popular Locations call get_spaces
# Will have a search feature when user can enter destination name

def index(request):
    return render(request, "index.html")

# Accepts a location name and if the location name matches DB then show spaces present in location
# User can filter the type of spaces as per all the boolean fields and add a new space
# If location returns zero spaces, ask the user to add as primary action

def get_spaces(request, location):
    location = location.lower()
    return render(request, "spaces.html", {"location":location})