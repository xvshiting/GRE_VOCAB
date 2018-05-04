import random
import  dataset

class game(object):

    def __init__(self,words,meaning):
        self.words = words
        self.meaning = meaning

    def set_one_game(self,words_num = 4):
        meaning_1_index = random.randint(0,len(self.meaning)-1)
        meaning_2_index = random.randint(0,len(self.meaning)-1)
        while meaning_1_index == meaning_2_index:
            meaning_2_index = random.randint(0,len(self.meaning) - 1)

        self.meaning_1 = self.meaning[meaning_1_index]
        self.meaning_2 = self.meaning[meaning_2_index]

        words_index_1 = set()
        words_index_2 = set()
        words_1 = self.words[meaning_1_index]
        words_2 = self.words[meaning_2_index]

        words_num_1 = min(words_num,len(words_1))
        words_num_2 = min(words_num,len(words_2))

        while len(words_index_1)< words_num_1:
            words_index_1.add(random.randint(0,len(words_1)-1))
        while len(words_index_2)< words_num_2:
            words_index_2.add(random.randint(0,len(words_2)-1))

        self.words_1 = [words_1[index] for index in words_index_1]
        self.words_2 = [words_2[index] for index in words_index_2]

        self.question_words = self.words_1+self.words_2
        random.shuffle(self.question_words)
        self.answer = []

        for index,item in enumerate(self.question_words):
            if item in self.words_1:
                self.answer.append(str(index))

    def judge(self,answer_string):
        user_answer = set(answer_string.split())
        if user_answer == set(self.answer):
            return True
        else:
            return False

    def show_question(self):
        print_content = ''
        for index, item in enumerate(myGame.question_words):
            print_content = print_content + "    " + str(index) + ' ' + item
            if index == 3:
                print_content = print_content + '\n'
        print(print_content)
        print('Meaning:' + myGame.meaning_1)




    def start(self):
        while 1==1:
            round = input('type the round you want to play!\n')
            round = int(round)
            self.count = 0
            self.correct_count = 0
            while self.count < round:
                self.count = self.count + 1
                print('===round ' + str(self.count) + '===')
                self.set_one_game()
                self.show_question()
                answer = input('type your answer:\n')
                self.feedback(answer)
            score = self.correct_count / self.count * 100
            print('You got {score} score'.format(score=score))


    def feedback(self,answer):
        if self.judge(answer):
            print('You are right. Other words meaning is '+self.meaning_2)
            self.correct_count = self.correct_count+1
        else:
            print('You are wrong. Right answer is :'+' '.join(self.answer))
            print(self.meaning_1+': '+' '.join(self.words_1))
            print(self.meaning_2+': '+' '.join(self.words_2))




if __name__ == '__main__':
    myGame = game(dataset.words,dataset.meaning)
    myGame.start()














