import time
import pygame
import sys
from cotoy_01 import LV_1
from cotoy_02 import LV_2
from cotoy_03 import LV_3
import requests

levels = [LV_1, LV_2, LV_3]

def main():
    pygame.init()

    # 화면 크기 설정
    screen_width = 1500
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monkey Coding")

    # 배경 이미지 로드 및 크기 조정
    background = pygame.image.load("./background.jpg")
    background = pygame.transform.scale(background, (screen_width, screen_height))

    # 이미지 로드 및 크기 조정
    image_monkey = pygame.image.load("./monkey.png")
    image_banana = pygame.image.load("./banana.png")
    image_correct = pygame.image.load("./correct.png")
    image_wrong = pygame.image.load("./wrong.png")
    image_apple =  pygame.image.load("./apple.png")

    images = {
        'monkey': image_monkey, 
        'banana': image_banana, 
        'correct': image_correct, 
        'wrong': image_wrong,
        'apple': image_apple,
    }
    image_sizes = [[200, 200, 500, 500, 100], [200, 200, 200, 200, 100], [150, 150, 150, 150, 150]]

    level = 1
    level_init = False

    # 게임 루프
    running = True
    t = 0
    ended = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        t += 1
        answer_list = [-1 for i in range(16)]
        if t >= 500: # 정답 감지
            t = 0
            try:
                payload = {'name': 'kyh'}
                r = requests.get('http://monkeycoding.kro.kr:8000', params=payload)
                answer_text, taken = r.text.split('/')
                if taken == 'False':
                    answer = int(answer_text)
                    answer_list = [0 for i in range(16)]
                    for i in range(16):
                        bin = 1 << i
                        if answer & bin:
                            answer_list[i] = 1
                        else:
                            answer_list[i] = 0
                print('정답: ', answer_list)
            except:
                pass
        
        # 배경 이미지 표시
        screen.blit(background, (0, 0))

        for i, LV in enumerate(levels):
            if level != i+1:
                continue
            if not level_init:
                # 이미지 크기 조정
                for i, key in enumerate(images.keys()):
                    size = image_sizes[level-1][i]
                    images[key] = pygame.transform.scale(images[key], (size, size))
                view = LV(images)
                level_init = True
            ended = view.loop(answer_list)
            if ended > 0:
                print(ended)
                level_init = False
                if ended == 2:
                    level += 1
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()