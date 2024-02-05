# from django.http import HttpResponseNotFound
from django.shortcuts import render
from products.models import Product


# Create your views here.
def mainpage(request):
    all_products = Product.objects.order_by('-date')[:3]
    return render(request, 'main/main_page.html', {'all_products': all_products})


# def handle_invalid_path(request, error):
#     return HttpResponseNotFound('page not found')
