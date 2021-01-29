
from django.contrib import admin
from django.urls import path, include
from query import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.querypage,name='querypage'),
    path('follow_up/',views.follow_up,name='follow_up'),
    path('login/',views.log,name='login'),
    path('logout/',views.out,name='logout'),
    path('updatequery/<int:id>/',views.updatequery,name='updatequery'),
    path('deletequery/<int:id>/',views.deletequery,name='deletequery'),
]
