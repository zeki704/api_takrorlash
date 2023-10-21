from django.urls import path
from app1.views import Ishchiview
urlpatterns = [
    path("ishchi/", Ishchiview.as_view()),
    path("ishchi/<int:pk>/", Ishchiview.as_view()),
]
