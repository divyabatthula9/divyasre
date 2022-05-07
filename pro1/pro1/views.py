from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("about us page")
def contactus(request): 
    return HttpResponse("contact us") 
def course(request):
    return HttpResponse("course") 