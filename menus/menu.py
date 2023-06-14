from abc import ABC, abstractmethod
import curses

class Menu(ABC):

    @abstractmethod
    def spawn():
        pass