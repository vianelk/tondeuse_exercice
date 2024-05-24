
class CommandParser :
    def __init__(self,file_path) -> None:
        file = open(file=file_path,mode= "r")
        line = file.readline()
        self.gazon_dimension = []
        self.coords_list= []
        self.commands_list = []
        counter = 0
        while line:
            line = (line.split("\n"))[0]
            print(line)
            # if is the dimension of the turf << gazon >>
            if(counter == 0):
                self.gazon_dimension = [str(x) for x in line.split(" ") ]
            # 
            elif(counter != 0 and counter%2 != 0):
               self.coords_list.append(line.split(" "))
            
            #
            elif(counter != 0 and counter%2 == 0):
                
                self.commands_list.append([ x for x in line])
            
            
            line = file.readline()
            counter+=1
        file.close()
        
        pass