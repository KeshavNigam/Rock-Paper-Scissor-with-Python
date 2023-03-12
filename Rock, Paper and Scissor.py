#!/usr/bin/env python
# coding: utf-8

# In[16]:


import random
comp = random.randint(0,2)
user = int(input("0 for Rock,1 for Paper and 2 for Scissor:\n "))
def check (comp,user):
    if comp == user:
        return 0
    if (comp == 1 and user == 0):
        return -1
    if (comp == 2 and user == 1):
        return -1
    if (comp == 0 and user == 2):
        return -1
    return 1
Score = check(comp,user)
print("You:",user)
print("Computer:",comp)

if(Score == 0):
    print("Its a Draw")
elif (Score == -1):
    print("You Lose")
else:
    print("You Won")

