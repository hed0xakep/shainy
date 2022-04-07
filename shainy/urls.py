from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),  # new
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
    path('api/posts/add/', views.AddPostView.as_view()),
    path('api/posts/all/', views.PostsListView.as_view())
]
