from django.urls import path
from .views import HomePageVieew,DetailPageView, CreatePostView,UpdatePostView,DeletePostView, ArticlePageVieew,PrivacyPageVieew,TermsPageVieew
urlpatterns=[
    path('',HomePageVieew.as_view(),name='home'),
    path('post/<int:pk>',DetailPageView.as_view(),name='post_detail'),
    path('post/new/',CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',UpdatePostView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete/',DeletePostView.as_view(),name='post_delete'),
    path('article/',ArticlePageVieew.as_view(),name='article'),
    path('',TermsPageVieew.as_view(),name='terms'),
    path('',PrivacyPageVieew.as_view(),name='privacy'),

]