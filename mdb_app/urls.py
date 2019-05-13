from django.urls import path
from .views import ( MovieCreate, MovieList,
    UserCreate, LoginView,ChoiceListMovie, Temp , SnippetDetail)

urlpatterns = [
    path('api/movie_create/', MovieCreate.as_view(),name='movie_create'),
    path('api/list/',MovieList.as_view(),name='movie_list'),
    path('api/users/',UserCreate.as_view(),name='users'),
    path('api/login/',LoginView.as_view(),name='login'),
    path('api/movies/<int:pk>/choices/',ChoiceListMovie.as_view(),name='choice_list'),
    #path('api/del/<int:pk>', snippet_detail),
    path('api/serach/',Temp.as_view()),
    path('api/del/<int:pk>/', SnippetDetail.as_view()),




]
