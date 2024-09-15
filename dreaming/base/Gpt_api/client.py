from gpt4all import GPT4All


class GPTModel:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GPTModel, cls).__new__(cls)
            cls._instance._initialize()  # Chama o inicializador apenas uma vez
        return cls._instance

    def _initialize(self):
        """Este método é chamado uma vez para configurar o modelo."""
        self.model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

    def get_text_ia(self, prompt, max_tokens):
        with self.model.chat_session():
            text_ia = self.model.generate(prompt, max_tokens=max_tokens)
        return text_ia