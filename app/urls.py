from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),

    # Se num futuro for versionar as urls/recursos esse seria o padrão:
    # path('api/v2/', include('actors.urls_v2'))
    # path('api/v3/', include('actors.urls_v3'))
    # isso permite manter varias versões rodando mantendo o legado
]
