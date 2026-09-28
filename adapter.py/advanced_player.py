from abc import ABC, abstractmethod


class AdvancedMediaPlayer(ABC):
    """Interface Adaptada (Adaptee)"""

    @abstractmethod
    def play_vlc(self, file_name: str):
        pass

    @abstractmethod
    def play_mp4(self, file_name: str):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    

    def play_vlc(self, file_name: str):
        print(f"Reproduzindo arquivo VLC. Nome: {file_name}")

    def play_mp4(self, file_name: str):
        pass  


class Mp4Player(AdvancedMediaPlayer):
    

    def play_vlc(self, file_name: str):
        pass  

    def play_mp4(self, file_name: str):
        print(f"Reproduzindo arquivo MP4. Nome: {file_name}")