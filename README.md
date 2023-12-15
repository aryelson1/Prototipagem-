# Prototipagem

    <h1>Raspberry Pi Telegram Alarm System</h1>

    <p>Este projeto implementa um sistema de alarme usando uma Raspberry Pi, um sensor de movimento e a biblioteca <code>python-telegram-bot</code> para enviar mensagens e vídeos via Telegram quando o sensor é acionado.</p>

    <h2>Requisitos</h2>

    <p>Certifique-se de ter as seguintes bibliotecas instaladas:</p>

    <ul>
        <li><a href="https://pypi.org/project/RPi.GPIO/" target="_blank">RPi.GPIO</a></li>
        <li><a href="https://gpiozero.readthedocs.io/en/stable/" target="_blank">gpiozero</a></li>
        <li><a href="https://python-telegram-bot.readthedocs.io/en/stable/" target="_blank">python-telegram-bot</a></li>
        <li><a href="https://www.ffmpeg.org/" target="_blank">ffmpeg</a></li>
    </ul>

    <p>Você pode instalar essas dependências usando o seguinte comando:</p>

    <pre><code>pip install RPi.GPIO gpiozero python-telegram-bot</code></pre>

    <p>Além disso, o script usa o módulo <code>ffmpeg</code> para gravação de vídeos. Certifique-se de que o <code>ffmpeg</code> esteja instalado na sua Raspberry Pi. Você pode instalá-lo com o seguinte comando:</p>

    <pre><code>sudo apt-get install ffmpeg</code></pre>

    <h2>Configuração</h2>

    <ol>
        <li><strong>Token do Bot Telegram:</strong><br>Substitua a variável <code>bot_token</code> no script pelo token real do seu bot Telegram.</li>
        <li><strong>Lista de IDs dos Usuários:</strong><br>Atualize a lista <code>lista_id</code> com os IDs reais dos usuários para os quais você deseja enviar mensagens e vídeos.</li>
        <li><strong>Caminho do Arquivo de Saída:</strong><br>Substitua <code>output_file</code> pelo caminho real do arquivo de vídeo que será enviado.</li>
        <li><strong>Duração do Vídeo:</strong><br>Ajuste a variável <code>duration</code> para a duração desejada do vídeo em segundos.</li>
    </ol>

    <h2>Como Usar</h2>

    <ol>
        <li>Clone este repositório na sua Raspberry Pi:</li>
        <pre><code>git clone https://github.com/seu-usuario/raspberry-pi-telegram-alarm-system.git</code></pre>
        <li>Navegue até o diretório do projeto:</li>
        <pre><code>cd raspberry-pi-telegram-alarm-system</code></pre>
        <li>Execute o script Python:</li>
        <pre><code>python alarm_system.py</code></pre>
    </ol>

    <p>O script ficará aguardando o acionamento do sensor de movimento. Quando o sensor detectar movimento, ele enviará uma mensagem e um vídeo via Telegram para os usuários configurados.</p>

    <h2>Autores</h2>

    <p>Aryelson Gonçalves</p>
    <p>Antônio Roberto</p>

    <h2>Licença</h2>

    <p>Este projeto está licenciado sob a <a href="LICENSE" target="_blank">Licença MIT</a>.</p>
