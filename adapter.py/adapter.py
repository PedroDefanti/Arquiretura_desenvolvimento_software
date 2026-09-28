from advanced_player import Mp4Player, VlcPlayer
from media_player import MediaPlayer


class MediaAdapter(MediaPlayer):

    def __init__(self, audio_type: str):
        self.advanced_music_player = None
        if audio_type.lower() == "vlc":
            self.advanced_music_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_music_player = Mp4Player()

    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "vlc":
            self.advanced_music_player.play_vlc(file_name)
        elif audio_type.lower() == "mp4":
            self.advanced_music_player.play_mp4(file_name)