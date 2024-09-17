from django.shortcuts import render
from django.apps import apps


def chat_with_merlin(request):
    if request.method == 'POST':
        user_message = request.POST.get('message', '')
        if user_message:
            gpt_model = apps.get_app_config('base').gpt_model_instance
            response = gpt_model.get_text_ia(prompt=user_message, max_tokens=100)
            return render(request, 'base/chat.html', {'response': response, 'user_message': user_message})
        return render(request, 'base/chat.html', {'error': 'Mensagem não pode ser vazia'})

    return render(request, 'base/chat.html')