import random
from colorama import init, Fore, Style
init(autoreset=True)

def player_choice():
    choice = ''
    while choice not in ['Rock', 'Paper', 'Scissors']:
        choice = input(Fore.GREEN + "Choose Rock, Paper, or Scissors: " + Style.RESET_ALL).capitalize()
    return choice

def ai_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def win_conditions(player, ai):
    if player == ai:
        return "tie"
    elif (player == 'Rock' and ai == 'Scissors') or \
         (player == 'Paper' and ai == 'Rock') or \
         (player == 'Scissors' and ai == 'Paper'):
        return "player"
    else:
        return "ai"

def play_round(name):
    player = player_choice()
    ai = ai_choice()
    result = win_conditions(player, ai)
    
    print(Fore.CYAN + f"\n{name}, you chose {player}. AI chose {ai}.")
    
    if result == "tie":
        print(Fore.YELLOW + "It's a tie!")
        return 0, 0  # No score change
    elif result == "player":
        print(Fore.GREEN + "You win this round!")
        return 1, 0  # Player gets 1 point
    else:
        print(Fore.RED + "AI wins this round!")
        return 0, 1  # AI gets 1 point

def play_game():
    print(Fore.MAGENTA + "\n=== Rock Paper Scissors ===")
    name = input(Fore.YELLOW + "Enter your name: " + Style.RESET_ALL).capitalize()
    
    while True:
        player_score = 0
        ai_score = 0
        
        while player_score < 3 and ai_score < 3:
            print(Fore.BLUE + f"\nScore: {name} {player_score}-{ai_score} AI")
            p_points, a_points = play_round(name)
            player_score += p_points
            ai_score += a_points
        
        print(Fore.MAGENTA + f"\nFinal Score: {name} {player_score}-{ai_score} AI")
        if player_score == 3:
            print(Fore.GREEN + f"\n🎉 {name} wins the game! 🎉")
        else:
            print(Fore.RED + "\n😢 AI wins the game! 😢")
        
        replay = input(Fore.CYAN + "\nPlay again? (y/n): " + Style.RESET_ALL).lower()
        if replay != 'y':
            print(Fore.MAGENTA + "\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()