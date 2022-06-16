import time
# time.time(): Obtain the current timestamp.
time_now = time.time()
print("Timestamp:",time_now) 
# time.localtime(): Obtain the time tuple.
localtime = time.localtime(time_now) 
print("The local time is:", localtime) 
# time.asctime(): Obtain formatted time. 
localtime = time.asctime(localtime)
print("The local time is:", localtime) 
#time.strftime(format[, t]): Receive the time tuple and return the local time expressed in a readabl
# string, in the format specified by the format parameter.
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))






