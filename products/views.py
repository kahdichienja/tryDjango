from django.shortcuts import render

from .models import Product
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