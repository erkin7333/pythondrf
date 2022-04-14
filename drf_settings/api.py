from rest_framework import routers
from main import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewsets, basename='books')
router.register(r'lib-users', views.LibUserViewSets)
router.register(r'rented-books', views.RentBookViewSets)