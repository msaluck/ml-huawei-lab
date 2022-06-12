def welcome(): 
    print(' *'*15)
    print(" %s%30s"%("*","*"))
    print(" %s Welcome to the Treasury Management System %5s"%("*","*"))
    print(" %s%30s"%("*","*"))
    print(' *'*15)
    try: 
        action = input("Please select the operation: 1. Deposit 2. Withdraw 3. Transfer 4. Change
Password 5. Exit:")
        action = int(action)
    except Exception as e: 
        print("warn: Please enter a correct operation command.")
        return -1
    if action not in action_dict: 
    print("warn: Please perform a correct operation.")
    return -1
    return action
# Test the welcome method:
action = welcome() 
action

















