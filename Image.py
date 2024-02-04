class Image2 :
    
    def __init__(self,name,representation,label) :

        self.name = name
        self.representation = representation
        self.label = label

    def __str__(self):
        """ Overrides #print function """
        res = "Image\n"
        res += "name: " + str(self.name) + "\n"
        res += "representation : " + str(self.representation) + "\n"
        res += "label " + str(self.label) + "\n"
        
        return res
 