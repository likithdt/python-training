# product_price = 100
# delivery_fee = 10

# total=product_price + delivery_fee
# print("Total amount to be paid: ", total)

######################################################

# a=10
# b=3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)
# print(a//b)

######################################################

# followers = 100
# followers += 1
# print(followers)

######################################################

# saved_password = "123456@abcd"
# entered_password = "123456@abcd"

# print(saved_password == entered_password)

######################################################

# balance = 500
# pin_correct = True
# if balance >= 1000 and pin_correct:
#     print("You can withdraw money")
# else:
#     print("Failed")

######################################################

#billing system
# product_name = input("Enter the product name: ")
# product_price = float(input("Enter the product price: "))
# quantity = int(input("Enter the quantity: "))
# delivery_fee = float(input("Enter the delivery fee: "))
# discount = float(input("Enter the discount percentage: "))

# total = (product_price * quantity) + delivery_fee
# discount_amount = total * (discount / 100)
# final_total = total - discount_amount
# print("Total amount to be paid: ", final_total)

######################################################

password = input("Enter your password: ")

if password == "123456@abcd":
    print("welcome")
else:
    print("wrong password")