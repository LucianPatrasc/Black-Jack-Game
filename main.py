import random
from art import logo


def deal_cards():
    """Returneaza o carte aleatorie din lista"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return   card

def calculate_score(cards):
    """Ia o lista de carti  si calculeaza rezultarul lor"""
    if sum(cards) == 21 and len(cards) == 2 :
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

    """Aici comparam valorile cartilor celor 2 jucatori"""
def compare(u_score, c_score):
    if u_score == c_score:
        return "EGALITATE !!!"
    elif c_score == 0:
        return "AI PIERDUT, calculatorul are BlackJack !!!"
    elif u_score == 0:
        return "Ai BlacJack ! AI CASTIGAT !!!"
    elif u_score > 21:
        return "Ai peste 21 , deci AI PIERDUT !!!"
    elif c_score > 21:
        return "Calculatorul are peste 21 , deci AI CASTIGAT!!!"
    elif    u_score > c_score :
        return " AI CASTIGAT!!!"
    else:
        return "AI PIERDUT!!!"
def play_game():
    print(logo)
    print()
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    """ Mai jos ciclul for va itera de 2 ori , 
        caracterul _ este variabila de control  ca o conventie ca aceasta nu va fi folosita
        in concluzie for va distribui 2 carti catre jucator, cat si catre calculator"""

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Cartile tale {user_cards} , punctajul curent {user_score}")
        print()
        print(f"Prima carte a calculatorului {computer_cards[0]}")
        print()
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Apasa 'd' sa mai primesti o carte sau apasa 'n' sa nu primesti : ")
            if user_should_deal == "d":
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"Cartile tale finale sunt : {user_cards}, iar punctajul final este : {user_score}")
    print()
    print(f"Cartile calculatorului sunt : {computer_cards}, iar punctajul final este :{computer_score}")
    print()
    print(compare(user_score, computer_score))
    print()

   """Ciclare condiționată: Bucla while de jos este folosită pentru a repeta anumite instrucțiuni cât timp condiția 
   specificată este adevărată. În cazul de față, condiția este verificarea dacă input-ul utilizatorului este "da".
    Această condiție determină dacă bucla va continua sau nu."""

while input("Vrei sa joci BlackJack ? scrie 'da' sau 'nu' --> ") == "da":
    print("\n" * 20)
    play_game()
