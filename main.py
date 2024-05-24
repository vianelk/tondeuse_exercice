# THIS IS IS DONE BY VIANEL KONG FOR PUBLICIS

from tondeuse import Tondeuse
from commandsParser import CommandParser
from gazon import Gazon

def main():
    
    tondeuses : list[Tondeuse] = []
    instructions_parser = CommandParser("./data/commands.txt")
    gazon_x,gazon_y = instructions_parser.gazon_dimension
    my_gazon = Gazon(int(gazon_x),int(gazon_y))
    tondeuses_coords = instructions_parser.coords_list
    instructions_list = instructions_parser.commands_list
    
    # init all the lawnmovers
    for coords in tondeuses_coords :
        x, y, orientation = coords
        
        tondeuses.append(Tondeuse(int(x),int(y),orientation))
        
    # move all the lawnmovers
    for i in range(len(instructions_list)):
        
        print("".join(instructions_list[i]))
        
        for instruction in instructions_list[i] :
            
            tondeuses[i].control(instruction,my_gazon)
        
    tondeuses[0].get_coords()
    tondeuses[1].get_coords()
    
        
    
    
    pass
    
    
if __name__ == "__main__" :
    main()
