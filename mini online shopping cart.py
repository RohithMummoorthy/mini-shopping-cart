import datetime
import random

def generateorderid():
    return "ORD" + str(random.randint(1000,9999))
print("====MINI ONLINE SHOPPING CART SYSTEM====")

customer_id=input("Enter you customer ID :")
customer_name=str(input("Enter your Name : "))
walletbalance=float(input("Enter your Wallet Balance : "))

items=[]
price=[]

print("Enter the item Name,(or type 'done' to finish)")
while True:
    itemsname=input("Enter the item Name : ")
    if itemsname.lower()=="done":
        break
    itemprice=float(input("Enter the prices of the items : "))
    items.append(itemsname)
    price.append(itemprice)

totalprice=sum(price)


promocode=["SAVE10","SUPER20","TOP30"]
checkpromo=input("Enter the  promo code u have (if u not have one type 'no') : ")
if checkpromo.upper()=="SAVE10":
    print("The code you have applied is : SAVE10")
    dicountprice=totalprice*(10/100)
    finalprice=totalprice-dicountprice
elif checkpromo.upper()=="SUPER20":
    print("The code you have applied is : SUPER20")
    dicountprice=totalprice*(20/100)
    finalprice=totalprice-dicountprice
elif checkpromo.upper()=="TOP30":
    print("The code you have applied is: TOP30")
    dicountprice=totalprice*(30/100)
    finalprice=totalprice-dicountprice
else:
    print("No discount applicable : ")
    dicountprice=totalprice
    finalprice=dicountprice+0

time=datetime.datetime.now().strftime("%d-%m-%Y - %H-%M-%S")
if finalprice>walletbalance:
    reqamnt=-1*(walletbalance-finalprice)
    print("Insufficient Wallet Balance : ")
    print(f"You need ${reqamnt} to complete the payment")
    afterpaymentamount=0
    order_id=generateorderid()
    order_time=time
    print("="*80)
    print(" "*31,"ORDER SUMMARY"," "*31)
    print("="*80)
    print("PAYMENT FAILED DUE TO INSUFFICIENT WALLET BALANCE")
    print("REQUIED AMOUNT TO COMPLETE THE PAYMENT ",reqamnt)
    print("RECHARGE WALLET BALANCE !!!!!! TO COMPLETE THE PAYMENT ")
    print("="*80)
else:
    afterpaymentamount=walletbalance-finalprice
    print(f"Updated Bank Balance {afterpaymentamount} : ")
    order_id=generateorderid()
    order_time=time
    print("="*80)
    print(" "*31,"ORDER SUMMARY"," "*31)
    print("="*80)
    print("CUSTOMER NAME  : ",customer_name)
    print("CUSTOMER ID    : ",customer_id)
    print("ORDER ID       : ",order_id)
    print("PRICES         : ",price)
    print("TOTAL PRICE    : ",totalprice)
    print("PROMO CODE     : ",checkpromo)
    print("DISCOUNT PRICE : ",dicountprice)
    print("FINAL AMOUNT   : ",finalprice)
    print("TIME           : ",time)
    print("WALLET BALANCE : ",afterpaymentamount)
    print("THANKS FOR SHOPPING WITH US .......")
    print("PLEASE VISIT US AGAIN")
    print("="*80)































