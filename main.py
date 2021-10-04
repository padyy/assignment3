''' Coding Bootcamp - Assigment 
-Title:  Assignment 3 Brief
-Last name : Pantelakis
-First Name: Ioannis
-Advisors: Tyrovola Sarantia 
-Python ver:3.9.2
-win: win10 64bit

'''

''' tshirt1= T_Shirt_payment('red','xs','wool','credit',PaymentCredit())
print(tshirt1.executeStrategy())
tshirt2= T_Shirt_payment('yellow','s','polyester','bank',PaymentBank())
print(tshirt2.executeStrategy())
tshirt3= T_Shirt_payment('blue','xxl','linen','cash',PaymentCash())
print(tshirt3.executeStrategy())'''
from u_i import User_Interface
from context import T_Shirt_payment
from strategy import PaymentCredit,PaymentBank,PaymentCash


def main():
    ch=None
    tshirt_list = []
    while ch!=2:
        ch=ch=User_Interface.Menu() #Menu fucntion call and choice for next step
        if ch == 1:
            User_Interface.tshirt_buy(tshirt_list , top=True,)
        list_len= len(tshirt_list)
        print(f"You have just bought {list_len} T-shirts with the following characteristics:\n\n ")  
        for tshirt in tshirt_list: #for loop for printing all the t-shirts and check what strategy plan to apply depending on user's payment method choice.
            if tshirt.t_payment == 'credit' :
                tshirt.strategy = PaymentCredit() #apply the right strategy plan
                print(tshirt.executeStrategy()) # call the right strategy plan
            elif tshirt.t_payment == 'bank' :               
                tshirt.strategy = PaymentBank()
                print(tshirt.executeStrategy())
            else:
                tshirt.strategy = PaymentCash()
                print(tshirt.executeStrategy())
            print('\n\n')
    User_Interface.exitprogram()
    






    

if __name__=='__main()__':
    main()

main()   
