
from django.contrib import admin
from django.urls import path
from signup.views import signaction, sobre
from login.views import loginaction



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginaction, name = 'login'),
    path('', signaction),
    path('signup/', signaction, name = 'signup'),
    path('sobre/', sobre, name = 'sobre')

]
