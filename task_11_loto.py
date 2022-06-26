from random import randint
import time

def generate_uniq_number(count, min_num, max_num):
    if count > max_num - min_num + 1:
        raise ValueError('Неправильно введенные параметры')
    else:
        out = []
        while len(out) < count:
            new_num = randint(min_num, max_num)
            if new_num not in out:
                out.append(new_num)
        return out

class Card:
    def __init__(self):
        self.__cells = 9
        self.__num_in_line = 5
        self.__line = 3
        self.__empty_num = 0
        self.__cross_num = -1
        self.__data = []# список из 15 случайных чисел и 12 нулей

        count_nums = self.__num_in_line * self.__line
        nums = generate_uniq_number(count_nums, 1, 90)
        for i in range(0, self.__line):
            temp_num = sorted(nums[self.__num_in_line * i:self.__num_in_line * (i + 1)])
            empty_num_count = self.__cells - self.__num_in_line
            for j in range(0, empty_num_count):
                index = randint(0, len(temp_num))
                temp_num.insert(index, self.__empty_num)
            self.__data += temp_num

    def __str__(self):
        limiter = '--------------------------'
        out = limiter + '\n'
        for i, num in enumerate(self.__data):
            if num == self.__empty_num:
                out += '  '
            elif num == self.__cross_num:
                out += ' _'
            elif num < 10:
                out += f' {str(num)}'
            else:
                out += str(num)
            if (i + 1) % self.__cells == 0:
                out += '\n'
            else:
                out += ' '
        return out + limiter

    def __contains__(self, item):
        return item in self.__data

    def cross_num(self, num):
        for index, item in enumerate(self.__data):
            if item == num:
                self.__data[index] = self.__cross_num
                return

    def closed(self):
        return set(self.__data) == {self.__empty_num, self.__cross_num}

class Game:
    def __init__(self):
        self.__usercard = Card()
        self.__computercard = Card()
        self.__numkegs = 90
        self.__kegs = generate_uniq_number(self.__numkegs, 1, 90)
        self.complications = None

    @property
    def play(self):
        while True:
            try:
                self.complications = int(input('Введите время на ход в секундах - 4(hard), 6(medium), 8(easy): '))
            except ValueError:
                print('Введено не число')
            else:
                if self.complications not in (4, 6, 8):
                    print('Введено неправильное число')
                else:
                    break
        while True:
            keg = self.__kegs.pop()
            print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
            print(f'----- Ваша карточка ------\n{self.__usercard}')
            print(f'-- Карточка компьютера ---\n{self.__computercard}')
            start = time.perf_counter()
            useranswer = input(f'Зачеркнуть цифру? (y/n)').lower().strip()
            end = time.perf_counter()
            if end - start > self.complications:
                print('Вы проиграли')
                break
            if useranswer == 'y' and keg not in self.__usercard or useranswer != 'y' and keg in self.__usercard:
                print('Вы проиграли')
                break
            if keg in self.__usercard:
                self.__usercard.cross_num(keg)
                if self.__usercard.closed():
                    print('Вы выиграли')
                    break
            if keg in self.__computercard:
                self.__computercard.cross_num(keg)
                if self.__computercard.closed():
                    print('Вы проиграли')
                    break

loto = Game()
loto.play








