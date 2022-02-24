from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path
from Products.views import *
urlpatterns = [
    path('about', about),
    path('', login_required(ListProduct.as_view(), login_url='/login/'), name= 'home'),
    path('buying', login_required(buying.as_view(), login_url='/login/'), name='confirmar_compra'),
    path('master', login_required(CreateProduct.as_view(), login_url='/login/'), name = 'add_product'),
    path('master/<int:pk>', login_required(UpdateProduct.as_view(), login_url='/login/'), name = 'edit_product'),
    path('delete_product/<int:pk>', login_required(DeleteProduct.as_view(), login_url='/login/'), name = 'delete_product'),
    path('register/',  register, name = 'register'),
    path('login/', login_required(LoginView.as_view(template_name = 'login.html'), login_url='/login/'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'logout.html'), name='logout'),
    path('contact_us', post, name = 'post'),
    path('historial/', sendRequest, name='historial')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
