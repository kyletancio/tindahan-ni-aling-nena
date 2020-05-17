"""manSys1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from web import views as page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page.home, name="home"),
    path('products/', page.products, name="products"),
    path('about/', page.about, name="about"),
    path('login/', page.login, name="login"),
    path('signup/', page.signup, name="signup"),
    path('view/<product_id>', page.view, name="view"),
    path('edit/<product_id>', page.edit, name="edit"),
    path('delete/<product_id>', page.delete, name="delete"),
]
