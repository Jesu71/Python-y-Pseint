from abc import ABC, abstractmethod
 
class PlayerState(ABC):
    @abstractmethod
    def press_play(self, player):
        pass

class PlayingState(PlayerState):
    def press_play(self, player):
        print("Pausing")
        player.state = PausedState()

class PausedState(PlayerState):
    def press_play(self, player):
        print("Playing")
        player.state = PlayingState()

class StoppedState(PlayerState):
    def press_play(self, player):
        print("Playing")
        player.state = PlayingState()