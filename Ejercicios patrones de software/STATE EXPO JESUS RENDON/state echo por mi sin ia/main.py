from state import PlayingState as PausedState, StoppedState
from context import MusicPlayer

def main():
    player = MusicPlayer()
    player.press_play()
    player.press_play()
    player.press_play()

if __name__ == "__main__":
    main()
    