from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello World</h1>")
    context = {

    }
    return render(request, "home.html", context)


def contact_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    context = {
        "my_text": "This is exmple context",
        "my_number": 1234,
        "my_list": [123, 2323, 444]
    }
    return render(request, "about.html", context)

