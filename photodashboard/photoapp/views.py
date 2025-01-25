from django.shortcuts import render
from .models import Event  # Make sure to import your Event model

def home(request):
    return render(request, 'home.html')

def search(request):
    return render(request, 'search.html')  # This view renders the search options page

def search_results(request):
    event_name = request.GET.get('event_name')
    location = request.GET.get('location')
    date = request.GET.get('date')
    categories = request.GET.getlist('category')  # Get selected categories as a list

    # Implement your filtering logic here using the above variables
    queryset = Event.objects.all()  # Start with all events

    if event_name:
        queryset = queryset.filter(name__icontains=event_name)  # Adjust field name as necessary
    if location:
        queryset = queryset.filter(location__icontains=location)  # Adjust field name as necessary
    if date:
        queryset = queryset.filter(date=date)  # Adjust field name as necessary
    if categories:
        queryset = queryset.filter(category__in=categories)  # Adjust field name as necessary

    return render(request, 'search_results.html', {'results': queryset})  # Pass filtered results to template
