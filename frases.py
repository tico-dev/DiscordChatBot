import random
from time import gmtime, strftime


class RandomMessage:
    def __init__(self, author):
        self.frases = [
            '"Seja a mudança que você quer ver no mundo" - Mahatma Gandhi',
            '"Posso não concordar com o que você diz, mas defenderei até a morte o seu direito de dizê-lo" - Voltaire',
            '"Para que o mal triunfe, basta que os bons não façam nada" - Edmund Burke',
            'Mais de 9 horas de codificação foram necessárias para desenvolver o esse BOT!',
            'Se esta funcionando, NÃO MEXA!!',
            'Eu te ouço!',
            'Talvez eu não tenha criatividade para criar tantas frases :(',
            f'{strftime("%Y-%m-%d %H:%M:%S", gmtime())}',
            'Já era hora!',
            'Tente o comando: HELP. Ele pode te ensinar algo 🤝',
            f'Desculpa {author.mention}, estou ocupado fazendo algo mais importante :pray:',
            'Chamou? :flushed:',
            '😒',
        ]

    def randomoption(self):
        return random.choice(self.frases)


class Texts:
    def __init__(self, activity_type, activity_input):
        self.activity_type = str(activity_type)
        self.activity_input = tuple(activity_input)
        doing_auxiliar = self.activity_type[13:].lower()
        print(doing_auxiliar)

        if doing_auxiliar == "playing":
            self.doing = "jogando"

        elif doing_auxiliar == "listening":
            self.doing = "ouvindo"

        elif doing_auxiliar == "streaming":
            self.doing = "streamando"

        elif doing_auxiliar == "watching":
            self.doing = "assistindo"

        if self.doing != "streamando":
            self.title = ' '.join(self.activity_input)

        else:
            self.title = ' '.join(self.activity_input[:-1])
            self.url = ''.join(self.activity_input[-1])
            self.url_formatada = self.url.replace("http://", '').replace("https://", '')

    def set_text(self):
        if self.doing != "streamando":
            # If activity_type is "playing", "listening" or "watching"
            return f'''Agora estou ***{self.doing}*** ``{self.title}``'''

        # If activity_type is "streaming"
        else:
            self.title = ' '.join(self.activity_input[:-1])
            print("url(frases): " + self.url)

            # Final text
            # -------- I'm now *** streaming *** ` stream title ` at ** stream url **
            return f'''Agora estou ***{self.doing}*** `{self.title}` em: **{self.url_formatada}**'''

    def get_title(self):
        print("title (frases): ", end='')
        print(self.title)
        return self.title

    def get_url(self):
        print("url (frases): ", end='')
        print(self.url)
        return self.url
