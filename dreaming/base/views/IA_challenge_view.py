from django.shortcuts import render, redirect, get_object_or_404
from ..forms import ChallengeForm
from django.urls import reverse_lazy
import time
from django.apps import apps


def create_challenge(request):
    gpt_description = None

    if request.method == 'POST':
        form = ChallengeForm(request.POST)

        if request.POST.get('action') == 'generate':  # Se o botão "Gerar Desafio" for clicado
            if form.is_valid():
                # Captura os dados do formulário
                book = form.cleaned_data['book']
                title = form.cleaned_data['title']

                # Definir o objetivo desejado
                objective = f"Crie um desafio para o livro '{book}' com o objetivo '{title}'. O desafio deve durar 30 dias"
                print(f"Iniciando geração de desafio para o livro '{book}' com o objetivo '{title}'")
                start_time = time.time()  # Opcional: captura o tempo de início

                # Gera o desafio usando o modelo GPT
                gpt_model = apps.get_app_config('base').gpt_model_instance
                gpt_description = gpt_model.get_text_ia(prompt=objective, max_tokens=150)

                print(f"Desafio gerado em {time.time() - start_time:.2f} segundos")

                # Exibe a descrição gerada na tela, mas não salva ainda
                return render(request, 'base/challenge_front/challenge_form.html', {
                    'form': form,
                    'gpt_description': gpt_description  # Passa a descrição gerada para o template
                })

        elif 'save' in request.POST:  # Se o botão "Salvar" for clicado
            if form.is_valid():
                # Preenche a descrição do desafio com o texto gerado pelo GPT, se disponível
                form.instance.user = request.user
                form.instance.description = request.POST.get('gpt_description')  # Atribui a descrição gerada pelo GPT
                form.save()

                return redirect(reverse_lazy('challenges'))  # Redireciona para a lista de desafios
    else:
        form = ChallengeForm()

    return render(request, 'base/challenge_front/challenge_form.html', {'form': form})