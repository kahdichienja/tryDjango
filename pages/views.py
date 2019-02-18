from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Home view</h1>")
    return render(request, "home.html", {})
    
def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Home view</h1>")
    my_context = {
        "my_text": "this is contact context",
        "my_number": 123,
        "my_list": [123, 345, 12344, 6577]
    }
    return render(request, "contact.html", my_context )    