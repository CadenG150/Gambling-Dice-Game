from random import randint
import os
repeat = True
def startingwelcome():
	os.system("clear")
	print("Welcome To The Dice Game!")
	print("You Choose A Range For A Random Number, Wager, And Select What You Think The Number Will Be!")
	print("The Payout Could Be Huge, But Be Careful!  You Can Lose!")
	print("Press Enter To Start!")
	input()
	os.system("clear")
	balance = 500
	saveFile = open("Balance.txt", "w")
	saveFile.write(str(balance))
	saveFile.close()
	rangesystem()

def realwelcome():
	os.system("clear")
	print("Welcome To The Dice Game!")
	print("You Choose A Range For A Random Number, Wager, And Select What You Think The Number Will Be!")
	print("The Payout Could Be Huge, But Be Careful!  You Can Lose!")
	reset = input("Would You Like To Reset Your Money? Y / N: ")
	if reset == "Y":
		saveFile = open("Balance.txt", "w")
		saveFile.write("500")
		saveFile.close()
		os.system("clear")
		rangesystem()
	elif reset == "y":
		saveFile = open("Balance.txt", "w")
		saveFile.write("500")
		saveFile.close()
		os.system("clear")
		rangesystem()
	elif reset == "N":
		os.system("clear")
		rangesystem()
	elif reset == "n":
		os.system("clear")
		rangesystem()
	else:
		print("Invalid Answer!")

def wagerthemoney(rangechoice, payback, balance):
	stringbalance = str(balance)
	print("You Have A Balance Of " + stringbalance)
	wager = input("How Much Do You Want To Wager? ")
	try:
		realwager = int(wager)
	except ValueError:
		print("NO!")
		input()
		os.system("clear")
		wagerthemoney(rangechoice, payback, balance)
	if realwager > int(balance):
		print("\nYou Don't Have That Kind Of Cash!  Try Again!")
		wagerthemoney(rangechoice, payback, balance)
	elif realwager < 10:
		print("\nCome On Man!  Bet At Least 10!")
	elif realwager > 10 & realwager < int(balance):
		print("Wager Accepted!\n")
		os.system("clear")
		diceplayer(rangechoice, payback, realwager, balance)
	else:
		print("\nThat Is Not A Valid Wager!")

def diceplayer(rangechoice, payback, realwager, balance):
	numberchoice = input("What Do You Think The Number Is Going To Be? ")
	if numberchoice == number:
		print("Correct! You Win " + str(realpayback) + " Dollars!")
		realpayback = realwager * payback
		balance = int(balance) + realpayback
		open("Balance.txt", "w").close()
		saveFile = open("Balance.txt", "w")
		saveFile.write(str(balance))
		saveFile.close()
		saveFile = open("StartOrNot.txt", "w")
		saveFile.write("NO")
		saveFile.close()
		input()
		realwelcome()
	else:
		realpayback = realwager * payback
		print("Incorrect!  You Lose " + str(realpayback) + " Dollars!")
		balance = int(balance) - realpayback
		open("Balance.txt", "w").close()
		saveFile = open("Balance.txt", "w")
		saveFile.write(str(balance))
		saveFile.close()
		saveFile = open("StartOrNot.txt", "w")
		saveFile.write("NO")
		saveFile.close()
		input()
		realwelcome()


def rangesystem():
	balance = open("Balance.txt", "r").read()
	print("Choose Your Range For The Random Number")
	rangechoice = input("Range Options: \n 1) 1-10 (1x Your Wager) \n 2) 1-50 (2x Your Wager)\n 3) 1-100 (3x Your Wager)\n ")
	if rangechoice == "1":
		payback = 1
		os.system("clear")
		wagerthemoney(rangechoice, payback, balance)
	elif rangechoice == "2":
		os.system("clear")
		payback = 2
		wagerthemoney(rangechoice, payback, balance)
	elif rangechoice == "3":
		os.system("clear")
		payback = 3
		wagerthemoney(rangechoice, payback, balance)
	else:
		print("Not A Valid Range!")
	input()


while repeat:
	startorno = open("StartOrNot.txt", "r").read() 
	number = randint(1,6)
	if startorno == "YES":
		startingwelcome()
	elif startorno == "NO":
		realwelcome()
	else:
		print("ERROR")