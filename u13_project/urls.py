from django.urls import path

from .views import BookList,CreateBook,DeleteBook,UpdateBook


app_name = 'u13_project'

urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('create/', CreateBook.as_view(), name='create'),
    path('<int:pk>/', UpdateBook.as_view(), name='update_book'),
    path('delete/<int:pk>/', DeleteBook.as_view(), name='delete_book'),
]
