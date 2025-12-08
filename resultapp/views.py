from django.shortcuts import render

# Create your views here.
def index(request):
    """
    index.html page created in template is called
    home page kholna ko lagi
    """
    return render(request,'index.html') 