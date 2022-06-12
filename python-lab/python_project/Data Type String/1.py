# Step 2Immutability of strings:
S = 'python' # Assign value "python" to variable S.
S[0] = 'Z' # The program is abnormal.
S1 ='Z'+S[1:] # New string Zython is generated and assigned to S1.
print("S:%s, S1:%s"%(S, S1))# Output: S:python, S1:Zython
