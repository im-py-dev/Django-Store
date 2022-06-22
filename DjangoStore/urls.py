import debug_toolbar
from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'Django Store Admin'
admin.site.index_title = 'Welcome admin'


urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),

    path('', include('store.urls')),
]
