import pygame
import time

class LV_2():
    screen_width = 1500
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 원숭이와 바나나의 초기 위치 설정
    upper_monkey_x = 50
    upper_monkey_y = screen_height // 2 - 200
    upper_banana_x = screen_width - 200 - 50
    upper_banana_y = screen_height // 2 - 200
    lower_monkey_x = 50
    lower_monkey_y = screen_height // 2 + 200
    lower_banana_x = screen_width - 200 - 50
    lower_banana_y = screen_height // 2 + 200 
    # correct 와 wrong의 초기 위치 설정
    wrong_x =  screen_width//2
    wrong_y_top = screen_height // 2 - 200
    wrong_y_bottom = screen_height // 2 + 200
    correct_x =  screen_width//2
    correct_y_top = screen_height // 2 - 200
    correct_y_bottom = screen_height // 2 + 200

    # 이동 속도
    move_speed = 2

    # 바나나 표시 여부를 나타내는 플래그
    show_upper_banana = True
    show_lower_banana = True

    # correct 표시 여부를 나타내는 플래그
    show_upper_correct= False
    show_lower_correct= False

    # wrong 표시 여부를 나타내는 플래그
    show_upper_wrong= False
    show_lower_wrong= False

    answered = False

    def __init__(self, img) -> None:
        self.ended = 0 # 0: running, 1: wrong, 2: correct
        self.img = img
        self.t = 0
        self.correct_answer= [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def loop(self, answer = [-1]):
        # 원숭이와 바나나 이미지 그리기
        self.screen.blit(self.img['monkey'], (self.upper_monkey_x , self.upper_monkey_y))
        self.screen.blit(self.img['monkey'], (self.lower_monkey_x , self.lower_monkey_y))
        if self.show_upper_banana == True:
            self.screen.blit(self.img['banana'], (self.upper_banana_x, self.upper_banana_y))
        if self.show_lower_banana == True:    
            self.screen.blit(self.img['banana'], (self.lower_banana_x, self.lower_banana_y))

        # 상단 원숭이는 바나나를 먹는다
        if answer[0] >= 0 and not self.answered:
            self.answered = True
            # 입력받은 list값이 내가 정한 list값과 같은 경우
            if answer == self.correct_answer:
                self.show_lower_banana = False
                self.show_lower_correct = True
            else:
                self.show_wrong= True
                self.show_lower_wrong = True
                self.screen.blit(self.img['wrong'], (self.wrong_x, self.wrong_y_top))
                self.screen.blit(self.img['wrong'], (self.wrong_x, self.wrong_y_bottom))
                pygame.display.flip()
                time.sleep(1)
                self.ended = 1
                
        
        if self.show_lower_correct:
            if self.upper_monkey_x < self.upper_banana_x:
                self.upper_monkey_x += self.move_speed
            else:
                self.show_upper_banana = False
                self.show_upper_correct = True
                self.screen.blit(self.img['correct'], (self.correct_x, self.correct_y_top))
                self.screen.blit(self.img['correct'], (self.correct_x, self.correct_y_bottom))
                pygame.display.flip()
                time.sleep(1)
                self.ended = 2
        
        return self.ended
