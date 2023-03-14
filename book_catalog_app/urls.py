
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('login_user',views.login_user,name='login_user'),
    path('logout',views.logout,name='logout'),
    path('get_books',views.get_books,name='get_books'),
    path('add_book_to_collection',views.add_book_to_collection,name='add_book_to_collection'),
    path('delete',views.delete,name='delete'),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)