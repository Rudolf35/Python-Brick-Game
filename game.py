import pygame, math
import sys

def run_game(stage):
    # 게임 초기화
    pygame.init()
    
    # 화면 설정
    screen = pygame.display.set_mode((800, 600))
    
    # 색상 설정
    WHITE = (255, 255, 255)
    GRAY = (150, 150, 150)
    
    font = pygame.font.Font(None, 72)  # None은 pygame의 기본 폰트를 사용하겠다는 의미입니다.
    game_over_text = font.render('Game Over', True, (255, 0, 0))  # True는 안티앨리어싱을 사용하겠다는 의미입니다.
    game_clear_text = font.render('Game Clear', True, (0, 255, 0))
    
    # 패들 설정
    paddle_width = 80
    paddle_height = 15
    paddle_x = (800 - paddle_width) / 2
    paddle_y = 550
    
    # 공 설정
    ball_color = GRAY
    ball_radius = 7
    ball_x = 400
    ball_y = 400
    ball_speed = 5
    ball_angle = math.radians(270)  # 270도
    ball_dx = ball_speed * math.cos(ball_angle)
    ball_dy = -ball_speed * math.sin(ball_angle)
    
    brick_width = 65
    brick_height = 15
    
    class Brick:
        def __init__(self, x, y, width = brick_width, height = brick_height, health = 1):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.health = health
            self.color = (200-health*50, 200-health*50, 255)
            self.is_destroyed = False
        def collision(self):
            self.health -= 1
            self.color = (200-self.health*50, 200-self.health*50, 255)
        def destroy_check(self):
            if(self.health == 0):
                self.is_destroyed = True
    if(stage == 1):
        bricks = [[Brick(x, y, health = 1) for x in range(15, 785, 70)] for y in range(50, 150, 20)]
    elif(stage == 2):
        bricks = [[Brick(x, y, health = 2) for x in range(15, 785, 70)] for y in range(50, 150, 20)]
    elif(stage == 3):
        bricks = [[Brick(x, y, health = 3) for x in range(15, 785, 70)] for y in range(50, 150, 20)]
    
    def all_bricks_destroyed(bricks):
        for row in bricks:
            for brick in row:
                if not brick.is_destroyed:
                    return False
        return True
    
    # 게임 루프
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # 패들 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0:
            paddle_x -= 5
        if keys[pygame.K_RIGHT] and paddle_x < 720:
            paddle_x += 5
    
        # 공 이동
        ball_x += ball_dx
        ball_y += ball_dy
    
        # 공 반사
        if ball_y> 600:
            screen.blit(game_over_text, (200, 250))  # (200, 250)의 위치에 텍스트를 그립니다.
            pygame.display.flip()
            pygame.time.wait(2000)
            return False
        if ball_x < ball_radius or ball_x > 800 - ball_radius:
            ball_dx = -ball_dx
        if ball_y < ball_radius:
            ball_dy = -ball_dy
        # 공 반사
        if paddle_y - ball_radius < ball_y < paddle_y + paddle_height and paddle_x < ball_x < paddle_x + paddle_width:
        # 발판의 중앙에서 공이 얼마나 떨어져 있는지 계산
            offset = (ball_x - (paddle_x + paddle_width / 2)) / (paddle_width / 2)
            # 공의 방향 변경
            ball_angle = math.radians(90) - offset * (math.pi / 3)  # 최대 +-45도
            ball_dx = ball_speed * math.cos(ball_angle)
            ball_dy = -ball_speed * math.sin(ball_angle)
    
    
        # 벽돌 충돌
        for row in bricks:
            for brick in row:
                if not brick.is_destroyed:
                    # 공의 왼쪽 또는 오른쪽 표면이 벽돌에 닿았는지 판단
                    if brick.x - ball_radius < ball_x < brick.x + brick.width + ball_radius and brick.y < ball_y < brick.y + brick.height:
                        ball_dx = -ball_dx
                        brick.collision()
                        brick.destroy_check()
                        # 공의 위쪽 또는 아래쪽 표면이 벽돌에 닿았는지 판단
                    elif brick.x < ball_x < brick.x + brick.width and brick.y - ball_radius < ball_y < brick.y + brick.height + ball_radius:
                        ball_dy = -ball_dy
                        brick.collision()
                        brick.destroy_check()
        
        # 화면 그리기
        screen.fill(WHITE)
        paddle_segments = 10
        for i in range(paddle_segments):
            segment_width = paddle_width / paddle_segments
            segment_x = paddle_x + i * segment_width
            # 색상 계산 (중앙에서 양 끝으로 갈수록 진해짐)
            color_intensity = abs(2 * i / paddle_segments - 1)
            segment_color = (255 * color_intensity, 0, 0)
            pygame.draw.rect(screen, segment_color, pygame.Rect(segment_x, paddle_y, segment_width, paddle_height))
        pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
        for row in bricks:
            for brick in row:
                if not brick.is_destroyed:
                    pygame.draw.rect(screen, brick.color, pygame.Rect(brick.x, brick.y, brick.width, brick.height))
        pygame.display.flip()
        
        if all_bricks_destroyed(bricks):
            screen.blit(game_clear_text, (200, 250))
            pygame.display.flip()
            pygame.time.wait(2000)
            return True
    
        # FPS 설정
        pygame.time.Clock().tick(60)