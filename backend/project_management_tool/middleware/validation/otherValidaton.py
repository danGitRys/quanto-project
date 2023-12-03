class otherValidation:

    def can_convert_to_int(s:str)->bool:
        try:
            convert = int(s)
            return True
        except:
            return False
    
    def can_convert_to_float(s:str)->bool:
        try:
            convert = float(s)
            return True
        except:
            return False
    
    def validPauseInteger(s:str)->bool:
        if(otherValidation.can_convert_to_int(s)):
            if(int(s)>=0):
                return True
            else:
                return False
        else:
            return False
   
