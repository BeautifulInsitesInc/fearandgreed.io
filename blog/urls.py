from django.urls import path
#from . import views
from .views import PostListView
from .views import PostDetailView
from .views import BlogHome, AddPostView, EditPostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, DeleteCategoryView, EditCategoryView, LikeView, AddCommentView

urlpatterns = [
   path('', BlogHome.as_view(), name='blog'),
   path('post_list/', PostListView.as_view(), name='post_list'),
   path('post_detail/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
   #path('<str:post_name>/', PostDetailView.as_view(), name = 'post_detail'),
   path('add_post/', AddPostView.as_view(), name = 'add_post'),
   path('edit_post/<int:pk>', EditPostView.as_view(), name = 'edit_post'),
   path('delete_post/<int:pk>', DeletePostView.as_view(), name = 'delete_post'),
   path('add_category/', AddCategoryView.as_view(), name = 'add_category'),
   path('category_list/', CategoryListView, name = 'category_list'),
   path('category/<str:category_name>/', CategoryView, name = 'category'),
   path('delete_category/<int:pk>', DeleteCategoryView.as_view(), name = 'delete_category'),
   path('edit_category/<int:pk>', EditCategoryView.as_view(), name = 'edit_category'),
   path('like/<int:pk>', LikeView, name = 'like_post'),
   path('post/<int:pk>/comment', AddCommentView.as_view(), name = 'add_comment'),
]
