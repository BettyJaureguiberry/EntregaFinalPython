from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Page

# 🌐 Vistas generales
def home_view(request):
    return render(request, 'blog/home.html')

def about_view(request):
    return render(request, 'blog/about.html')

# 📄 Listado de páginas (CBV)
class PageListView(ListView):
    model = Page
    template_name = 'blog/pages_list.html'
    context_object_name = 'pages'

# 📄 Detalle de página (CBV)
class PageDetailView(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'

# 📝 Crear página (CBV)
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# 📝 Editar página (CBV)
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ['title', 'subtitle', 'content', 'image']
    template_name = 'blog/page_form.html'
    success_url = reverse_lazy('pages_list')

# 🗑️ Borrar página (decorador en FBV + CBV)
@method_decorator(login_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    template_name = 'blog/page_confirm_delete.html'
    success_url = reverse_lazy('pages_list')

# 👤 Registro de usuario
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})