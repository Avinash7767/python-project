#ATM
a='''
1.credit
2.Debit
3.Mini statement
4.exit
'''
name="optimus"
password="123"
user_name=input("Enter the user Name:")
passwords=input("Enter the password")
Amount=10000
if name==user_name and passwords==password:
    while True:
        print(a)
        option=int(input("Enter the option:"))
        if option==1:
            credit_amount=float(input("Enter the amount:"))
            print("Amount after credit",Amount+credit_amount)
        elif option==2:
            debit_amount=float(input("Enter the Amount:"))
            print("Amount after debit:",Amount-debit_amount)
        elif option==3:
            print(" ###Mini statement ### Amount:",Amount)
        elif option==4:
         break
else:
    print("incorrect")
    
    
    
