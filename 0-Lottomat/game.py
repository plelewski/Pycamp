from random import sample
from math import ceil

class Game:
    def __init__(self, max_num: int, how_many_num: int):
        self.max_num = max_num
        self.how_many_num = how_many_num
        self.hits_three = 0
        self.hits_four = 0
        self.hits_five = 0
        self.is_done = False
        self.num_of_draws = 0
        self.drawn_numbers = set()
        self.user_numbers = set()

    def run_game(self):
        self.get_user_numbers()
        self.draw_numbers()

    def get_user_numbers(self):
        while len(self.user_numbers) < self.how_many_num:
            try:
                self.user_numbers.add(int(input(f'Podaj {len(self.user_numbers) + 1} liczbę od 1 do {self.max_num}: ')))
            except ValueError:
                print('To nie jest liczba całkowita')

    def draw_numbers(self):
        while not self.is_done:
            self.num_of_draws += 1
            self.drawn_numbers = set(sample(range(1, self.max_num + 1), k=self.how_many_num))
            self.check_winnings()

    def check_winnings(self):
        if self.num_of_draws % 500000 == 0:
            print(f'Za nami już {self.num_of_draws:,} losowań i nadal nie trafiłeś szóstki')
        if self.drawn_numbers == self.user_numbers:
            self.is_done = True
            self.show_stats()
        elif len(self.user_numbers & self.drawn_numbers) == 5:
            self.hits_five += 1
        elif len(self.user_numbers & self.drawn_numbers) == 4:
            self.hits_four += 1
        elif len(self.user_numbers & self.drawn_numbers) == 3:
            self.hits_three += 1

    def show_stats(self):
        print(f'\n *** Oto Twoje wyniki ***')
        print(f'Aby wygrać główną nagrodę musiałeś zagrać {self.num_of_draws} razy')
        print(f'Suma jaką wydałeś {self.num_of_draws * 3:,}\n')
        print(f'Trafiłeś {self.hits_three} trójek')
        print(f'Trafiłeś {self.hits_four} czwórek')
        if self.how_many_num == 6:
            print(f'Trafiłeś {self.hits_five} piątek')
            print(f'... no i oczywiście szóstkę :)')
        else:
            print(f'... no i oczywiście piątkę :)')

    def calculate_time_to_win(self):
        """

        :return:
            :int: number of years in conditions: 4 draws multiple 52 weeks
        """
        return ceil(self.num_of_draws / (4 * 52))
