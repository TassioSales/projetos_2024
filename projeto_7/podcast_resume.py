import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr
import shutil


# Função para listar arquivos MP3
def list_mp3_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.endswith('.mp3')]


# Função para converter MP3 para WAV
def convert_mp3_to_wav(mp3_path, output_folder):
    audio = AudioSegment.from_mp3(mp3_path)
    wav_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(mp3_path))[0]}.wav")
    audio.export(wav_path, format="wav")
    return wav_path


# Função para transcrever áudio com Google SpeechRecognition
def transcribe_audio_google(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
            return recognizer.recognize_google(audio, language="pt-BR")
    except Exception as e:
        return f"Erro ao transcrever o áudio: {e}"


# Função para dividir áudios longos em segmentos menores
def split_audio(file_path, chunk_length_ms=60000):
    audio = AudioSegment.from_file(file_path)
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    return chunks


# Função principal
def main():
    audio_folder = "audios"
    temp_folder = "temp_wav"
    transcription_folder = "transcricao"

    os.makedirs(temp_folder, exist_ok=True)
    os.makedirs(transcription_folder, exist_ok=True)

    # Verificar se a pasta de áudios existe
    if not os.path.exists(audio_folder):
        print(f"Pasta '{audio_folder}' não encontrada. Crie a pasta e coloque os arquivos MP3 nela.")
        return

    # Listar arquivos MP3
    mp3_files = list_mp3_files(audio_folder)
    if not mp3_files:
        print("Nenhum arquivo MP3 encontrado.")
        return

    print("Arquivos MP3 disponíveis:")
    for idx, file in enumerate(mp3_files, start=1):
        print(f"{idx}. {file}")

    # Selecionar arquivo
    try:
        choice = int(input("Digite o número do arquivo que deseja transcrever: ")) - 1
        if choice < 0 or choice >= len(mp3_files):
            print("Escolha inválida. Tente novamente.")
            return
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return

    selected_file = mp3_files[choice]
    selected_path = os.path.join(audio_folder, selected_file)

    # Converter MP3 para WAV
    print("Convertendo MP3 para WAV...")
    wav_path = convert_mp3_to_wav(selected_path, temp_folder)

    # Dividir áudio, se necessário
    audio_chunks = split_audio(wav_path)
    print(f"Áudio dividido em {len(audio_chunks)} segmentos para transcrição.")

    # Transcrever cada segmento
    transcription = ""
    recognizer = sr.Recognizer()

    for idx, chunk in enumerate(audio_chunks):
        temp_chunk_path = os.path.join(temp_folder, f"chunk_{idx}.wav")
        chunk.export(temp_chunk_path, format="wav")

        try:
            with sr.AudioFile(temp_chunk_path) as source:
                audio = recognizer.record(source)
                print(f"Transcrevendo segmento {idx + 1}...")
                transcription += recognizer.recognize_google(audio, language="pt-BR") + " "
        except Exception as e:
            print(f"Erro ao transcrever segmento {idx + 1}: {e}")

    # Salvar transcrição
    transcription_file = os.path.join(transcription_folder, f"{os.path.splitext(selected_file)[0]}.txt")
    with open(transcription_file, "w", encoding="utf-8") as file:
        file.write(transcription)

    print(f"Transcrição salva em: {transcription_file}")

    # Limpar arquivos temporários
    try:
        for temp_file in os.listdir(temp_folder):
            temp_file_path = os.path.join(temp_folder, temp_file)
            os.remove(temp_file_path)
        # Remover a pasta temporária após excluir os arquivos
        shutil.rmtree(temp_folder)
    except PermissionError as e:
        print(f"Erro ao remover arquivos temporários: {e}")
    except OSError as e:
        print(f"Erro ao remover a pasta temporária: {e}")


if __name__ == "__main__":
    main()

