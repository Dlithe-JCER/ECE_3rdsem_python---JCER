balance = 5000.0   # initial balance

print("===== ATM MACHINE =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

# ---- Conditional Statements ----

if choice == 1:
    print("\nYour Balance: ₹", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposited Successfully!")
    print("Updated Balance: ₹", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= balance:      # nested conditional
        balance -= amount
        print("Withdrawn Successfully!")
        print("Updated Balance: ₹", balance)
    else:
        print("Insufficient Balance!")

elif choice == 4:
    print("Thank you for using ATM!")

else:
    print("Invalid Option! Please choose between 1 to 4.")
