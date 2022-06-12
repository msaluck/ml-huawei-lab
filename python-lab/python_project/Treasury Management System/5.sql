# Define the system startup function.
def run():
    action = welcome()
    user_account.implement(action)
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sql = """ 
    update user set balance=%f,start_time='%s',end_time='%s' where username='%s'
    """%(user_account.money, user_account.start_time,end_time,user_account.username)
    con_mysql(sql)
    user_account.voucher(end_time, action)








