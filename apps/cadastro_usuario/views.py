from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import Usuario
from django.contrib.auth.hashers import make_password



class UsuarioCreate(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['primeiro_nome', 'segundo_nome', 'email', 'empresa']


    def form_valid(self, form):
        usuario = form.save(commit=False)

        username = usuario.primeiro_nome.lower() + usuario.segundo_nome.lower()
        # criptografa a senha padrao
        # sem criptografar a senha nao eh possivel logar com o user criado
        # agora vc pode logar no sistema com o username e senha padrao
        password = make_password('123456')

        usuario.user = User.objects.create(username=username, password=password)
        usuario.save()

        return super(UsuarioCreate, self).form_valid(form)