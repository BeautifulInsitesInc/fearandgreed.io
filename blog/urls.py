from django.urls import path
#from . import views
from .views import ArticleListView
from .views import ArticleDetailView
from .views import BlogHome, AddPostView

urlpatterns = [
   path('', BlogHome.as_view(), name='blog'),
   path('article_list/', ArticleListView.as_view(), name='article-list'),
   path('article_detail/<int:pk>', ArticleDetailView.as_view(), name = 'article-detail'),
   path('add_post/', AddPostView.as_view(), name = 'add_post'),
]
