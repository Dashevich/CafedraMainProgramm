import pygame
import pygame_gui
import os

pygame.init()
pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

screen = pygame.Surface((800, 600))
screen.fill(pygame.Color('#FFFFFF'))

manager = pygame_gui.UIManager((800, 600))
# кнопки
right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650, 275), (100, 50)),
                                            text='>',
                                            manager=manager)
left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((50, 275), (100, 50)),
                                           text='<',
                                           manager=manager)
gen_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 450), (100, 50)),
                                          text='Generate',
                                          manager=manager)
# меню предметов
directory = 'Subjects'
files = os.listdir(directory)
subj = files[0]
themes = os.listdir("Subjects/" + subj)
subj_drop = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(options_list=files,
                                                                 starting_option=files[0],
                                                                 relative_rect=pygame.Rect(0, 0, 150, 30),
                                                                 manager=manager)
clock = pygame.time.Clock()
is_running = True
theme = 0


def load_gen(subj, theme):   # запуск генератора
    os.startfile("C:/Users/Xiaomi/Documents/school/ProjGens/Subjects/" + subj + "/" + themes[theme])


def draw(subj, theme):   # переотрисовка окна
    global themes
    pygame.draw.rect(screen, (0, 0, 0), (150, 100, 500, 400), 4)
    text = pygame.font.Font("freesansbold.ttf", 30)
    y = 120
    if len(themes) > 0:
        #print(theme)
        demo_file = open(r"Subjects/" + subj + "/" + themes[theme], encoding='utf-8')
        for i in demo_file:
            if "# &" in i:
                story = i.split("# &")[1]
                story = story.split('\n')[0]
                text1 = text.render(story, True, (0, 0, 0))
                screen.blit(text1, (160, y))
                y += 35
        demo_file.close()

    else:
        story = "Заданий нет"
        text1 = text.render(story, True, (0, 0, 0))
        screen.blit(text1, (160, 120))


while is_running:  # основной цикл
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:  # события
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == right_button:
                    screen.fill(pygame.Color('#FFFFFF'))
                    theme += 1
                    if len(themes) <= theme:
                        theme = 0
                if event.ui_element == left_button:
                    screen.fill(pygame.Color('#FFFFFF'))
                    theme -= 1
                    if theme < 0:
                        theme = len(themes)-1
                if event.ui_element == gen_button:
                    screen.fill(pygame.Color('#FFFFFF'))
                    if len(themes) > 0:
                        load_gen(subj, theme)
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                screen.fill(pygame.Color('#FFFFFF'))
                if event.ui_element == subj_drop:
                    theme = 0
                    themes = os.listdir("Subjects/" + event.text)
                    subj = event.text
                    print("Selected option:", event.text)
        draw(subj, theme)
        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(screen, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
