# Define a user class. 
class Account(object):
    self.money = money # Account balance.
    self.username = username # User name.
# Last login time.
    self.start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    self.number = number
# Deposit.
def save(self):
    self.money += self.number
    print("Saved CNY %f"%(self.number))
# Withdrawal.
def take(self):
    if self.number > self.money:
        print("Insufficient balance")
        return 0
    else:
    self.money -= self.number
    print (" Withdraw CNY %f"%(self.number))
    return 1 
# Change the password.
def update(self):
    pwd = getpass.getpass("Enter a new password：")
    sql = "update user set pwd=%s where username=%s"%(pwd, self.username)
    return sql
# Transfer.
def transfer(self):
    user = input("Please enter the transferee.")
    if self.number > self.money:
        print("Insufficient balance")
        return
    else:
        sql = "select username from user where username='%s'"%(user)
        result = con_mysql(sql)
        if result == None: 
            print ("The transferee does not exist.") 
            self.number=0
        else:
            return user
# Perform the selected operation.
def implement(self, action):
    if action == 5:
        sys.exit()
    elif action == 1:
        try:
            self.number = float (input("Please enter the deposit amount:"))
        except Exception as e:
            print("Enter a correct amount.")
        self.save()
    elif action == 2:
        try: 
            self.number = float (input("Please enter the amount to be withdrawn:"))
        except Exception as e:
            print("Enter a correct amount.")
        if self.take():
            sql = "update user set balance=%f where
username=%s"%(self.number,self.username)
            con_mysql(sql)
    elif action == 3:
        try:
            self.number = float (input("Please enter the transfer amount."))
        except Exception as e:
            print("Enter a correct amount.") 
        User = self.transfer()
        if User: 
            sql = "update user set balance=%f where username=%s"%(self.number,User) 
            con_mysql(sql)
  else:   
        self.update()
# Generate the credential after the operation.
    def voucher(self,end_time, action):
        str_action = """user:%s \n operation:%s\n Operation amount: %s\n Login time: 
                    %s\n End time: %s"""%(self.username, action_dict[action], self.number, 
self.start_time, end_time)
    with open("%s.txt"%(self.username), 'w') as f: 
    try: 
        f.write(str_action)
        except Exception as e:
            print("The credential fails to be generated. Please contact the administrator.)
        print ("Generation succeeded. Keep it safely.")
