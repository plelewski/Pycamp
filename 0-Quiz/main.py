from json import load, dump
from random import randint


class Question:
    def __init__(self, question: str, answers: list, right_answer: str):
        self.question = question
        self.answers = answers
        self.right_answer = right_answer

    def __str__(self):
        return self.question + '\n' + '\n'.join(self.answers)

    def get_right_answer(self):
        return self.right_answer


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0


class JsonFile:
    def __init__(self, filename):
        self.filename = filename
        self.output = []
        self.scores = []

    def load_questions(self) -> list:
        try:
            with open(self.filename, 'r') as file:
                questions = load(file)
                for item in questions:
                    self.output.append(
                        Question(
                            item['question'],
                            item['answers'],
                            item['right_answer']
                        )
                    )
        except FileNotFoundError:
            print('Nie ma takiego pliku. Koniec gry.')

        return self.output

    def get_old_scores(self):
        try:
            with open('scores.json', 'r') as score_file:
                self.scores = load(score_file)
        except FileNotFoundError:
            self.scores = []

    def save_score(self, player: Player):
        self.get_old_scores()
        self.scores.append({
            'player_name': player.name,
            'final_score': player.score
        })

        with open('scores.json', 'w') as score_file:
            dump(self.scores, score_file, indent=4, sort_keys=False)


class Game:
    def __init__(self, player_name: str, qlist: JsonFile):
        self.player_name = player_name
        self.qlist = qlist

    def run(self):
        player = Player(name=self.player_name)
        questions = self.qlist.load_questions()
        # ask 3 random questions
        for question_num in range(3):
            current_question = questions.pop(randint(0, len(questions) - 1))
            print(f"Pytanie {question_num + 1}: {current_question}")
            if current_question.get_right_answer() == input('Twoja odpowiedź: '):
                player.score += 1
                print('poprawna odpowiedź')
            else:
                print('odpowiedź nieprawidłowa')

        j_file.save_score(player)
        print(f'ilość poprawnych odpowiedzi: {player.score}. Wynik zapisany do pliku. Do widzenia')


if __name__ == '__main__':
    v_player_name = input('Podaj swoje imię/ksywę: ')
    j_file = JsonFile('questions.json')
    game = Game(player_name=v_player_name, qlist=j_file)
    game.run()
