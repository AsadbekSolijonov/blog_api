from django.urls import path, include  # new
from rest_framework import routers  # new

from blog.views import UserViewSet, UserAPIView  # new

router = routers.DefaultRouter()  # new
router.register(r'users', UserViewSet)  # new

# new
urlpatterns = [
    path('', include(router.urls)),
    path('followers/', UserAPIView.as_view()),
    path('followers/<int:pk>', UserAPIView.as_view(), name='user-detail')

]
