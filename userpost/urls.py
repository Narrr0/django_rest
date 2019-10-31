from django.urls import include, path
from rest_framework.routers import DefaultRouter
from userpost import views

router=DefaultRouter()
router.register('',views.UserPostViewSet)

urlpatterns=[
    path('',include(router.urls))
]