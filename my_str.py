#FIX THE LINE BELOW
class MyStr(str):
    
    def exclaim(self,num):
        #return str+"!"*num
        return self+'!'*num

    def replace(self, take_out, use_this):
        '''
    self.take_out= take_out
        self.use_this= use_this
        CAP= MyStr("HhHhHh")
        CAP.replace('h','l')
        return CAP
        '''
        """
        Override the replace method of string.
        The new replace method is case-insensitive;
        otherwise, it behaves the same as str.replace.
        Example:
        >>> test=MyStr('aAaA')
        >>> test.replace('a','b')
        bbbb

        :param take_out: the substring that will be replaced
        :param use_this: the substring that will be used in place of take_out

        :returns: a new string with replacement complete
        """
        #################
        #Make this method work in the way described in
        #the block comment above.
        #Hints:
        # 1. Remember that self is a MyStr object,
        #    and a MyStr object is also a str
        # 2. The following str methods will be helpful:
        #       replace, lower, and upper
        # 3. There are multiple solutions, but you can
        #       do this in as little as 1 line.
        #YOUR CODE BELOW:
        #################
        
        return super (MyStr,self).replace (take_out, use_this)
    
        
