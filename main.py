import pygame
import random
class BlankScorePage:
    def __init__(self, screen):
        self.screen = screen

    def draw_score_page(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        font = pygame.font.SysFont("Calibri", 30, bold=True)
        score_text = font.render("Top 10 Scores: "
                                 "12 11 10 9 8 7 6 5 4 3", True, (0, 0, 0))
        back_button = pygame.Rect(50, 300, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), back_button)
        back_text = font.render("Back", True, (155, 255, 255))
        self.screen.blit(score_text, (150, 100))
        self.screen.blit(back_text, (60, 310))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        return

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Score Page")

# Create and display the blank score page
score_page = BlankScorePage(screen)
score_page.draw_score_page()

pygame.quit()

class BlankConfigurePage:
    def __init__(self, screen):
        self.screen = screen

    def draw_configure_page(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        font = pygame.font.SysFont("Calibri", 30, bold=True)

        lines = [
            "Configure Page",
            "Size of the field: 10",
            "Game lvl: 1",
            "Game Type: Normal",
            "Player or AI mode: Player"
        ]

        line_height = font.get_linesize()

        back_button = pygame.Rect(50, 600, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), back_button)
        back_text = font.render("Back", True, (155, 255, 255))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        return

            self.screen.fill((255, 255, 255))

            # Render each line of text
            for i, line in enumerate(lines):
                text_surface = font.render(line, True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + i * line_height))
                self.screen.blit(text_surface, text_rect)

            pygame.draw.rect(self.screen, (0, 0, 0), back_button)
            self.screen.blit(back_text, (60, 610))
            pygame.display.flip()



    pygame.init()


screen = pygame.display.set_mode((550, 700))
pygame.display.set_caption("Configure Page")

# Create and display the blank configure page
configure_page = BlankConfigurePage(screen)
configure_page.draw_configure_page()

pygame.quit()
class ScorePage:
    def __init__(self, screen):
        self.screen = screen

    def draw_score_page(self):
        # Clear the screen
        self.screen.fill((255, 255, 255))

        font = pygame.font.SysFont("Calibri", 30, bold=True)
        score_text = font.render("Top Scores Page", True, (0, 0, 0))
        back_button = pygame.Rect(50, 600, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), back_button)
        back_text = font.render("Back", True, (155, 255, 255))
        self.screen.blit(score_text, (100, 100))
        self.screen.blit(back_text, (60, 610))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        return

