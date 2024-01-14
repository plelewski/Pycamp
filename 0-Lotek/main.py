from random import randint, sample


class Application:
    """
    :summary: check after how many times you will win the main reward
    """
    def __init__(self):
        self.output = {}

    def get_six(self):
        """
        :return:
            set: 6 pseduo random numbers
        """
        # lotto = set()
        #while len(lotto) < 6:
        #    lotto.add(randint(1, 49))

        return set(sample(range(1,50), k=6))

    def show_stats(self):
        for v_key, v_value in self.output.items():
            print(f'{v_key} : {v_value}')

        print(f"Na losy loteryjne wydałeś {self.output['Ilość losowań'] * 3:,} zł")

    def run(self):
        num_of_tries = 1
        user_numbers = set()

        while len(user_numbers) < 6:
            try:
                user_numbers.add(int(input(f'Podaj {len(user_numbers)+1} liczbę od 1 do 49: ')))
            except ValueError:
                print('To nie jest liczba całkowita')

        self.output['Twoje liczby'] = user_numbers

        while self.get_six() != user_numbers:
            num_of_tries += 1
            if num_of_tries % 100000 == 0:
                print(f'Za nami już {num_of_tries:,} losowań i nadal nie trafiłeś szóstki')

        self.output['Ilość losowań'] = num_of_tries

if __name__ == "__main__":
    app = Application()
    app.run()
    app.show_stats()


