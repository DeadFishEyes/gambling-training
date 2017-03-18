import os
import time
import random

os.system('color 0a')

diamonds = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
hearts = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
spades = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']
clubs = ['A', 'K', 'Q', 'J', '2', '3', '4', '5', '6', '7', '8', '9', '10']

dice = [1, 2, 3, 4, 5, 6]


bacc_deck = diamonds + hearts + spades + clubs
bljk_deck = diamonds + hearts + spades + clubs
random.shuffle(bacc_deck)
random.shuffle(bljk_deck) # shuffles two.

def one():
	one =  '''
#########
#       #
#   O   # 
#       #
#########
'''
	return one

def two():
	two =  '''
#########
# O     #
#       # 
#     O #
#########
'''
	return two

def three():
	three =  '''
#########
# O     #
#   O   # 
#     O #
#########
'''
	return three

def four():
	four =  '''
#########
# O   O #
#       # 
# O   O #
#########
'''
	return four

def five():
	five =  '''
#########
# O   O #
#   O   # 
# O   O #
#########
'''
	return five

def six():
	six =  '''
#########
# O   O #
# O   O # 
# O   O #
#########
'''
	return six

os.system('cls')

dices = [one(), two(), three(), four(), five(), six()]

def bljk(card_num):
	print "\t[",
	print random.choice(bljk_deck),
	for i in range(int(card_num)-1):
		print '\t'+str(random.choice(bljk_deck)),
	print "]"


def bacca():
	random.shuffle(bacc_deck)
	z = random.choice(bacc_deck)
	return z

def check_val_bacc(num):
	if num == 'A':
		val = 1
	elif num == 'K':
		val = 0
	elif num == 'Q':
		val = 0
	elif num == 'J':
		val = 0
	elif num == '10':
		val = 0
	else:
		val = int(num)

	return val

def dice():
	random.shuffle(dices)
	a = random.choice(dices)
	return a



print '''
+--------------------------------+
|                                |
|                                |
|      Addition Techniques!      |
|          Mauri Vanoro          |
|                                |
|                                |
+--------------------------------+
'''

print "[1] BlackJack"
print "[2] Baccarat"
print "[3] Dice"
print "[4] Exit"

ans = raw_input('>>> ')
if int(ans) == 1:
	print "\n\nHow many cards?"
	cards_maniness = raw_input('>>> ')
	print "Delay?"
	delay = raw_input('>>> ')
	print "Loops?"
	loops = raw_input('>>> ')
	s = int(loops)
	while s > 0:
		for y in range(int(loops)):	
			bljk(cards_maniness)
			time.sleep(int(delay))
		delay =int(delay)
		delay = delay - 1
	
elif int(ans) == 2:
	print "\n\nDelay?"
	delay = raw_input('>>> ')
	print "How many cards? [2] or [3]?"
	cardz = raw_input('>>> ')
	print "Loops?"
	loops = raw_input('>>> ')
	s = int(loops)
	cardz = int(cardz)

	if cardz == 2:
		while s > 0:
			for z in range(int(loops)):
				x1 = bacca()
				x2 = bacca()
				print "[" + str(x1) + '\t'  + str(x2) + ']'
				value1 = check_val_bacc(x1)
				value2 = check_val_bacc(x2)
				time.sleep(float(delay))
				print "[" + str(value1) + '\t' + str(value2) + ']\n\n'
		delay = int(delay)
		delay = delay - 1

	elif cardz == 3:
		while s > 0:
			for z in range(int(loops)):
				x1 = bacca()
				x2 = bacca()
				x3 = bacca()
				print "[" + str(x1) + '\t' + str(x2) +  '\t'+str(x3)+']'
				value1 = check_val_bacc(x1)
				value2 = check_val_bacc(x2)
				value3 = check_val_bacc(x3)
				time.sleep(float(delay))
				print "[" + str(value1) + '\t' + str(value2) +  '\t'+str(value3) + ']\n\n'
		delay = int(delay)
		delay = delay - 1

elif int(ans) == 3:

	print "\n\nHow many dice/s?"
	dice_maniness = raw_input('>>> ')
	print "Delay?"
	delay = raw_input('>>> ')
	print "Loops?"
	loops = raw_input('>>> ')
	s = int (loops)

	while s > 0:
		for z in range(int(loops)):
			for s in range(int(dice_maniness)):
				print dice(),
			time.sleep(float(delay))
			print "_________\n"
	delay = int (delay)
	delay = delay -1
elif ans == '4':
	os.system('exit')