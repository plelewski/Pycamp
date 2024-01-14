from game import Game

class MainMenu:
    def __init__(self, player_age):
        self.player_age = player_age

    def menu(self):
        while True:
            print('\n*** MENU ***')
            print('1: Lotto')
            print('2: Mini Lotto')
            print('9: wyjście')
            choice = input('Dokonaj wyboru: ')

            if choice == '1':
                game = Game(49, 6)
                game.run_game()
                print(f'Wygrałeś mając {self.player_age + game.calculate_time_to_win()} lat. Żyjesz jeszcze?')

            elif choice == '2':
                game = Game(42, 5)
                game.run_game()
                print(f'Wygrałeś mając {self.player_age + game.calculate_time_to_win()} lat. Żyjesz jeszcze?')

            elif choice == '9':
                break

            else:
                print('Niepoprawny wybór. Wybierz ponownie')

