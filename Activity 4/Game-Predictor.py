dayGame = input('Is it a day game (yes or no)?\n')
currTemp = float(input('What is the current temperature?\n'))
firstChoice = input('Is the first-choice QB playing (yes or no)?\n')

dayGame = dayGame.upper()
firstChoice = firstChoice.upper()

win = True

if(dayGame != 'YES'):
    win = False
if(currTemp >= 76):
    win = False
if(firstChoice != 'YES'):
    win = False

if(win):
    print('The Bears will win')
else:
    print('The Bears will not win')
