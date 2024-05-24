from gazon import Gazon
class Tondeuse : 
    """ Tondeuse CLASS """
    
    x : int 
    y : int 
    orientation : str
    def __init__(self, x : int,y : int,orientation : str,gazon : Gazon) -> None:
        self.set_x(x,gazon)
        self.set_y(y,gazon)
        self.set_orientation(orientation)
        
        # add the x,y coordinates to the turf
        gazon.add_position_in_gazon(self.get_xy())
    
    def execute_instructions(self,instructions : list[str],gazon: Gazon):
        """ Execute all the instruction and then print out coordinates of the lawnmower"""
        for instruction in instructions :
            
           self.control(instruction,gazon)
        # print the coordinates 
        self.get_coords()
        pass
    
    def control(self,command : str,gazon : Gazon):
        """ Execute the instruction to move or to turn a lawnmower """
        if(command in ["D","G"]):
            self.turn(command)
        elif(command == "A"):
            self.move(gazon)
    
    # make an action when the command is "A"
    def move(self, gazon : Gazon)-> None:    
        coords = []
        # The advancement if the oriention is on "N" equal (x,y+1)
        if(self.orientation == "N"):
            coords = [self.x,self.y+1]
        
        # The advancement if the oriention is on "E" equal (x+1,y)
        elif(self.orientation == "E"):
            coords = [self.x +1,self.y]
            
        # The advancement if the oriention is on "W" equal (x-1,y)
        elif(self.orientation == "W"):
           coords = [self.x - 1,self.y]
           
        # The advancement if the oriention is on "S" equal (x,y-1)  
        elif(self.orientation == "S"):
            coords = [self.x,self.y - 1]
        
        if(gazon.is_position_in_gazon(coords) == True):
            gazon.remove_position_in_gazon(self.get_xy())
            gazon.add_position_in_gazon(coords)
            self.set_x(coords[0],gazon) 
            self.set_y(coords[1],gazon) 
            
        else :
            print("l'opération ne peut etre effectuer")
    
    # turn a lawnmower when the command is "D" or "G"
    def turn(self,direction : str):
        
       if( direction in ["D","G"]):
           self.set_orientation(self.get_oriantation_assiociated(direction))
        
    def get_oriantation_assiociated(self,direction):
        oriantation_associated = {"D":"","G":""}
        # Case when the oriention it's N
        if(self.orientation == "N"):
            # If direction is D, the associated orientation is E and for G is W
            oriantation_associated = {"D":"E","G":"W"}
            
        # Case when the oriention it's E
        elif(self.orientation == "E"):
            # If the direction is D, the associated orientation is S and for G is N
            oriantation_associated = {"D":"S","G":"N"}
            
        # Case when the oriention it's W    
        elif(self.orientation == "W"):
            # If the direction is D, the associated orientation is N and for G is S
            oriantation_associated = {"D":"N","G":"S"}
            
        # Case when the oriention it's S    
        elif(self.orientation == "S"):
            # If the direction is D, the associated orientation is W and for G is E
            oriantation_associated = {"D":"W","G":"E"}
            
        return oriantation_associated[direction]
    
    def get_coords(self) -> list:
        """ get the x,y position and the orientation like [x,y,orientation]"""
        print(self.x,self.y,self.orientation)
                
        return [self.x,self.y,self.orientation]
    
    def get_xy(self) -> list[int]:
        """ get the x,y postion of lawnmower"""
        return [self.x,self.y]
    
    def set_orientation(self,orientation):
        if(orientation in ["N","E","W","S"]):
            self.orientation = orientation
        return ''
    
    def set_x(self,x : int,gazon : Gazon):
        if(x >= 0 and x <= gazon.coords[0]):
            self.x = x
            
    def set_y(self,y : int,gazon : Gazon):
        if(y >= 0 and y <= gazon.coords[1]):
            self.y = y