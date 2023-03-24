import random

class RockPaperScissors:

    hands = ['rock', 'scissors', 'paper']
    results = {'win': 'win', 'lose': 'lose', 'draw': 'draw try again'}


    def __init__(self):
        print('start rock-paper-scissors\' ')
        self.game_ended = False

    def get_hand_name(self, hand_number):
        return self.hands[hand_number]
    

    def view_hand(self, your_hand, computer_hand):
        print('My hand is ' + self.get_hand_name(your_hand))
        print('Rival\'s hand is ' + self.get_hand_name(computer_hand))


    def get_result(self, hand_diff):
        if hand_diff == 0:
            return 'draw'
        elif hand_diff == -1 or hand_diff == 2:
            return 'win'
        else:
            return 'lose'
        
    def view_result(self, result):
        print(self.results[result])

    # validating the input for replay
    def is_valid_choice(self, choice):
        if choice == 'Y':
            return True
        elif choice == 'N':
            return True
        return False


    # argue the user to replay function when game ends
    def replay(self):
        choose = input('Replay? (Y or N): ')
        while self.is_valid_choice(choose) == False:
            choose = input('Replay? (Y or N): ')
        if choose == 'Y':
            Computer.lives = 3
            Myself.lives = 3
            self.play()
        else:
            self.game_ended = True


    def play(self):
        computer = Computer()
        myself = Myself()
        while not self.game_ended:
            while computer.lives != 0 and myself.lives != 0:
                print(f'Lives: Rival {computer.lives} / You {myself.lives}')
                computer_hand = computer.get_computer()
                my_hand = myself.my_player(self.hands)
                diff = my_hand - computer_hand
                self.view_hand(my_hand, computer_hand)
                result = self.get_result(diff)
                self.view_result(result)
                if result == 'lose':
                    myself.lives -= 1
                elif result == 'win':
                    computer.lives -= 1
            else:
                if not self.game_ended:
                    self.replay()




class Player:
    lives = 3



class Computer(Player):
    def __init__(self) -> None:
        super().__init__()

    def get_computer(self):
        return random.randint(0, 2)
    

class Myself(Player):
    def __init__(self) -> None:
        super().__init__()

    def get_player(self, hands):
        print('Input your hand')
        input_message = ''
        index = 0
        for hand in hands:
            input_message += str(index) + ':' + hand
            if index < 2:
                input_message += ', '
            index += 1
        return input(input_message)
    

    def is_hand(self, string):
        if string.isdigit():
            number = int(string)
            if number >= 0 and number <= 2:
                return True
            else:
                return False
        else:
            return False
        
    def my_player(self, hands):
        your_hand = self.get_player(hands)
        while not self.is_hand(your_hand):
            your_hand = self.get_player(hands)
        return int(your_hand)


# creating instances of game
game = RockPaperScissors()
game.play()



