import time
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sent_tokenize, word_tokenize, pos_tag
import numpy as np
import sys

 
def sentiment_anal(sentiment):
	sentiment = sent_tokenize(sentiment)

	sid = SentimentIntensityAnalyzer()
	sentiment_list = []
	sentiment_list = np.array(sentiment_list, dtype = np.float32)
	 
	## calculate sentiment value of input sentences
	for sentence in sentiment:
	     ss = sid.polarity_scores(sentence)
	     ## make the values into list
	     temp_list = list(ss.values())[3]
	     sentiment_list = np.append(sentiment_list, temp_list)
	         
	## calculate the average of sentiment
	a = np.mean(sentiment_list)

	normal_day = ["It seems like you had a normal day!", "Sometimes, a day with no big 'specials' is the best day!", 
	"An exquisite dessert will make your day better!"]
	great_day = ["Looks like someone was having a good day! :)", "You seems to have a good time! Hope you have another good day tomorrow!!", 
	"I also feel good when you are happy."]
	bad_day = ["Tomorrow will be a better day!! I know it. I just do. :)", 
	"Seems like you had a bad day :( \nA little hug will make you feel better!", 
	"How about some good music to cheer you up! \nAsk Gieun for some music :)"]

	print("\n\nAccording to my calculation, your emotion index is")
	time.sleep(1)
	print("\n*")
	time.sleep(1)
	print("\n*")
	time.sleep(1)
	print("\n*")
	time.sleep(1)
	print("\n\n\n", a, "\n\n\n")

	if a > -0.35 and a < 0.35:
		print(random.choice(normal_day))
	elif a >= 0.35:
		print(random.choice(great_day))
	elif a <= -0.35:
		print(random.choice(bad_day))



####################################################################################################################
####################################################################################################################



greeting_words = ("Hello there!", "Hi!!!!! (In a very high voice)", "Hey hey hey~~", 
	"Sup.", "Greetings :)", "Nice to meet you ~.~", "hellooo~ :)", "Hey. (With a sexy voice)")

print("\n\n\n\n", random.choice(greeting_words))
time.sleep(1)

## introducting the program
print("\n\n\n\n******\n******", 
	"\nI'm a program designed to deliver Gieun's words.", 
	"\nI'll deliver Gieun's words, corresponding to your input!! Fascinating, isn't it?",
	"\nHowever, bear in mind that I'm not that smart, so you'll have to tell me nice and easy.",
	"\nIf you do not want to proceed, just close the screen. \nOr, you could just jump off the window...",
	"\nBy, Gieun", 
	"\n******\n******",
	"\n\n\n")

time.sleep(3)

print("If you want to prceed, type 'Y'. If not, type'N'.")
########## proceed or not ############
proceed = input("Type your choice: ")

if proceed == 'Y':
	print("\n\nGreat!\n\n")
elif proceed == 'N':
	print("\n\nOh well...\n\n")
	sys.exit()
else:
	print("\n\nEXIT\n\n")
	sys.exit()
########################################

time.sleep(1)

######################### granting access ######################
password = ""
print("\n\nBefore we move on, I have to know if you are 'the one' I'm looking for.", 
	"\nPlease enter your name.",
	"\n\n")
while password.lower() != 'queen of wrath':
	password = input("INPUT NAME: ")
	if password.lower() == 'queen of wrath':
		print("\n*\n*\n*", "Welcome, Yeonjung. I've been waiting for you :)", "\n\nHere's a lovely rose. @)---'--,----")
	else:
		print("Access denied.")

########################################
time.sleep(1)

print("\n\n")
#################################  doing sentiment analysis  ##############################
end = "Y"
while end == 'Y':
	sentiment = input("How was your day? \n\n(You can type anyword or any sentence you want.) : ")
	sentiment_anal(sentiment)
	print("\n\n\nWould you like to try one more time? [Y/N]")
	end = input("\n\nTYPE HERE: ")

print("\n\nBYE!!")
sys.exit()

#####################################################################################################