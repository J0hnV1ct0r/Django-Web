from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..forms import ChallengeForm, ChallengeFormUpdate
from ..mediators.challengeMediator import ChallengeMediator
from ..models import Challenge




class ChallengeList(LoginRequiredMixin, ListView):
    """View de listagem dos desafios não completados pelo usuario."""
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'base/challenge_front/challenge_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mediator = ChallengeMediator(self.request)
        context.update(mediator.get_combined_context())
        return context


class ChallengeDetail(LoginRequiredMixin, DetailView):
    """View de detalhamento de desafios de leitura."""
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'base/challenge_front/challenge.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        challenge = self.get_object()
        mediator = ChallengeMediator(self.request)
        context.update(mediator.get_combined_context(challenge=challenge))
        return context


class ChallengeCreate(LoginRequiredMixin, CreateView):
    """View de criação de desafios de leitura."""
    model = Challenge
    form_class = ChallengeForm
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_form.html'

    def get_context_data(self, **kwargs):
        """Inclui a descrição gerada no contexto se disponível."""
        context = super().get_context_data(**kwargs)
        context['gpt_description'] = self.request.POST.get('gpt_description', '')
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        action = request.POST.get('action')

        if action == 'generate':
            if form.is_valid():
                # Captura os dados do livro e título do formulário
                book = form.cleaned_data['book']
                title = form.cleaned_data['title']
                mediator = ChallengeMediator(request)
                gpt_description = mediator.generate_challenge_description(book, title)

                # Retorna o formulário com a descrição gerada para o usuário revisar
                return render(request, self.template_name, {
                    'form': form,
                    'gpt_description': gpt_description
                })

        elif action == 'save':
            form = self.get_form()
            if form.is_valid():
                # Cria uma nova instância de Challenge com os dados do formulário
                challenge = form.save(commit=False)
                challenge.user = request.user
                challenge.save()
                return redirect(self.success_url)

        # Se a ação não for reconhecida ou o formulário for inválido
        return self.form_invalid(form)




class ChallengeUpdate(LoginRequiredMixin, UpdateView):
    """View de atualização de desafios de leitura."""
    model = Challenge
    form_class = ChallengeFormUpdate

    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_update.html'


class ChallengeDelete(LoginRequiredMixin, DeleteView):
    """View de deleção de desafios de leitura do sistema."""
    model = Challenge
    context_object_name = 'challenge'
    success_url = reverse_lazy('challenges')
    template_name = 'base/challenge_front/challenge_confirm_delete.html'
