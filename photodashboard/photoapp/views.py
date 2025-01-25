

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'home.html')

def search(request):
    query = request.GET.get('query', '')
   
    context = {
        'query': query,
    }
    return render(request, 'search_results.html', context) 
 
def search(request):
    return render(request, 'search.html')


def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        
        # Save the file to the media directory
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

        return HttpResponseRedirect('/success/')  # Redirect to a success page or another view

    return render(request, 'upload.html')  # Render the upload page if not a POST request
