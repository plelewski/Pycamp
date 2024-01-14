from mainmenu import MainMenu


class Application:
    def run(self):
        mm = MainMenu(self.get_user_data())
        mm.menu()

    @staticmethod
    def get_user_data():
        try:
            return int(input('Graczu, podaj swój wiek w latach: '))
        except ValueError:
            print('Niestety nie umiesz się bawić')
            quit()


if __name__ == "__main__":
    app = Application()
    app.run()
