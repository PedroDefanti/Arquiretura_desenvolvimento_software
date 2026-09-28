from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    """Interface Alvo (Target)"""

    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass


class AudioPlayer(MediaPlayer):
    

    def __init__(self):
        self.media_adapter = None

    def play(self, audio_type: str, file_name: str):
        
        if audio_type.lower() == "mp3":
            print(f"Reproduzindo arquivo MP3. Nome: {file_name}")

        
        elif audio_type.lower() in ["vlc", "mp4"]:
            
            from adapter import MediaAdapter

            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        else:
            print(f"Erro: O formato '{audio_type}' não é suportado.")