import random
from sty import fg

banana = [fg(226) + '         ' + fg.rs,
          fg(226) + '      #  ' + fg.rs,
          fg(226) + '     ##  ' + fg.rs,
          fg(220) + '    ##   ' + fg.rs,
          fg(220) + '  ##     ' + fg.rs,
          fg(226) + '         ' + fg.rs]

jahudka = [fg(111) + '         ' + fg.rs,
            fg(34) + '    ##   ' + fg.rs,
           fg(196) + '   ####  ' + fg.rs,
           fg(196) + '   ####  ' + fg.rs,
           fg(196) + '    ##   ' + fg.rs,
           fg(111) + '         ' + fg.rs]

sedmicka = [fg(111) + '         ' + fg.rs,
             fg(88) + '   ####  ' + fg.rs,
            fg(124) + '      #  ' + fg.rs,
            fg(160) + '     #   ' + fg.rs,
            fg(196) + '    #    ' + fg.rs,
            fg(111) + '         ' + fg.rs]

sloty_val = []
while len(sloty_val) < 3:
    sloty_val.append(random.randint(1, 1000))

for i in range(len(sloty_val)):

    if sloty_val[i] < 900:
        sloty_val[i] = banana

    elif sloty_val[i] > 900 and sloty_val[i] < 990:
        sloty_val[i] = jahudka
    else:
        sloty_val[i] = sedmicka

print(sloty_val)
