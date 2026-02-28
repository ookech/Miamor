from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.hmtl')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, '404.html')
