import time
import pygame
import sys
pygame.init()

my_answer_LV3_1 =[1, 2, 3, 4, 5]
my_answer_LV3_2 =[]
my_answer_LV3_3 =[1, 1, 1, 1, 1]
correct_answer_LV3_1= [1, 2, 3, 4, 5]
correct_answer_LV3_2= [0, 0, 0, 0, 0]
correct_answer_LV3_3= [1, 1, 1, 1, 1]

class LV_3():
    # 화면 크기 설정
    screen_width, screen_height = 1500, 1000
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 원숭이와 바나나의 초기 위치 설정
    top_monkey_x = 50
    top_monkey_y = 200 
    top_banana_x = screen_width -250
    top_banana_y = 200
    middle_monkey_x = 50
    middle_monkey_y = screen_height // 2 
    bottom_monkey_x = 50
    bottom_monkey_y = 800
    bottom_banana_x = screen_width - 250
    bottom_banana_y = 800
    
    #사과의 위치 설정
    apple_x = screen_width - 250
    apple_y = screen_height // 2

    # correct 와 wrong의 초기 위치 설정
    wrong_x =  screen_width//2 - 100
    wrong_y_top = 200
    wrong_y_middle = screen_height // 2 
    wrong_y_bottom = 800
    correct_x =  screen_width//2 - 100
    correct_y_top = 200
    correct_y_middle = screen_height // 2 
    correct_y_bottom = 800

    # 이동 속도
    move_speed = 2

    # 바나나 표시 여부를 나타내는 플래그
    show_top_banana = True
    show_bottom_banana = True

    # 사과 표시 여부를 나타내는 플래그
    show_apple = True
    show_apple = True

    # correct 표시 여부를 나타내는 플래그
    show_top_correct = False
    show_middle_correct = False
    show_bottom_correct = False


    # wrong 표시 여부를 나타내는 플래그
    show_top_wrong = False
    show_middle_wrong = False
    show_bottom_wrong = False

    answered = False

    correct = False

    def __init__(self, img) -> None:
        self.ended = 0 # 0: running, 1: wrong, 2: correct
        self.img = img
        self.t = 0
        self.correct_answer= [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]

    def loop(self, answer = [-1]):
        # 원숭이와 바나나 이미지 그리기
        self.screen.blit(self.img['monkey'], (self.top_monkey_x , self.top_monkey_y))
        self.screen.blit(self.img['monkey'], (self.middle_monkey_x , self.middle_monkey_y))
        self.screen.blit(self.img['monkey'], (self.bottom_monkey_x , self.bottom_monkey_y))
        if self.show_top_banana == True:
            self.screen.blit(self.img['banana'], (self.top_banana_x, self.top_banana_y))
        if self.show_bottom_banana == True:    
            self.screen.blit(self.img['banana'], (self.bottom_banana_x, self.bottom_banana_y))
        if self.show_apple == True:    
            self.screen.blit(self.img['apple'], (self.apple_x, self.apple_y))
        
        if answer[0] >= 0 and not self.answered:
            self.answered = True
            # 입력받은 list값이 내가 정한 list값과 같은 경우
            if answer == self.correct_answer:
                show_bottom_banana = False
                show_bottom_correct = True
                self.correct = True
            else:
                self.screen.blit(self.img['wrong'], (self.wrong_x, self.wrong_y_middle))
                self.screen.blit(self.img['wrong'], (self.wrong_x, self.wrong_y_bottom))
                self.screen.blit(self.img['wrong'], (self.wrong_x, self.wrong_y_top))
                pygame.display.flip()
                time.sleep(1)
                self.ended = 1
        
        if self.correct:
            if self.top_monkey_x < self.top_banana_x:
                self.top_monkey_x += self.move_speed
            else:
                self.screen.blit(self.img['correct'], (self.correct_x, self.correct_y_top))
                self.screen.blit(self.img['correct'], (self.correct_x, self.correct_y_middle))
                self.screen.blit(self.img['correct'], (self.correct_x, self.correct_y_bottom))
                time.sleep(1)
                self.ended = 2

            if self.middle_monkey_x < self.apple_x:
                self.middle_monkey_x += self.move_speed
            else:
                show_apple = False
                show_middle_correct = True
        return self.ended
        