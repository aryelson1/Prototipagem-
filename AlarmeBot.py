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

Autores: Antonio Roberto
       Aryelson Gonçalves 

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
bot_token = 'SEU_TOKEN_DO_BOT'  # Substitua pelo token real do seu bot Ex: 6960608001:AAHmE8CE5xRhHkgHMUl-s_G_6UdRnWQOTSQ
lista_id = ['ID_USUARIO_1', 'ID_USUARIO_2']  # Substitua pelos IDs reais dos usuários Ex: 1622322437
output_file = "/caminho/para/o/arquivo/Aviso.mp4"  # Substitua pelo caminho real do arquivo Ex: /home/assert/Desktop/protAlarme/Aviso.mp4
duration = 10  # Duração do vídeo em segundos

def record_video(output_file, duration):
    """
    Grava um vídeo usando o ffmpeg.

    Parâmetros:
    - output_file: Caminho do arquivo de saída.
    - duration: Duração do vídeo em segundos.
    """
    
    try:
        # Comando para capturar vídeo da câmera usando ffmpeg
        command = [
            "ffmpeg",              # Executável ffmpeg
            "-y",                  # Sobrescreve o arquivo de saída, se existir
            "-f", "v4l2",          # Formato de entrada: v4l2 (Video for Linux Two)
            "-input_format", "h264",  # Formato de entrada do vídeo H.264
            "-video_size", "1920x1080",  # Resolução do vídeo: 1920x1080 pixels
            "-framerate", "30",    # Taxa de quadros: 30 frames por segundo
            "-i", "/dev/video0",  # Dispositivo de vídeo de entrada (pode variar)
            "-t", str(duration),   # Duração da gravação em segundos
            "-vcodec", "copy",     # Usa o mesmo codec de vídeo de entrada para a saída
            output_file            # Caminho do arquivo de saída
        ]

        # Executa o comando ffmpeg para gravar o vídeo
        subprocess.run(command, check=True)
        
        # Mensagem de sucesso
        print(f"Vídeo gravado e salvo em {output_file}")

    except subprocess.CalledProcessError as e:
        # Trata erro se o subprocesso falhar
        print(f"Erro ao gravar vídeo: {e}")

    except Exception as e:
        # Trata erros inesperados
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
