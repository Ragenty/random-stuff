import random

class Player:
    def __init__(self, name, money, clothing_items):
        self.name = name
        self.money = money
        self.clothing_items = clothing_items

    def remove_clothing(self):
        if self.clothing_items:
            item = random.choice(self.clothing_items)
            self.clothing_items.remove(item)
            print(f"{self.name} removes {item}.")

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in range(2, 11):
                self.cards.append(Card(suit, str(rank)))
            for rank in ['Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(suit, rank))
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

def calculate_total(hand):
    total = 0
    num_aces = 0
    for card in hand:
        if card.rank.isdigit():
            total += int(card.rank)
        elif card.rank in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            num_aces += 1
            total += 11
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

def play_blackjack():
    print("Welcome to Strip Blackjack!")
    name = input("What's your name? ")
    money = int(input("How much money are you starting with? "))
    clothing_items = ['shirt', 'pants', 'underwear', 'socks']
    player = Player(name, money, clothing_items)

    while True:
        print(f"\n{player.name}, you have ${player.money}.")
        bet = int(input("How much do you want to bet? "))
        if bet > player.money:
            print("You don't have enough money!")
            continue

        deck = Deck()
        player_hand = [deck.deal_card(), deck.deal_card()]
        dealer_hand = [deck.deal_card()]

        print("\nYour hand:")
        for card in player_hand:
            print(card)
        print("\nDealer's hand:")
        print(dealer_hand[0])

        while True:
            total_player = calculate_total(player_hand)
            if total_player == 21:
                print("You got 21!")
                break
            action = input("Do you want to hit or stand? ").lower()
            if action == 'hit':
                player_hand.append(deck.deal_card())
                print("\nYour hand:")
                for card in player_hand:
                    print(card)
                total_player = calculate_total(player_hand)
                if total_player > 21:
                    print("Bust! You lose and remove an article of clothing.")
                    player.remove_clothing()
                    player.money -= bet
                    break
            elif action == 'stand':
                print("You stand.")
                break
            else:
                print("Invalid action! Please enter 'hit' or 'stand'.")

        if total_player <= 21:
            print("\nDealer's turn:")
            while calculate_total(dealer_hand) < 17:
                dealer_hand.append(deck.deal_card())
            print("\nDealer's hand:")
            for card in dealer_hand:
                print(card)
            total_dealer = calculate_total(dealer_hand)

            if total_dealer > 21:
                print("Dealer busts! You win and can choose to remove an article of the dealer's clothing.")
                player.money += bet
            elif total_dealer > total_player:
                print("Dealer wins.")
                player.money -= bet
            elif total_dealer < total_player:
                print("You win!")
                player.money += bet
            else:
                print("It's a tie!")

        if player.money <= 0:
            print("You're out of money! Game over.")
            break
        play_again = input("\nDo you want to play again? (yes/no) ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play_blackjack()