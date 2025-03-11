menu={
    'pizza':50,
    'coffie':20,
    'tea':10,
    'drink':100
}
total_price=0
#greet
print("welome to our restaurant, here is our menu")
print('''
pizza:50
coffee:60
tea:10
drink:20

''')

item_1=input("Enter a first item which you want:")
if item_1 in menu:
    total_price += menu[item_1]
    print("your item is added ",item_1)
else:
    print("sorry please tell me another else")
q=input('are you want to another item(yes/no)')
if q =="yes":
    item_2=input("enter secound item:")
    total_price +=menu[item_2]
    print("your item is added",item_1,item_2)
else:
    print("ok , thanks")
print ("your total amounnt is",total_price)
