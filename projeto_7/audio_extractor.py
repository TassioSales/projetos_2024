from pytubefix import YouTube
from pydub import AudioSegment
import os
import sys


# Função para obter o link do YouTube do usuário
def obter_audio():
    try:
        link = input("Digite o link do vídeo: ")
        youtube_video = YouTube(link)
        return youtube_video
    except Exception as e:
        print(f"Erro ao obter o áudio: {e}. Verifique o link e sua conexão de internet.")
        return None


# Função para baixar o áudio
def baixar_audio(youtube_video):
    try:
        diretorio = "audios"
        if not os.path.exists(diretorio):
            os.makedirs(diretorio)

        stream_audio = youtube_video.streams.filter(only_audio=True).first()
        if not stream_audio:
            print("Erro: Nenhum stream de áudio disponível para este vídeo.")
            return False

        arquivo_destino = os.path.join(diretorio, f"{youtube_video.title}.mp4")
        if os.path.exists(arquivo_destino):
            print("Áudio já foi baixado anteriormente.")
            return True

        stream_audio.download(output_path=diretorio, filename=f"{youtube_video.title}.mp4")
        print(f"Áudio baixado: {arquivo_destino}")
        return True
    except Exception as e:
        print(f"Erro ao baixar o áudio: {e}. Verifique se há espaço no disco e se o link é válido.")
        return False


# Função para converter o áudio para MP3 usando pydub
def converter_audio():
    try:
        for arquivo in os.listdir("audios"):
            if arquivo.endswith(".mp4"):
                arquivo_mp4 = os.path.join("audios", arquivo)
                arquivo_mp3 = os.path.join("audios", arquivo.replace(".mp4", ".mp3"))

                if os.path.exists(arquivo_mp3):
                    print(f"O arquivo {arquivo_mp3} já existe e não será convertido novamente.")
                    continue

                # Converte o arquivo de MP4 para MP3 com pydub
                try:
                    audio = AudioSegment.from_file(arquivo_mp4, format="mp4")
                    audio.export(arquivo_mp3, format="mp3")
                    print(f"Convertido: {arquivo} -> {arquivo_mp3}")

                    # Após a conversão, exclui o arquivo .mp4
                    os.remove(arquivo_mp4)
                    print(f"Arquivo MP4 excluído: {arquivo_mp4}")
                except Exception as e:
                    print(f"Erro ao converter {arquivo}: {e}")
                    continue
        return True
    except Exception as e:
        print(f"Erro ao converter os arquivos de áudio: {e}")
        return False


# Função principal
def main():
    youtube_video = obter_audio()
    if youtube_video:
        if baixar_audio(youtube_video):
            if converter_audio():
                print("Áudio baixado e convertido com sucesso!")
            else:
                print("Erro ao converter o áudio!")
        else:
            print("Erro ao baixar o áudio!")
    else:
        print("Erro ao obter o áudio!")


# Função para executar o programa com tratamento de erros
def executar_programa():
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcesso interrompido pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        sys.exit(1)


# Execução do programa
if __name__ == "__main__":
    executar_programa()
