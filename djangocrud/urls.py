from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from api import views
from . import view
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)
#router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path('^admin/',admin.site.urls),
    path('', include(router.urls)),
    #path('',view.index,name="index"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

admin.site.site_header = settings.SITE_NAME + " Admin"
admin.site.site_title = settings.SITE_NAME + " Admin"
admin.site.index_title = "Welcome to " + settings.SITE_NAME
