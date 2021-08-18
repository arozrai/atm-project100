class atm(object):
    def __init__(self,bankMoney,cardNumber,pinNumber):
        self.bankMoney = bankMoney
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        
    
    def CashWithdrawl(bankMoney,pinNumber):
        inputtedNumber = int(input("Put in your pin number: "))
        if (inputtedNumber == pinNumber):
            withdraw = int(input("How much money will you like to withdraw: "))
            bankMoney = bankMoney - withdraw
            print("You have ", bankMoney," left")
        else:
            print("non-matching pin number")    

    def CashInput(bankMoney,pinNumber):
        inputtedNumber = int(input("Put in your pin number: "))
        if (inputtedNumber == pinNumber):
            inputure = int(input("How much money will you like to input: "))
            bankMoney = bankMoney + inputure
            print("You have ", bankMoney," left")
        else:
            print("non-matching pin number") 
    
    def BalanceEnquiry(bankMoney,cardNumber):
        inputtedCardNumber = int(input("Put in your card number: "))
        if (inputtedCardNumber == cardNumber):
            print("You have ",bankMoney," left in your bank")
        else:
            print("Non-matching card number")

user1 = atm(10000,1111111108,9268316325)

print(user1.CashWithdrawl(9268316325))
print(user1.CashInput(9268316325))
print(user1.BalanceEnquiry(1111111108))

# Example:
#     class Student(object): 
#         def __init__(self, name, age, gender, level, grades=None): 
#             self.name = name 
#             self.age = age 
#             self.gender = gender 
#             self.level = level 
#             self.grades = grades or {} 
            
#         def setGrade(self, course, grade): 
#             self.grades[course] = grade 
        
#         def getGrade(self, course):
#             return self.grades[course] 
        
#         def getGPA(self): 
#             return sum(self.grades.values())/len(self.grades) 
    
#     # Define some students 
#     john = Student("John", 12, "male", 6, {"math":3.3}) 
#     jane = Student("Jane", 12, "female", 6, {"math":3.5}) 
#     # Now we can get to the grades easily 
#     print(john.getGPA()) 
#     print(jane.getGPA())