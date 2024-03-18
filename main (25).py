class Hero(ABC):
    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp
        
    @abstractmethod
    def active_skill(self):
        pass
    
    @abstractmethod
    def passive_skill(self):
        pass
    
    @abstractmethod
    def ulti(self):
        pass

hero = Hero("Generic Hero", 100, 2000)
