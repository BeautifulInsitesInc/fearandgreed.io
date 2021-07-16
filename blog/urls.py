from django.urls import path
#from . import views
from .views import ArticleListView
from .views import ArticleDetailView
from .views import BlogHome, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
   path('', BlogHome.as_view(), name='blog'),
   path('article_list/', ArticleListView.as_view(), name='article_list'),
   path('article_detail/<int:pk>', ArticleDetailView.as_view(), name = 'article_detail'),
   path('add_post/', AddPostView.as_view(), name = 'add_post'),
   path('edit_post/<int:pk>', EditPostView.as_view(), name = 'edit_post'),
   path('delete_post/<int:pk>', DeletePostView.as_view(), name = 'delete_post'),
   path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
   #path('category_list/', CategoryListView.as_view(), name = 'category_list'),
   path('category/<str:category_name>/', CategoryView, name = 'category'),

]
