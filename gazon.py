
class Gazon :
    coords: list[int,int]
    
    def __init__(self, x:int, y: int) -> None:
        self.coords = [x,y]

    def is_position_in_gazon(self,coords : list[int,int]):
        for i in range(2): 
           if ((coords[i] > self.coords[i]) or (coords[i] < 0 )):
               return False
        return True
