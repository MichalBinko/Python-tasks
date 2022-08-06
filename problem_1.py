import random
class Password:
    #input password
    def input_password(self):
        print("Write your password.\nUse minimall 8 characters, upercase, numbers, and special character. ")
        self.__password = input()
        p.minimall(self.__password)
        p.alpha_check(self.__password)
        p.uppercase_check(self.__password)
        p.lowercase_check(self.__password)
        p.number_check(self.__password)
        p.special_check(self.__password)
        return p.mix_characters(self.__password)

        #return self.__password
    
    #check minimall 8 characters
    def minimall(self, password):
        self.__password = str(password)
        if len(self.__password) >= 8:
            return True
        else:
            print("Error. Please use more letters in your password.\nPlease try again.")
            p.input_password()    
    
    
    #alpha character check
    def alpha_check(self, password):
        self.__password = str(password)
        self._alpha_check = False
        for character in self.__password:
            if character.isalpha():
                self._alpha_check = True
                break
        
        if self._alpha_check:
            return True
        else:
            print("Error. Please use letters in your password.\nPlease try again.")
            p.input_password()
    
    #uppercase check
    def uppercase_check(self, password):
        self.__password = str(password)
        self._uppercase_check = not(self.__password.islower())
        if not self._uppercase_check:
            print("Error. Please use upper case in your password.")
            p.input_password()
        else:
            return True

    #lowercase check
    def lowercase_check(self, password):
        self.__password = str(password)
        self._lowercase_check = not(self.__password.isupper())
        if not self._lowercase_check:
            print("Error. Please use lower case in your password.")
            p.input_password()
        else:
            return True
    
    #number_character_check
    def number_check(self, password):
        self.__password = str(password) 
        self._number_character_check = False
        for character in self.__password:
            if character.isdigit():
                self._number_character_check = True
                return True
        print("Error. Please use number in your password.")
        p.input_password()
    
    #special_character_check
    def special_check(self, password):
        self.__password = str(password)
        self._special_character_check = not(self.__password.isalnum())          
        if not self._special_character_check:
            print("Error. Please use special character in your password.")
            p.input_password()
        else:
            return True
    def mix_characters(self, password):
        self.__password = str(password)
        self._mix_password = ''.join(random.sample(self.__password,len(self.__password)))
        return self._mix_password
p = Password()
print("Your password {0} is strong.".format(p.input_password()))

