from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def blog(request):
    return render(request, 'blog.html')

def package(request):
    return render(request, 'package.html')

def testimonial(request):
    return render(request, 'testimonial.html')

