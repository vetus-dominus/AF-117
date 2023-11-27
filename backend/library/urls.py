""" Route URLs """
from rest_framework.routers import DefaultRouter
from library.views import BooklistViewSet
from library.views import UsersViewSet

router = DefaultRouter()
router.register(r'booklist', BooklistViewSet, basename='booklist')
router.register(r'users', UsersViewSet, basename='users')
library_urlpatterns = router.urls
