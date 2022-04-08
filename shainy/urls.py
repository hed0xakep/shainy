from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('api/auth/', include('djoser.urls')),                  #регистрация
    re_path(r'^auth/', include('djoser.urls.authtoken')),       #авторизация по токену
    path('api/posts/add/', views.AddPostView.as_view()),        #добавить запись
    path('api/posts/all/', views.PostsListView.as_view()),      #все записи
    path('api/responses/my/', views.MyResponsesView.as_view()), #отклики которые пришли на наши посты
    path('api/responses/match/<int:resp_id>/', views.MatchReponseView.as_view()), #ответить на оклик(ответом придет почта)
    path('api/responses/<post_id>/', views.SendResponse.as_view()), # url для отклика на пост
]
