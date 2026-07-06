#multiple users must be able to input their name, number of followers, verified status, and rating. The program should then print out the information for each user.

u_name=input("Enter your name: ")
followers=int(input("Enter number of followers: "))
verified=input("Is the user verified? (True/False): ")
if verified.lower() == 'true':
    verified = True
elif verified.lower() == 'false':
    verified = False
else :
    print("Invalid input for verified status. Please enter True or False.")
    exit()
rating=float(input("Enter the user's rating: "))

print(u_name, followers, verified, rating)