from gazon import Gazon

class Tondeuse :     
    x : int 
    y : int 
    orientation : str
    def __init__(self, x : int,y : int,orientation : str) -> None:
        self.x =x
        self.y = y
        self.orientation = orientation
        pass
    
    def control(self,command : str,gazon : Gazon):
        if(command in ["D","G"]):
            self.turn(command)
        elif(command == "A"):
            
            self.move(gazon)
        print(self.x,self.y,self.orientation)
    
    def move(self, gazon : Gazon)-> None:    
        coords = []
        # NORTH
        if(self.orientation == "N"):
            coords = [self.x,self.y+1]
        
        #
        elif(self.orientation == "E"):
            coords = [self.x +1,self.y]
            
        #
        elif(self.orientation == "W"):
           coords = [self.x - 1,self.y]
           
        #  
        elif(self.orientation == "S"):
            coords = [self.x,self.y - 1]
        print(gazon)
        if(gazon.is_position_in_gazon(coords) == True):
            self.x =  coords[0]
            self.y = coords[1]
        else :
            print("l'opération ne peut etre effectuer")
    
    def turn(self,direction : str):
       if( direction in ["D","G"]):
           self.orientation = self.get_oriantation_assiociated(direction)
           print(self.orientation)
        
    def get_oriantation_assiociated(self,direction):
        oriantation_associated = {"D":"E","G":"W"}
        
        if(self.orientation == "N"):
            oriantation_associated = {"D":"E","G":"W"}
            
        elif(self.orientation == "E"):
            oriantation_associated = {"D":"S","G":"N"}
            
        elif(self.orientation == "W"):
            oriantation_associated = {"D":"N","G":"S"}
            
        elif(self.orientation == "S"):
            oriantation_associated = {"D":"W","G":"E"}
            
        return oriantation_associated[direction]
    
    def get_coords(self):
        print(self.x,self.y,self.orientation)
       # print(type(self.x),type(self.y),type(self.orientation))
        
        return [self.x,self.y,self.orientation]