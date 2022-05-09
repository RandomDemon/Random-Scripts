import random
import time

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def play_again():
    time.sleep(1)
    again = input("Do you want to play again? (Y/N) : ").lower()
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    print("Bye!")
	    time.sleep(1)
	    exit()

def total(hand):
    total = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        total+= 10
	    elif card == "A":
	        if total >= 11: total+= 1
	        else: total+= 11
	    else: total += card
    return total

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def print_results(dealer_hand, player_hand):
	print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
	time.sleep(1)
	print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		time.sleep(1)
		print ("Congratulations! You got a Blackjack!\n")
		time.sleep(1)
		play_again()
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)		
		time.sleep(1)
		print ("Sorry, you lose. The dealer got a blackjack.\n")
		time.sleep(1)
		play_again()

def both(dealer_hand, play_again):
    if total(player_hand) >=22 and total(dealer_hand) >=22:
        print_results(dealer_hand, player_hand)
        time.sleep(1)
        print("Both you and the dealer bust!")

def score(dealer_hand, player_hand):
	if total(player_hand) == 21:
		print_results(dealer_hand, player_hand)
		time.sleep(1)
		print ("Congratulations! You got a Blackjack!\n")
	elif total(player_hand) >=22 and total(dealer_hand) >=22:
	    print_results(dealer_hand, player_hand)
	    time.sleep(1)
	    print("Both you and the dealer bust!")
	elif total(dealer_hand) == 21:
		print_results(dealer_hand, player_hand)	
		time.sleep(1)
		print ("Sorry, you lose. The dealer got a blackjack.\n")
	elif total(player_hand) > 21:
		print_results(dealer_hand, player_hand)
		time.sleep(1)
		print ("Sorry. You busted. You lose.\n")
	elif total(dealer_hand) > 21:
		print_results(dealer_hand, player_hand)
		time.sleep(1)
		print ("Dealer busts. You win!\n")
	elif total(player_hand) < total(dealer_hand):
		print_results(dealer_hand, player_hand)
		time.sleep(1)
		print("Sorry. Your score isn't higher than the dealer. You lose.\n")
	elif total(player_hand) > total(dealer_hand):
		print_results(dealer_hand, player_hand)  
		time.sleep(1)
		print ("Congratulations. Your score is higher than the dealer. You win\n")

def game():
	choice = 0
	print ("WELCOME TO BLACKJACK!\n")
	dealer_hand = deal(deck)
	player_hand = deal(deck)
	while choice != "q":
		print ("The dealer is showing a " + str(dealer_hand[0]))
		time.sleep(1)
		print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
		blackjack(dealer_hand, player_hand)
		time.sleep(1)
		choice = input("Do you want to [H]it, [S]tand, or [F]old: ").lower()
		if choice == "h":
			hit(player_hand)
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "s":
			while total(dealer_hand) < 17:
				hit(dealer_hand)
			score(dealer_hand, player_hand)
			play_again()
		elif choice == "f":
			print ("Bye!")
			exit()
	
if __name__ == "__main__":
    game()
