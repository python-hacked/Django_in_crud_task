from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index),
    path("Ragistration/", create_user),
    path("data/",table),
    path("delete/<int:pk>/",delete_user, name="delete"),
    path("update/<int:uid>/",update_user, name="update"),
    path("update_user/",update_data),
    # path("login/", login_view),
    path("login_us/", login),
    path("login/", login_user),
    path("product/", product),
    path("add_product/", add_product)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # for image uploading</s
