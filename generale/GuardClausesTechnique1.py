def getPayAmount(self):
    if self.isDead:
        result = deadAmount()
    else:
        if self.isSeparated:
            result = separatedAmount()
        else:
            if self.isRetired:
                result = retiredAmount()
            else:
                result = normalPayAmount()
    return


    # ------------------------------------------
    # GUARD Clauses Technique

    def getPayAmount(self):
        if self.isDead:
            return deadAmount()
        if self.isSeparated:
            return separatedAmount()
        if self.isRetired:
            return = retiredAmount()
        return normaPayAmount()
            
