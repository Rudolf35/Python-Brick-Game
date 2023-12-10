import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Brick Game")

# 색상 설정
LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 버튼 클래스
class Button:
    def __init__(self, text, x, y, color=BLACK):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont('Arial', 16, bold=True)

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        pygame.draw.rect(screen, self.color, text_rect.inflate(20, 10))
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return pygame.Rect(self.x - 50, self.y - 15, 100, 30).collidepoint(pos)

# 버튼 생성
start_button = Button("Start", 400, 300, BLUE)
exit_button = Button("Exit", 400, 400, RED)

stage_clears = [False, False, False]

stage_buttons = [
    Button("1", 300, 300, RED if not stage_clears[0] else BLUE),
    Button("2", 400, 300, RED if not stage_clears[1] else BLUE),
    Button("3", 500, 300, RED if not stage_clears[2] else BLUE)
]

# 화면 상태
states = ["start", "stage"]
current_state = "start"

# 텍스트 설정
title_font = pygame.font.SysFont('Arial', 30, bold=True)

# 메인 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if current_state == "start":
                if start_button.is_clicked(pos):
                    current_state = "stage"
                elif exit_button.is_clicked(pos):
                    pygame.quit()
                    sys.exit()
            elif current_state == "stage":
                for i, button in enumerate(stage_buttons):
                    if button.is_clicked(pos):
                        # 스테이지를 실행하고 클리어 여부를 저장
                        from game import run_game
                        stage_clears[i] = run_game(i+1)
                        # 게임이 종료된 후 여기로 돌아옴
                        current_state = "stage"
                        # 클리어 여부에 따라 버튼 색상 변경
                        button.color = BLUE if stage_clears[i] else RED
    # 화면 그리기
    screen.fill(LIGHTGRAY)
    if current_state == "start":
        start_button.draw(screen)
        exit_button.draw(screen)
        # 타이틀 텍스트
        title_surface = title_font.render("Brick Game", True, BLACK)
        title_rect = title_surface.get_rect(center=(400, 100))
        screen.blit(title_surface, title_rect)
    elif current_state == "stage":
        stage_buttons[0].draw(screen)
        stage_buttons[1].draw(screen)
        stage_buttons[2].draw(screen)
    pygame.display.flip()