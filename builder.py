from abc import abstractmethod

class Builder():

    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_flavour(self, flavour):
        pass

    @abstractmethod
    def set_style(self, style):
        pass

    @abstractmethod
    def set_cover(self, cover):
        pass


class CakeBuilder(Builder):
    
    def __init__(self):
        super().__init__()
        self.result = Cake()

    def reset(self):
        self.result = Cake()

    def set_flavour(self, flavour):
        self.result.set_lavour(flavour)

    def set_style(self, style):
        self.reset.set_style(style)

    def set_cover(self, cover):
        self.reset.set_cover(cover)

    def get_result(self):
        return self.result


class Director():

    def __init__(self, builder):
        self.builder = builder

    def ChangeBuilder(self, builder):
        self.builder = builder

    def MakeCake(self):
        self.builder.reset()
        self.builder.set_style()
        self.builder.set_flavour()
        self.builder.set_cover()


class Cake():
    
    def set_flavour(self, flavour):
        self.flavour = flavour

    def set_style(self, style):
        self.style = style

    def set_cover(self, cover):
        self.cover = cover