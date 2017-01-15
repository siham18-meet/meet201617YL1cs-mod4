from rectangle import Rectangle

class Square (Rectangle):
    
    def  __init__ (self,height):
       super(Square,self).__init__(height,height)
       
    def set_height(self,new_height):
        super(Square, self).set_length(new_height)
        super(Square,self).set_height(new_height)

    def set_length(self,new_length):
        super(Square, self).set_height(new_length)
        super(Square,self).set_length(new_length)

        

    
       
       
    
