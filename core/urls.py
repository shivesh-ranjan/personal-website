from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.ProjectHomeView.as_view(), name="projects"),
    path("blogs/", views.BlogHomeView.as_view(), name="blogs"),
    path("blogs/<int:pk>", views.BlogPostView.as_view(), name="blogPost"),
]
