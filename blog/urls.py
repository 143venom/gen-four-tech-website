from django.urls import path
from . import views

urlpatterns = [
  path("blog", views.blog_index, name="blog"),
  path("blog_details/<int:blog_id>", views.blog_details, name="blog_details"),
  path("blog_details/<int:blog_id>/comment", views.blog_comment, name="blog_comment"),
  path("blog_details/<int:blog_id>/reply/<int:comment_id>", views.reply_comment, name="reply_comment"),
]