from gpt4all import GPT4All

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

def get_challenge_ai_description(title, book):
    prompt = f'''
    crie um desafio litearrio para a obra {book} em apenas 50 caracteres. O desafio tem que durar no maximo 30 dias e 
    tem o objetivo{title}.
    '''

    with model.chat_session():
        decription = model.generate(prompt, max_tokens=130)


    return decription