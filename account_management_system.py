class webiste_owner:
    def __init__(self):
        self.companies=[]
    def add_company(self,company):
        self.companies.append(company)
        print(self.companies)
    def get_info(self,name):
        for company in self.companies:
            if company.name==name:
                print(company.name)    
class company:
    def __init__(self,name):
        self.name=name
    def permission(self,income,balance):
        self.income=income
        self.balance=balance
        if self.balance>self.income:
            return False
        else:
            return True  
    def info(self,account):
        self.account=account
        self.account.reports()        
class account:
    def __init__(self,company,income):
        self.company=company
        self.income=income
    def manage_income(self,balance):
        self.income=self.income+balance
        print("balance is inserted successfully ")
    def manage_expense(self,balance):
        if self.company.permission(income,balance) is True :
            self.income=self.income-balance
            print("balance is deducted from your company account")
        else:
            print("Can not perform this operation")
    def reports(self):
        print( self.income)

while True: 
    n=int(input("enter the role \n 1. company owner \n 2.website owner \n 3.close "))

    if n==1:
        a=input("please create a company \nyou need to enter company name  ")
        
        comp1=company(a)
        w1=webiste_owner()
        w1.get_info(a)
        w1.add_company(comp1)
        # w1.get_info()
        income=int(input(f"enter total income"))
        ans=True
        while ans:
            b=int(input("1. manage income \n2. manage expense \n3. report \n4. close" ))
            if b==1:
                acc1=account(comp1,income)
                amount=int(input("enter amount ")) 
                acc1.manage_income(amount)
            elif b==2:
                acc1=account(comp1,income)
                amount=int(input("enter amount"))
                acc1.manage_expense(amount)
            elif b==3:
                acc1.reports()
            elif b==4:
                ans= False
    elif n==2:
        w1=webiste_owner()   
    elif n==3:
        break     
    else:
        print("invalid number please enter the number again ")