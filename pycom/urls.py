import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("produtos/", include("products.urls")),
    path("carrinho/", include("cart.urls")),
    path("", include("pages.urls")),
    path("orders/",include("orders.urls")),    
    path("accounts/",include("allauth.urls")),
    path("payments/", include("payments.urls")),
    path("blog/", include("blog.urls")),
    path("perfil/", include("users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]