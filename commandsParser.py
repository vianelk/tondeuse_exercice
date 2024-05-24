
class CommandParser :
    """ this class is built for read the file where are 
    the lawnmover's instructions and parse it.
    
    """
    def __init__(self,file_path : str) -> None:
        """file_path is the path of the commands file """
        # file where are the lawnmovers commands instruction
        file = open(file=file_path,mode= "r")
        line = file.readline()
        self.gazon_dimension = []
        self.coords_list = []
        self.commands_list = []
        counter = 0
        while line:
            # i remove the \n of the line
            line = (line.split("\n"))[0]
            
            # if it is the dimension of the turf << gazon >>
            if(counter == 0):
                self.gazon_dimension = [str(x) for x in line.split(" ") ]
            # if it is the coordinates of lawnmovers
            elif(counter != 0 and counter%2 != 0):
               self.coords_list.append(line.split(" "))
            
            # if it is the instructions of lawnmovers
            elif(counter != 0 and counter%2 == 0):
                
                self.commands_list.append([ x for x in line])
            
            
            line = file.readline()
            counter+=1
        file.close()
        