

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('query', '')
   
    context = {
        'query': query,
    }
    return render(request, 'search_results.html', context)  
