"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home),
    path('about/',views.about),
    path('books/',views.books),
    path('contact/',views.contact),
    path('addbook/',views.addbook),
    path('login/',views.login),
    path('signup/',views.signup),
    path('Mystery-book/',views.mysterybook),
    path('programming-book/',views.program),
    path('Science-book/',views.science),
    path('Electronics-book/',views.electronics),
    path('Business-book/',views.business),
    path('History-book/',views.History),
    path('payment/', views.payment_page),
    path('Story-book/',views.story),
    path('newhome/',views.newhome),
    path('rent-programming/<int:id>/', views.rent_programming),
    path('rent-mystery/<int:id>/', views.rent_mystery),
    path('rent-science/<int:id>/', views.rent_science),
    path('rent-electronics/<int:id>/', views.rent_electronics),
    path('rent-business/<int:id>/', views.rent_business),
    path('rent-history/<int:id>/', views.rent_history),
    path('rent-story/<int:id>/', views.rent_story),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
