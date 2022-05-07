from django.http import HttpResponse

def home(request):
    return HttpResponse("home page")
def contactus(request):
    return HttpResponse("contactus page")
def aboutus(request):
    return HttpResponse("aboutus")