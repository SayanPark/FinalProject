from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductCategory, ProductTag, ProductColor, ProductStyle


# Create your views here.
def list_of_products(request):
    all_products = Product.objects.order_by('-date')
    return render(request, 'products/product_list.html', {'all_products': all_products})


def details_of_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_by_category(request, category_slug):
    category = ProductCategory.objects.get(url_title=category_slug)
    products = category.product_set.order_by('-date')
    return render(request, 'products/products_by_category.html', {'products': products, 'category': category})


def product_detail_in_category(request, product_slug, category_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_by_tag(request, tag_slug):
    tag = ProductTag.objects.get(tag=tag_slug)
    products = tag.product_set.order_by('-date')
    return render(request, 'products/products_by_tag.html', {'products': products, 'tag': tag})


def product_detail_in_tag(request, product_slug, tag_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_by_color(request, color_slug):
    color = ProductColor.objects.get(color=color_slug)
    products = color.product_set.order_by('-date')
    return render(request, 'products/products_by_color.html', {'products': products, 'color': color})


def product_detail_in_color(request, product_slug, color_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_by_style(request, style_slug):
    style = ProductStyle.objects.get(style=style_slug)
    products = style.product_set.order_by('-date')
    return render(request, 'products/products_by_style.html', {'products': products, 'style': style})


def product_detail_in_style(request, product_slug, style_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_bracelet(request):
    category = ProductCategory.objects.get(url_title='bracelet')
    products = category.product_set.order_by('-date')
    return render(request, 'products/products_by_category.html', {'products': products, 'category': category})


def product_detail_in_bracelet(request, product_slug, category_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_necklace(request):
    category = ProductCategory.objects.get(url_title='necklace')
    products = category.product_set.order_by('-date')
    return render(request, 'products/products_by_category.html', {'products': products, 'category': category})


def product_detail_in_necklace(request, product_slug, category_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_decorative_hangings(request):
    category = ProductCategory.objects.get(url_title='decorative-hangings')
    products = category.product_set.order_by('-date')
    return render(request, 'products/products_by_category.html', {'products': products, 'category': category})


def product_detail_in_decorative_hangings(request, product_slug, category_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def products_keychain(request):
    category = ProductCategory.objects.get(url_title='keychain')
    products = category.product_set.order_by('-date')
    return render(request, 'products/products_by_category.html', {'products': products, 'category': category})


def product_detail_in_keychain(request, product_slug, category_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def add_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = request.session.get('wishlist', [])
    if product_id not in wishlist:
        wishlist.append(product_id)
    request.session['wishlist'] = wishlist
    return redirect('product', slug=product.slug)


def remove_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist = request.session.get('wishlist', [])
    if product_id in wishlist:
        wishlist.remove(product_id)
    request.session['wishlist'] = wishlist
    return redirect('wishlist')


def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    products = Product.objects.filter(id__in=wishlist)
    return render(request, 'products/wishlist.html', {'products': products})


def product_detail_in_wishlist(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})


def search_product(request):
    search_query = request.GET.get('search', '')
    results = Product.objects.filter(title__icontains=search_query)
    return render(request, 'products/search.html', {'results': results, 'search_query': search_query})


def product_detail_in_search(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'products/product_details.html', {'product': product})
