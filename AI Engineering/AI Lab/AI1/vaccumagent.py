from random import random
location = 'A'
stateA = 'Clean'
stateB = 'Clean'

# idx 0: A/Clean, idx 1: A/Dirty 
# idx 2: B/Clean, idx 3: B/Dirty
mantra = ['move','clean','move','clean']

if random() < 0.2: #probability of 20%
    stateA = 'Dirty'
if random() < 0.2: #probability of 20%
    stateB = 'Dirty'

print('A is', stateA,', B is', stateB)

if location=='A':
    if stateA=='clean':
        action=mantra[0]
    else:
        action=mantra[1]
else:
    if stateB=='clean':
        action=mantra[2]
    else:
        action=mantra[3]

if location=='A':
    if action=='clean':
        print("Agent is in room A, Cleaning")
    else:
        
