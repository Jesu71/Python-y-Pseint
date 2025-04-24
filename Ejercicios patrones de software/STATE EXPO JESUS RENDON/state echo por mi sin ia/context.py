from state import StoppedState


class MusicPlayer:
    def __init__(self):
        self.state = StoppedState()

    def press_play(self):
        self.state.press_play(self)
