

class Gazon :
    """ Gazon CLASS """
    
    coords: list[int,int]
    
    def __init__(self, x:int, y: int) -> None:
        self.coords = [x,y]
        self.positions_occupated = []

    def is_position_in_gazon(self,coords : list[int,int]) -> bool:
        for i in range(2): 
           if ((coords[i] > self.coords[i]) or (coords[i] < 0 )):
               return False
           
        # if the coordinates are corret but occupied,
        # it will be returned false because 2 lawnmowers can't have the same postion
        return True and not self.is_position_occupated(coords) 
    
    def is_position_occupated(self,coords : list[int]) -> bool:
        if(coords in self.positions_occupated) :
            return True
        else :
            return False
        
    def add_position_in_gazon(self,coords : list[int]):
        self.positions_occupated.append(coords)
        
    def remove_position_in_gazon(self,coords : list[int]):
        self.positions_occupated.remove(coords)