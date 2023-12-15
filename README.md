# Prototipagem

# Raspberry Pi Telegram Alarm System

Este projeto implementa um sistema de alarme usando uma Raspberry Pi, um sensor de movimento e a biblioteca `python-telegram-bot` para enviar mensagens e vídeos via Telegram quando o sensor é acionado.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/)
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/)
- [ffmpeg](https://www.ffmpeg.org/)

1. Você pode instalar essas dependências usando o seguinte comando:

      ```bash
      pip install RPi.GPIO gpiozero python-telegram-bot

2. Além disso, o script usa o módulo ffmpeg para gravação de vídeos. Certifique-se de que o ffmpeg esteja instalado na sua Raspberry Pi. Você pode instalá-lo com o seguinte comando:

      ```bash
      sudo apt-get install ffmpeg
      

# Como Obter o Token do Bot no Telegram

Para integrar o seu bot Telegram ao projeto, você precisará obter o token do bot. Siga as etapas abaixo para criar um novo bot no Telegram e obter o token necessário.
    
1. **Crie um novo bot no Telegram:**
    - Abra o aplicativo Telegram e pesquise por [@BotFather](https://t.me/BotFather).
    - Inicie uma conversa com o BotFather e envie o comando `/newbot` para criar um novo bot.
    
2. **Siga as instruções do BotFather:**
    - O BotFather solicitará um nome para o seu bot. Escolha um nome adequado para o seu projeto.
    - Em seguida, o BotFather solicitará um nome de usuário para o bot. Este deve ser único e terminar com "bot" (por exemplo, `meubotalarme_bot`).
    - Após a conclusão, o BotFather fornecerá uma mensagem com o token do seu bot. O token será algo parecido com `1234567890:ABCDEFGHIJKLMNOPQRSTUVWX`.
    
3. **Guarde o Token do Bot:**
    - Copie o token fornecido pelo BotFather.
    - Substitua a variável `bot_token` no seu script pelo token que você acabou de copiar.
    
Agora, você tem o token do seu bot e pode usá-lo no seu projeto. Certifique-se de manter o token do bot em um local seguro e não o compartilhe publicamente.

**Observação:** Mantenha seu token em segredo, pois ele é essencial para a integração do seu bot com o Telegram.

## Configuração

1. **Token do Bot Telegram:**
   Substitua a variável `bot_token` no script pelo token real do seu bot Telegram.
   
2. **Lista de IDs dos Usuários:**
   Atualize a lista `lista_id` com os IDs reais dos usuários para os quais você deseja enviar mensagens e vídeos.

3. **Caminho do Arquivo de Saída:**
   Substitua `output_file` pelo caminho real do arquivo de vídeo que será enviado.

4. **Duração do Vídeo:**
   Ajuste a variável `duration` para a duração desejada do vídeo em segundos.

## Como Usar

1. Clone este repositório na sua Raspberry Pi:

   ```bash
   git clone https://github.com/aryelson1/raspberry-pi-telegram-alarm-system.git

2. Navegue até o diretório do projeto:

   ```bash
   cd raspberry-pi-telegram-alarm-system

3. Execute o script Python:

   ```bash
   python alarm_system.py

## Autor

- Aryelson Gonçalves(https://github.com/aryelson1)
- Antônio Roberto(https://github.com/antoniojunior2222)


## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

