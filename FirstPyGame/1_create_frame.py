import pygame

pygame.init()   # 초기화 : 반드시 필요!!

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 title 설정
pygame.display.set_caption("Yongnam Game")

# Event Loop : 게임이 계속 진행되는지 아닌지
isRunning = True  # 게임이 진행중인지?
while isRunning:                        # 게임이 진행되는 동안에
    for event in pygame.event.get():    # 중간에 사용자가 키보드 등으로 이벤트를 일으키는지 확인
        if event.type == pygame.QUIT:   # QUIT이라는 이벤트가 발생했다면 게임을 종료해줌 (이 이벤트 발생 시, event.type은 pygame.QUIT이 되는 것!(창이 닫히는 이벤트))
            isRunning = False

# pygame 종료
pygame.quit()