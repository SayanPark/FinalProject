from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.mainpage, name='starting_page'),
    # path('members-join', views.mainpagemember, name='member_page')
    # path('<path:error>', views.handle_invalid_path, name='error')
]
