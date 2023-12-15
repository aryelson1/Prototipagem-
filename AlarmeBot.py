"""
Sistema de Alarme com Raspberry Pi e Telegram

Este script monitora um sensor de movimento usando uma Raspberry Pi e envia uma mensagem e um vídeo
via Telegram quando o sensor é acionado.

Dependências:
- RPi.GPIO
- gpiozero
- python-telegram-bot
- ffmpeg

Certifique-se de instalar essas bibliotecas antes de executar o script.

Autor: [Seu Nome/Autor]

"""

# Importação de módulos necessários
import RPi.GPIO as GPIO  # Módulo para interagir com os pinos GPIO da Raspberry Pi
import time  # Módulo para manipulação de tempo
import asyncio  # Módulo para suportar programação assíncrona
import subprocess  # Módulo para executar subprocessos
from telegram import Bot  # Classe Bot da biblioteca python-telegram-bot para interagir com a API do Telegram
from telegram import InputFile  # Classe InputFile para representar um arquivo a ser enviado ao Telegram
from gpiozero import MotionSensor  # Módulo gpiozero para interagir com o sensor de movimento

# Configuração do bot
bot_token = 'SEU_TOKEN_DO_BOT'  # Substitua pelo token real do seu bot
lista_id = ['ID_USUARIO_1', 'ID_USUARIO_2']  # Substitua pelos IDs reais dos usuários
output_file = "/caminho/para/o/arquivo/Aviso.mp4"  # Substitua pelo caminho real do arquivo
duration = 10  # Duração do vídeo em segundos

def record_video(output_file, duration):
    """
    Grava um vídeo usando o ffmpeg.

    Parâmetros:
    - output_file: Caminho do arquivo de saída.
    - duration: Duração do vídeo em segundos.
    """
    try:
        command = [
            "ffmpeg",
            "-y",
            "-f", "v4l2",
            "-input_format", "h264",
            "-video_size", "1920x1080",
            "-framerate", "30",
            "-i", "/dev/video0",
            "-t", str(duration),
            "-vcodec", "copy",
            output_file
        ]
        subprocess.run(command, check=True)  # Executa o comando ffmpeg para gravar o vídeo
        print(f"Vídeo gravado e salvo em {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gravar vídeo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

async def enviar_mensagem():
    """
    Envia uma mensagem e um vídeo via Telegram.

    A mensagem e o vídeo são enviados para todos os usuários na lista_id.
    """
    bot = Bot(token=bot_token)  # Cria uma instância do bot
    mensagem = 'ALARME ACIONADO'
    record_video(output_file, duration)  # Grava o vídeo
    for user_id in lista_id:
        await bot.send_message(chat_id=user_id, text=mensagem)  # Envia a mensagem para cada usuário na lista
        video = open(output_file, "rb")
        await bot.send_video(chat_id=user_id, video=InputFile(video))  # Envia o vídeo para cada usuário na lista
        video.close()

async def main():
    """
    Função principal que monitora o sensor de movimento e aciona o envio de mensagem e vídeo.
    """
    pir = MotionSensor(17)  # Cria uma instância do sensor de movimento
    while True:
        pir.wait_for_motion()  # Aguarda até que o sensor detecte movimento
        if pir.motion_detected:
            await enviar_mensagem()  # Chama a função para enviar mensagem e vídeo
            await asyncio.sleep(15)  # Aguarda 15 segundos antes de continuar o loop

# Executa o loop principal
if __name__ == "__main__":
    asyncio.run(main())  # Inicia o loop principal usando asyncio
