
class jsonUpdateFormValidation:
    
    def assignment(keys)->bool:
        valid:bool = True
        for key in keys:
            if key not in ["fk_project","fk_employee","role"]:
                return False
        return valid
        

