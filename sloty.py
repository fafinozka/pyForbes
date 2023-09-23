import random

sloty_val = []
while len(sloty_val) < 3:
    sloty_val.append(random.randint(1, 1000))

for i in range(len(sloty_val)):

    if sloty_val[i] < 900:
        sloty_val[i] = "pears"

    elif sloty_val[i] > 900 and sloty_val[i] < 990:
        sloty_val[i] = "apples"
    else:
        sloty_val[i] = "cherries"

print(sloty_val)