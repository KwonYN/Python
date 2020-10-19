import pygame

pygame.init()   # 초기화 : 반드시 필요!!

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 title 설정
pygame.display.set_caption("Yongnam Game")
# 게임 배경 불러오기
background = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/background_basic.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/character_basic.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴!
character_width = character_size[0]     # 캐릭터의 가로 크기
character_height = character_size[1]    # 캐릭터의 세로 크기
character_x_pos = int((screen_width - character_width)/2)        # 캐릭터의 시작 가로 위치
character_y_pos = screen_height - character_height               # 캐릭터의 시작 세로 위치

# Event Loop : 게임이 계속 진행되는지 아닌지
isRunning = True  # 게임이 진행중인지?
while isRunning:                        # 게임이 진행되는 동안에
    # 배경화면 계속 그려주기
    screen.blit(background, (0, 0)) # 배경 그리기        screen.fill((0, 0, 255))    : 파란색으로 그려주는 것!
    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    # 지속적으로 그리는 것 갱신 (배경, 캐릭터 등)
    pygame.display.update()         # 게임화면을 지속적으로 다시 그리기 (필수!!)
    
    # 게임 이벤트 확인
    for event in pygame.event.get():    # 중간에 사용자가 키보드 등으로 이벤트를 일으키는지 확인
        if event.type == pygame.QUIT:   # QUIT이라는 이벤트가 발생했다면 게임을 종료해줌 (이 이벤트 발생 시, event.type은 pygame.QUIT이 되는 것!(창이 닫히는 이벤트))
            isRunning = False

# pygame 종료
pygame.quit()