class StartupPage:
    def __init__(self):
        self.width = 400
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tetris Startup Page")
        self.start_game = False  # Flag to track if the game should start
        self.current_page = "startup"  # Flag to track the current page


    def draw_startup_page(self):
        new_button = pygame.Rect(50, 520, 300, 50)
        font = pygame.font.SysFont("Calibri", 30, bold=True)
        font_title = pygame.font.SysFont("Calibri", 50, bold=True)
        title = font_title.render("Tetris", True, (220, 140, 160))
        year_course = font.render("2023 "
                                  "2805ICT", True, (10, 2, 230))
        students = font.render("Students:", True, (0, 0, 0))
        student_names = [
            "Beven C"
            "        \n esc to Exit"

        ]

        student_texts = [font.render(student, True, (0, 0, 0)) for student in student_names]
        exit_button = pygame.Rect(50, 400, 300, 50)
        score_button = pygame.Rect(50, 400, 300, 50)
        configure_button = pygame.Rect(50, 460, 300, 50)
        new_button = pygame.Rect(50, 520, 300, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    return
                elif score_button.collidepoint(event.pos):
                    self.current_page = "score"  # Switch to the score page
                elif configure_button.collidepoint(event.pos):
                    self.current_page = "configure"  # Switch to the configure page

                elif score_button.collidepoint(event.pos):
                    self.current_page = "score"  # Switch to the score page
                elif configure_button.collidepoint(event.pos):
                    self.screen.fill((255, 255, 255))
            self.screen.fill((255, 255, 255))
            self.screen.fill((255, 255, 255))
            self.screen.blit(title, (150, 50))
            self.screen.blit(year_course, (20, 150))
            self.screen.blit(students, (20, 200))
            for i, text in enumerate(student_texts):
                self.screen.blit(text, (20, 230 + i * 30))

            pygame.draw.rect(self.screen, (0, 0, 0), exit_button)
            pygame.draw.rect(self.screen, (0, 0, 0), score_button)
            pygame.draw.rect(self.screen, (0, 0, 0), configure_button)
            pygame.draw.rect(self.screen, (0, 0, 0), new_button)

            font_button = pygame.font.SysFont("Calibri", 25, bold=True)
            exit_text = font_button.render("Start", True, (155, 255, 255))
            score_text = font_button.render("Top Scores", True, (155, 255, 255))
            configure_text = font_button.render("Configure", True, (155, 255, 255))

            self.screen.blit(exit_text, (160, 410))
            self.screen.blit(score_text, (130, 540))
            self.screen.blit(configure_text, (130, 465))

            if self.start_game:
                return
            elif self.current_page == "score":
                score_page = BlankScorePage(self.screen)
                score_page.draw_score_page()
                self.current_page = "startup"  # Switch back to the startup page
            elif self.current_page == "configure":
                configure_page = BlankConfigurePage(self.screen)
                configure_page.draw_configure_page()
                self.current_page = "startup"  # Switch back to the startup page

                # ... (your existing code)

            pygame.display.flip()

            pygame.display.flip()

            if self.start_game:
                return
            elif self.current_page == "score":
                score_page = ScorePage(self.screen)
                score_page.draw_score_page()
                self.current_page = "startup"  # Switch back to the startup page
            elif self.current_page == "configure":
                # Handle configure page action
                pass  # Add your code here to implement the configure page

            mouse_pos = pygame.mouse.get_pos()
            if exit_button.collidepoint(mouse_pos):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.quit()
                        return

                    def handle_events(self):
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                return

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.exit_button.collidepoint(event.pos):
                                    pygame.quit()
                                    return
                                elif self.score_button.collidepoint(event.pos):
                                    self.current_page = "score"  # Switch to the score page
                                elif self.configure_button.collidepoint(event.pos):
                                    self.current_page = "configure"  # Switch to the configure page
                                elif self.new_button.collidepoint(event.pos):
                                    self.start_game = True  # Start the game


def draw_score_page(self):
        self.screen.fill((255, 255, 255))  # Clear the screen
        font = pygame.font.SysFont("Calibri", 30, bold=True)
        # ... (draw score page content using font rendering)

        # Draw a back button
        back_button = pygame.Rect(50, 800, 100, 50)
        pygame.draw.rect(self.screen, (0, 0, 0), back_button)
        back_text = font.render("Back", True, (155, 255, 255))
        self.screen.blit(back_text, (60, 810))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.collidepoint(event.pos):
                        self.show_score_page = False
                        return
pygame.init()

startup_page = StartupPage()
startup_page.draw_startup_page()
colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class Figure:
    x = 0
    y = 0

    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])


class Tetris:
    def __init__(self, height, width):
        self.level = 2
        self.score = 0
        self.state = "start"
        self.field = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        self.zoom = 20
        self.figure = None

        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def draw_next_shape(self, screen):
        next_font = pygame.font.SysFont('Calibri', 20, True, False)
        next_text = next_font.render("Next:", True, BLACK)
        screen.blit(next_text, [320, 50])

        next_figure = Figure(0, 0)  # Create the next figure without moving it
        next_figure.type = self.figure.type  # Set the type of the next figure to the current one
        next_figure.color = random.randint(1, len(colors) - 1)  # Assign a random color to the next figure
        next_figure.rotation = 0  # Reset rotation for the next figure

        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in next_figure.image():
                    pygame.draw.rect(screen, colors[next_figure.color],
                                     [330 + 20 * j, 100 + 20 * i, 18, 18])

    def new_figure(self):
        self.figure = Figure(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation




pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris 2023 2805ICT")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    game.draw_next_shape(screen)  # Draw the next shape preview

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 65, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()