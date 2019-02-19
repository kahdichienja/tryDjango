from django.shortcuts import render

from .models import Product

from .forms import Contanct_form
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=1)
    context = {
        'title' : obj.title,
        'price' : obj.price,
        'summary' : obj.summary,
        'description' : obj.description
    }
    return render(request, "product/detail.html", context)


def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Contanct_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contanct_form()

    return render(request, 'forms/forms.html', {'form': form})