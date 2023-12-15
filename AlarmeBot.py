import RPi.GPIO as GPIO
import time
import asyncio
import subprocess
from telegram import Bot
from telegram import InputFile
from gpiozero import MotionSensor

# Configuração do bot
bot_token = '6960608001:AAHmE8CE5xRhHkgHMUl-s_G_6UdRnWQOTSQ'  # Token do Bot
lista_id = [ '5201121335','1622322437']  # ID dos usuários '1622322437',
output_file = "/home/assert/Desktop/protAlarme/Aviso.mp4"  # Caminho do Arquivo
duration = 10  # Duração do vídeo em segundos
#parte do instagram
#######

'''login = 'gabriel_alves778' #Usuario
senha = 'AulaInsta' #Senha
cl = Client()
cl.login(login, senha)
user_id_destinatario = cl.user_id_from_username('lucasdaris_ec')    # Destinatario'''
########## quando voces chegarem coloquem a funcao cl.logout() no final do codigo tambem. Obrigado

def record_video(output_file, duration):
    try:
        # Comando para gravar um vídeo usando o ffmpeg
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

        # Executa o comando
        subprocess.run(command, check=True)

        print(f"Vídeo gravado e salvo em {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gravar vídeo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

async def enviar_mensagem():
    # Criando o bot
    bot = Bot(token=bot_token)

    # Mensagem
    mensagem = 'ALARME ACIONADO'

    # Video
    record_video(output_file, duration)

    # Envio da mensagem
    for i in lista_id:
        await bot.send_message(chat_id=i, text=mensagem)
        #result = cl.direct_send(mensagem, user_ids=[user_id_destinatario]) # envia msg do instagram
        video = open(output_file, "rb")
        await bot.send_video(chat_id=i, video=InputFile(video))
        video.close()

async def main():
    pir = MotionSensor(17)

    while True:
        pir.wait_for_motion()
        if pir.motion_detected:
            await enviar_mensagem()
            await asyncio.sleep(15)



# Roda o loop principal
if __name__ == "__main__":
    asyncio.run(main())