class enumValidation:
    def assignementRole(role:str)->bool:
        return role in ["Admin","Worker","Manager"]