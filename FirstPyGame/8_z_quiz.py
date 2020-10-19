import pygame
from random import randint

########################### 기본 초기화 ###########################

pygame.init()  # 초기화 : 반드시 필요!!

# 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 title 설정
pygame.display.set_caption("Poo Game")

# FPS
clock = pygame.time.Clock()

########################### 사용자 ###########################

# 1. 사용자 게임 초기화 : 배경화면, 게임 이미지, 좌표, 속도, 폰트 등

# 게임 배경 불러오기
background = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/white_basic.png")
# Timeout 배경
success_background = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/Success.png")

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 디폴트 폰트
# 게임 시작 시간
total_running_time = 50
# 시간 계산
start_tics = pygame.time.get_ticks()  # 시작 tick 정보 받아옴

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/character_basic.png")
character_size = character.get_rect().size  # 이미지의 크기를 구해옴!
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = round(int((screen_width - character_width) / 2))  # 캐릭터의 시작 가로 위치
character_y_pos = round(screen_height - character_height)  # 캐릭터의 시작 세로 위치

# 캐릭터 이동 좌표
to_x = 0
# 캐릭터 이동 속도
to_x_step = 0.6

# Enemy 캐릭터
enemy = pygame.image.load("C:/Users/LG/Desktop/Professional_Algorithm/FirstPyGame/enemy_basic.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴!
enemy_width = enemy_size[0]  # Enemy 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # Enemy 캐릭터의 세로 크기
enemy_x_pos = randint(0, 480-enemy_width)   #round((screen_width / 2) - (enemy_width / 2))  # Enemy 캐릭터의 시작 가로 위치
enemy_y_pos = 0                             # round(screen_height / 2)  # Enemy 캐릭터의 시작 세로 위치

# Enemy 이동
enemy_to_y = 0
# Enemy 이동 속도
enemy_to_y_step = 0.6

# Event Loop : 게임이 계속 진행되는지 아닌지
isRunning = True  # 게임이 진행중인지?
while isRunning:  # 게임이 진행되는 동안에
    # FPS 지정
    # Ex> 캐릭터가 1초에 100만큼 움직여야 한다고 함!
    # 10 fps : 1초 동안 10번 동작 -> 한 번에 몇 만큼 이동? : 10만큼 (10만큼 * 10번 = 100만큼 움직임)
    # 20 fps : 1초 동안 20번 동작 -> 한 번에 몇 만큼 이동? : 5만큼 (5만큼 * 20번 = 100만큼 움직임)
    delta = clock.tick(50)
    print("FPS : " + str(clock.get_fps()))

    # 2. 이벤트 처리 : 키보드, 마우스 등

    # 게임 이벤트 확인
    for event in pygame.event.get():  # 중간에 사용자가 키보드 등으로 이벤트를 일으키는지 확인
        if event.type == pygame.QUIT:  # QUIT이라는 이벤트가 발생했다면 게임을 종료해줌 (이 이벤트 발생 시, event.type은 pygame.QUIT이 되는 것!(창이 닫히는 이벤트))
            isRunning = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인 => 움직임
            if event.key == pygame.K_LEFT:
                to_x -= to_x_step
            elif event.key == pygame.K_RIGHT:
                to_x += to_x_step

        if event.type == pygame.KEYUP:  # 키가 떼졌는지 확인 => 움직임 멈춤 (움직여주지 않음!)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * delta
    enemy_y_pos += enemy_to_y_step * delta

    # 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width
    # 4. 충돌 처리

    # 캐릭터 충돌 처리를 위한 캐릭터 rect 정보 업데이트 (Against Enemy)
    character_rect = character.get_rect()
    character_rect.left = round(character_x_pos)
    character_rect.top = round(character_y_pos)
    # Enemy
    enemy_rect = enemy.get_rect()
    enemy_rect.left = round(enemy_x_pos)
    enemy_rect.top = round(enemy_y_pos)  # 현재 Enemy 캐릭터 위치(화면상에 그려지는_변화 반영)

    # 똥 그리기
    if enemy_y_pos >= screen_height:   # 나갔어
        enemy_x_pos = randint(0, 480 - enemy_width)
        enemy_y_pos = 0

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print(f'똥 좌측상단 좌표 : y = {enemy_rect.top} x = {enemy_rect.left}')
        print(f'캐릭터 좌측상단 좌표 : y = {character_rect.top} x = {character_rect.left}')
        print("충돌 발생!!")
        isRunning = False

    # 5. 화면에 그리기

    # 타이머
    # 1. 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - total_running_time) / 1000  # msec 단위이기 때문 => 초 단위로 표시해주기 위함!
    # 2. 시간 표시
    timer = game_font.render(str(int(total_running_time - elapsed_time)) + " sec", True, (0, 0, 0))  # white

    # 배경화면 계속 그려주기
    screen.blit(background, (0, 0))  # 배경 그리기        screen.fill((0, 0, 255))    : 파란색으로 그려주는 것!
    # 캐릭터 그리기
    screen.blit(character, (round(character_x_pos), round(character_y_pos)))
    # Enemy 캐릭터 그리기
    screen.blit(enemy, (round(enemy_x_pos), round(enemy_y_pos)))

    # 타이머 그리기
    screen.blit(timer, (10, 10))
    # 만약 시간이 0이 되면, 게임 종료!
    if total_running_time - elapsed_time <= 0:
        print("Time out!!")
        screen.blit(success_background, (0, 0))
        pygame.display.update()  # 마지막 그려주기(갱신)
        isRunning = False

    # 지속적으로 그리는 것 갱신 (배경, 캐릭터 등)
    pygame.display.update()  # 게임화면을 지속적으로 다시 그리기 (필수!!)

# 종료되기 전 딜레이 시간
pygame.time.delay(2000)
# pygame 종료
pygame.quit()