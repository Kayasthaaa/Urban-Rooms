from unicodedata import name
from django.urls import path, include
from . import views
urlpatterns = [
   # path('signup', views.signup),
    path('login', views.login),
    path('signup', views.Sign.as_view()),
    path('api-auth/', include('rest_framework.urls')),

    path('rooms', views.RoomList.as_view()),
    path('rooms/<int:pk>', views.RoomRetriveDestroy.as_view()),

]
