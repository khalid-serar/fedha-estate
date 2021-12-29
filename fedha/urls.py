from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.signup, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('all-hoods/',views.neighbourhoods,name='neighbourhood'),
    url('new-hood/', views.create_neighbourhood, name='new-hood'),
    url('profile/', views.profile, name='profile'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
    path('leave_hood/<id>', views.leave_neighbourhood, name='leave-hood'),
    path('single_hood/<id>', views.single_neighbourhood, name='single-hood'),
    path('<hood_id>/post/', views.create_post, name='post'),
    url(r'^searched/', views.search_business, name='search'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)