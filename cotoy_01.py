import pygame
import time

class LV_1():
    screen_width = 1500
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))

    # 이미지 초기 위치
    image_x = 0
    image_y = screen.get_size()[1] // 2

    # 목표 위치
    target_x = 1300
    target_y = screen.get_size()[1] // 2

    # 이동 속도
    move_speed = 2

    # 이미지 이동 여부를 나타내는 플래그
    moving = False

    # 바나나 표시 여부를 나타내는 플래그
    show_banana = True

    # correct 표시 여부를 나타내는 플래그
    show_correct= False

    # wrong 표시 여부를 나타내는 플래그
    show_wrong= False

    answered = False

    def __init__(self, img) -> None:
        self.ended = 0 # 0: running, 1: wrong, 2: correct
        self.img = img
        self.t = 0
        self.correct_answer= [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def loop(self, answer = [-1]):
        if answer[0] >= 0 and not self.answered:
            self.answered = True
            # 입력받은 list값이 내가 정한 list값과 같은 경우
            if answer == self.correct_answer:
                self.moving = True
            else:
                self.show_wrong= True
        
        if self.moving:
                if self.image_x < self.target_x:
                    self.image_x += self.move_speed
                else:
                    # 목표 위치에 도달하면 이동 중지하고 바나나 이미지를 없앰
                    self.moving = False
                    self.show_banana = False
                    self.show_correct = True

        # 원숭이 이미지 표시
        self.screen.blit(self.img['monkey'], (self.image_x, self.image_y))
        
        # 바나나 이미지 표시 여부에 따라 화면 업데이트
        if self.show_banana:
            self.screen.blit(self.img['banana'], (self.target_x, self.target_y))
        # correct 이미지 표시 여부에 따라 화면 업데이트
        
        if self.show_correct:
            self.screen.blit(self.img['correct'], (self.screen.get_size()[0] // 2-300, self.screen.get_size()[1] // 2-200))
            pygame.display.flip()
            time.sleep(1)
            self.ended = 2
            
        # wrong 이미지 표시 여부에 따라 화면 업데이트   
        if self.show_wrong:
            self.screen.blit(self.img['wrong'], (self.screen.get_size()[0] // 2-300, self.screen.get_size()[1] // 2 - 200))
            pygame.display.flip()
            time.sleep(1)
            self.ended = 1

        return self.ended