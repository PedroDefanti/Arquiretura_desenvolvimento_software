from media_player import AudioPlayer


class Principal:
    

    @staticmethod
    def main():
        player = AudioPlayer()

        print("--- Testando Reprodução ---")
        player.play("mp3", "musica_estilo.mp3")
        player.play("mp4", "video_viagem.mp4")
        player.play("vlc", "filme_classico.vlc")
        player.play("avi", "formato_invalido.avi")


if __name__ == "__main__":
    Principal.main()