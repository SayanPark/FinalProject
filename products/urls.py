from django.urls import path
from . import views


urlpatterns = [
    path('all-products', views.list_of_products, name='all_products'),
    path('products/category/<str:category_slug>/', views.products_by_category, name='products_by_category'),
    path('products/tag/<str:tag_slug>/', views.products_by_tag, name='products_by_tag'),
    path('products/color/<str:color_slug>/', views.products_by_color, name='products_by_color'),
    path('products/style/<str:style_slug>/', views.products_by_style, name='products_by_style'),
    path('<slug:slug>', views.details_of_product, name='product'),
    path('products/category/<str:category_slug>/<slug:product_slug>', views.product_detail_in_category, name='product_detail_in_category'),
    path('products/category/bracelet/<slug:product_slug>/', views.product_detail_in_bracelet, name='product_detail_in_bracelet'),
    path('products/category/necklace/<slug:product_slug>/', views.product_detail_in_necklace, name='product_detail_in_necklace'),
    path('products/category/decorative-hangings/<slug:product_slug>', views.product_detail_in_decorative_hangings, name='product_detail_in_decorative_hanging'),
    path('products/category/keychain/<slug:product_slug>/', views.product_detail_in_keychain, name='product_detail_in_keychain'),
    path('products/tag/<str:tag_slug>/<slug:product_slug>', views.product_detail_in_tag, name='product_detail_in_tag'),
    path('products/color/<str:color_slug>/<slug:product_slug>', views.product_detail_in_color, name='product_detail_in_color'),
    path('products/style/<str:style_slug>/<slug:product_slug>', views.product_detail_in_style, name='product_detail_in_style'),
    path('products/category/bracelet/', views.products_bracelet, name='bracelets'),
    path('products/category/necklace/', views.products_necklace, name='necklaces'),
    path('products/category/decorative-hangings/', views.products_decorative_hangings, name='decorative_hangings'),
    path('products/category/keychain/', views.products_keychain, name='keychains'),
    path('products/wishlist/', views.wishlist, name='wishlist'),
    path('products/wishlist/<int:product_id>/', views.add_wishlist, name='add_wishlist'),
    path('products/wishlist/remove/<int:product_id>/', views.remove_wishlist, name='remove_wishlist'),
    path('products/wishlist/<slug:product_slug>', views.product_detail_in_wishlist, name='product_detail_in_wishlist'),
    path('products/search/', views.search_product, name='search_product'),
    path('products/search/<slug:product_slug>', views.product_detail_in_search, name='search_detail'),
]
