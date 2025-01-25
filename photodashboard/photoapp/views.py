
import base64
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import EventPhoto

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('query', '')
   
    context = {
        'query': query,
    }
    return render(request, 'search_results.html', context) 

def upload_file(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        
        # Handle multiple file uploads
        files = request.FILES.getlist('file')
        
        try:
            for uploaded_file in files:
                # Read the file as binary
                photo_data = uploaded_file.read()  # Read file content
                
                # Create an instance of EventPhoto and save it to the database
                EventPhoto.objects.create(event_name=event_name, photo=photo_data)  # Save binary data
            
            return JsonResponse({'success': True})  # Return success response

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})  # Return error response

    return render(request, 'upload.html')  # Render the upload page if not a POST request


def search_results(request):
    query = request.GET.get('query', '')
    results = EventPhoto.objects.filter(event_name__icontains=query)  # Filter based on event name
    
    # Prepare results for rendering
    for result in results:
        result.photo_display = base64.b64encode(result.photo).decode('utf-8')  # Encode binary data to base64 for display
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

