from abc import abstractmethod

class CakeFactory():

    @abstractmethod
    def createBirthdayCake(self):
        pass

    @abstractmethod
    def createWeddingCake(self):
        pass

    @abstractmethod
    def createPartyCake(self):
        pass


class ConcreteChocolateFactory(CakeFactory):

    def createBirthdayCake(self):
        return ConcreteChocolateBirthdayCake()

    def createWeddingCake(self):
        return ConcreteChocolateWeddingCake()

    def createPartyCake(self):
        return ConcreteChocolatePartyCake()


class ConcreteManiocFactory(CakeFactory):

    def createBirthdayCake(self):
        return ConcreteManiocBirthdayCake()

    def createWeddingCake(self):
        return ConcreteManiocWeddingCake()

    def createPartyCake(self):
        return ConcreteManiocPartyCake()


class ConcreteCarrotFactory(CakeFactory):

    def createBirthdayCake(self):
        return ConcreteCarrotBirthdayCake()

    def createWeddingCake(self):
        return ConcreteCarrotWeddingCake()

    def createPartyCake(self):
        return ConcreteCarrotPartyCake()


class Cake():

    def set_cover(self, cover):
        self.cover = cover


class BirthdayCake(Cake):
    
    def __init__(self):
        self.style = 'Birthday'

    def sing(self):
        return 'Happy birthday to you...'
    

class WeddingCake(Cake):
    
    def __init__(self):
        self.style = 'Wedding'

    def set_couple(self, groom, bride):
        self.goom = groom
        self.bride = bride


class PartyCake(Cake):
    
    def __init__(self):
        self.style = 'Party'

    def change_color(self, color):
        self.color = color


class ConcreteChocolateBirthdayCake(BirthdayCake):

    def __init__(self):
        super().__init__()


class ConcreteChocolateWeddingCake(WeddingCake):

    def __init__(self):
        super().__init__()

    
class ConcreteChocolatePartyCake(PartyCake):

    def __init__(self):
        super().__init__()


class ConcreteManiocBirthdayCake(BirthdayCake):

    def __init__(self):
        super().__init__()


class ConcreteManiocWeddingCake(WeddingCake):

    def __init__(self):
        super().__init__()

    
class ConcreteManiocPartyCake(PartyCake):

    def __init__(self):
        super().__init__()


class ConcreteCarrotBirthdayCake(BirthdayCake):

    def __init__(self):
        super().__init__()


class ConcreteCarrotWeddingCake(WeddingCake):

    def __init__(self):
        super().__init__()

    
class ConcreteCarrotPartyCake(PartyCake):

    def __init__(self):
        super().__init__()