from abc import ABC, abstractclassmethod, abstractmethod

class Country(ABC):
    def init(self,name,population) -> None:
        super().init()
        self.name = name
        self.population = population

    @abstractmethod
    def show_detail(self):
        passfrom abc import ABC, abstractclassmethod, abstractmethod

class Country(ABC):
    def init(self,name,population) -> None:
        super().init()
        self.name = name
        self.population = population

    @abstractmethod
    def show_detail(self):
        pass