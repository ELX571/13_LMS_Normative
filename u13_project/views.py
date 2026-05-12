from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from u13_project.models import Book


class BookList(ListView):
    model = Book
    template_name = 'u13_project/book_list.html'
    paginate_by = 3
    context_object_name = 'book_list'

    def get_queryset(self):
        search = self.request.GET.get("search")

        if search:
            result = Book.objects.filter(
                Q(title__icontains=search) |
                Q(author__icontains=search)
            )
            return result
        else:
            return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class CreateBook(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    template_name = 'u13_project/book_create.html'
    permission_required = 'u13_project.add_book'
    success_url = reverse_lazy('u13_project:book_list')


class UpdateBook(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'u13_project/book_update.html'
    success_url = reverse_lazy('u13_project:book_list')
    permission_required = 'u13_project.change_book'


class DeleteBook(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'u13_project/book_delete.html'
    permission_required = 'u13_project.delete_book'
    success_url = reverse_lazy('u13_project:book_list')
