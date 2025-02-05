import pygame, csv
from sys import exit
from random import randint, choice
from I_O_display import (
    StartScreen,
    StartButton,
    Game_BackG,
    Draw_Ground,
    Flying_Grounds,
)
from Player_Enemy import Player, Enemy_T, cloud, heart_D, Bonus_F, Score_Boost


class BoundaryError(Exception): ...


def New_User(text: str, score: float):
    # flag for file content  if empty check
    flag = False
    with open("Player_info.csv") as file1:
        reading_data = csv.DictReader(file1)
        # a check for file state wether empty or nt
        for checklist in reading_data:
            flag = True
    if flag:
        # here we read the file again to check if the new user does exist or not
        with open("Player_info.csv") as file1:
            reading_data = csv.DictReader(file1)
            file_content = [row for row in reading_data]
            chk_if_exist = any(text in file.values() for file in file_content)
            if not chk_if_exist:
                with open("Player_info.csv", "a") as file2:
                    adding_data = csv.DictWriter(
                        file2, fieldnames=["playername", "score"]
                    )
                    adding_data.writerow({"playername": text, "score": score})
    else:
        with open("Player_info.csv", "a") as file2:
            adding_data = csv.DictWriter(file2, fieldnames=["playername", "score"])
            adding_data.writeheader()
            adding_data.writerow({"playername": text, "score": score})

def Get_User(username: str):
    with open("Player_info.csv") as file1:
        reading_data = csv.DictReader(file1)
        key1, key2 = reading_data.fieldnames
        for single_line_data in reading_data:
            if single_line_data[key1] == username:
                return single_line_data[key2]

def Update_User(text: str, score: float):
    with open("Player_info.csv") as file1:
        reading_data = csv.DictReader(file1)
        key1, key2 = reading_data.fieldnames
        users_list = list(reading_data)
        for single_line_data in users_list:
            if single_line_data[key1] == text:
                single_line_data[key2] = score
    with open("Player_info.csv", "w") as file:
        adding_data = csv.DictWriter(file, fieldnames=[key1, key2])
        adding_data.writeheader()
        for row in users_list:
            adding_data.writerow(row)

def text_fnc(displaysurface, size, text: str, x: int, y: int, r: int, g: int, b: int):
    try:
        if x < 0 or x > displaysurface.get_width():
            raise BoundaryError
        text = int(text)
        font = pygame.font.Font("Font/Pixeltype.ttf", size)
        surface = font.render(f": {text}", True, (r, g, b))
    except ValueError:
        font = pygame.font.Font("Font/HighMount-PersonalUse.otf", size)
        surface = font.render(text, True, (r, g, b))
    rect = surface.get_rect(center=(x, y))
    displaysurface.blit(surface, rect)
    return surface, rect

def Score_f(start_time: float, scorex: int):
    score = (pygame.time.get_ticks() / 1024) - start_time + scorex
    return score

def Collision_Enemy_T_check(
    game_player,
    game_Enemy_T,
    draw_g,
    D_Surface,
    F_L,
    hearts: int,
    game_end,
    game_SF,
    frozen: bool,
    game_SB,
    game_Bonus_F,
    scorex: int,
):
    x_collide = y_collide = 0
    BG_capture = collision_time = 0
    if pygame.sprite.spritecollide(game_player.sprite, game_Enemy_T, False):
        if collision_list := pygame.sprite.spritecollide(
            game_player.sprite, game_Enemy_T, False, pygame.sprite.collide_mask
        ):
            collision_coord = [
                (sprite.rect.center, sprite.kill()) for sprite in collision_list
            ]
            x_collide, y_collide = collision_coord[0][0]
            draw_g.movment(D_Surface)
            F_L.draw(D_Surface)
            game_SB.draw(D_Surface)
            game_Bonus_F.draw(D_Surface)
            BG_capture = D_Surface.copy()
            collision_time = pygame.time.get_ticks() / 1024
            hearts -= 1
            scorex -= 25
            if hearts < 0:
                game_end = True
                game_SF = False
            frozen = True
    return (
        x_collide,
        y_collide,
        BG_capture,
        collision_time,
        hearts,
        game_end,
        game_SF,
        frozen,
        scorex,
    )

def Collision_Enemy_T_result(
    flag_c,
    frozen,
    D_Surface,
    BG_capture,
    x_collide,
    y_collide,
    fight,
    collision_time,
    cloud_flag,
    fight_cloud,
):
    D_Surface.blit(BG_capture, (0, 0))
    if cloud_flag == 0:
        fight_cloud = cloud(x_collide - 150, y_collide)
        flag_c = 1
        fight.play(-1)
        fight.set_volume(1)
        cloud_flag = 1

    if flag_c == 1:
        fight_cloud.animate(D_Surface)

    if (pygame.time.get_ticks() / 1024) > collision_time + 2:
        frozen = False
        cloud_flag = 0
        flag_c = 0
        fight.stop()

    return cloud_flag, frozen, flag_c, fight_cloud

def print_const_text(D_Surface, user_name=""):
    new_score = 0
    text_fnc(D_Surface, 150, "Game Over", 840, 100, 150, 105, 25)
    text_fnc(D_Surface, 150, f"Go Again", 850, 400, 150, 105, 25)
    if not user_name == "":
        new_score = Get_User(user_name)
    text_fnc(D_Surface, 75, f"Your Score is", 750, 950, 150, 105, 25)
    text_fnc(D_Surface, 150, int(float(new_score)), 1075, 955, 150, 105, 25)

def main():
    pygame.init()
    D_Surface = pygame.display.set_mode((1680, 1050))
    pygame.display.set_caption("Cat Hunt")
    clock = pygame.time.Clock()

    # start screen
    screen_sprite = StartScreen()
    s_screen = pygame.sprite.GroupSingle()
    s_screen.add(screen_sprite)

    # start button
    start_button_sprite = StartButton()
    s_button = pygame.sprite.GroupSingle()
    s_button.add(start_button_sprite)

    # Game_end_BG
    game_BG_sprite = Game_BackG()
    game_BG = pygame.sprite.GroupSingle()
    game_BG.add(game_BG_sprite)
    # Draw_Ground
    draw_g = Draw_Ground()
    F_L = pygame.sprite.Group()

    # BG_music
    pygame.mixer.init()
    pygame.mixer.music.load("Audio/Intro_Music.wav")
    # flags sued for audio control
    BG_M_flag = 0
    Repeater = 0
    # fight mp3
    fight = pygame.mixer.Sound("Audio/Fight.mp3")

    # player
    game_player_sprite = Player()
    game_player = pygame.sprite.GroupSingle()
    game_player.add(game_player_sprite)
    heart = heart_D()
    hearts = 3

    # Enemy_Tiger
    game_Enemy_T = pygame.sprite.Group()

    # Score_Booster
    game_SB = pygame.sprite.Group()

    # Bonus_fairy
    game_Bonus_F = pygame.sprite.Group()

    # cloud flag
    cloud_flag = 0
    flag_c = 0

    # userdata option
    nameflag = 1
    score = 0
    # score adder flag where it add 50 point when it collide with score booster avatar
    scorex = 0
    user_name = ""

    # collision data
    x_collide = 0
    y_collide = 0
    # screen capture before collision with enemy
    BG_capture = 0
    # used to determine the duration of the cloud animation
    collision_time = 0
    # later used to have cloud class assigned to it to apply animation for cloud
    fight_cloud = 0
    # used as a flag to let the player of the flying floor when he is out of its bound
    flag_pos_reset = 0

    # game_start_flag
    start_time = 0
    game_SF = False
    game_end = False

    # game_freeze flag
    frozen = False

    # creation of custome event
    # enemytiger
    tiger_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(tiger_timer, randint(10000, 15000))
    # summoning flying lands
    Flying_land = pygame.USEREVENT + 2
    pygame.time.set_timer(Flying_land, randint(15000, 25000))
    # Bonus_fairy
    Bonus_fairy = pygame.USEREVENT + 3
    pygame.time.set_timer(Bonus_fairy, randint(30000, 35000))
    # Bonus_fairy
    Score_Booster = pygame.USEREVENT + 4
    pygame.time.set_timer(Score_Booster, randint(20000, 30000))

    while True:
        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                game_SF = False
                game_end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (
                    (s_button.sprite.rect.collidepoint(event.pos))
                    and (nameflag == 0)
                    and (game_end == False)
                ):
                    start_time = pygame.time.get_ticks() / 1024
                    game_SF = True

            if (nameflag == 1) and (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_KP_ENTER:
                    New_User(user_name, 0)
                    nameflag = 0
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[0:-1]
                else:
                    user_name += event.unicode

            if event.type == tiger_timer and game_SF:
                game_Enemy_T.add(Enemy_T())

            if event.type == Flying_land and game_SF:
                F_L.add(Flying_Grounds())

            if event.type == Bonus_fairy and game_SF:
                yindex = randint(300, 400)
                game_Bonus_F.add(Bonus_F(yindex))

            if event.type == Score_Booster and game_SF:
                game_SB.add(Score_Boost())
        # Game Start
        if game_SF:
            score = Score_f(start_time, scorex)
            # if there is no collision with the enemy
            if not frozen:
                # bgmusic
                #flag used to ontialize/load the track for once and avoide it being starting from begining each cycle 
                if BG_M_flag == 0:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("Audio/BG_Music.wav")
                    BG_M_flag = 1
                elif Repeater == 0:
                    pygame.mixer.music.play(loops=-1)
                    pygame.mixer.music.set_volume(0.5)
                    Repeater = 1

                # backGround
                draw_g.movment(D_Surface)
                F_L.draw(D_Surface)
                F_L.update()

                # Player
                game_player.draw(D_Surface)
                game_player.update()

                # enemy_tiger
                game_Enemy_T.draw(D_Surface)
                game_Enemy_T.update()

                # Score_Booster
                game_SB.draw(D_Surface)
                game_SB.update()

                # Bonus_Fairy
                game_Bonus_F.draw(D_Surface)
                game_Bonus_F.update()

                # collision check for enemy_tiger
                (
                    x_collide,
                    y_collide,
                    BG_capture,
                    collision_time,
                    hearts,
                    game_end,
                    game_SF,
                    frozen,
                    scorex,
                ) = Collision_Enemy_T_check(
                    game_player,
                    game_Enemy_T,
                    draw_g,
                    D_Surface,
                    F_L,
                    hearts,
                    game_end,
                    game_SF,
                    frozen,
                    game_SB,
                    game_Bonus_F,
                    scorex,
                )
                # collision check for flying floor:
                for F_Lsprite in F_L:
                    if (
                        game_player.sprite.rect.y <= F_Lsprite.rect.top
                        and pygame.sprite.collide_mask(game_player.sprite, F_Lsprite)
                    ):
                        # F_Lsprite.rect.top = 450
                        game_player.sprite.rect.bottom = F_Lsprite.rect.top + 150
                        flag_pos_reset = 1
                    elif flag_pos_reset and game_player.sprite.rect.bottom == (
                        F_Lsprite.rect.top + 150
                    ):
                        game_player.sprite.rect.bottom = 860
                        flag_pos_reset = 0

                # collision with F/spirit:
                if pygame.sprite.spritecollide(game_player.sprite, game_Bonus_F, False):
                    if Bonus_C_list := pygame.sprite.spritecollide(
                        game_player.sprite,
                        game_Bonus_F,
                        False,
                        pygame.sprite.collide_mask,
                    ):
                        for sprite in Bonus_C_list:
                            sprite.kill()
                        if hearts < 3:
                            hearts += 1

                # collision with F/spirit:
                if pygame.sprite.spritecollide(game_player.sprite, game_SB, False):
                    if SB_list := pygame.sprite.spritecollide(
                        game_player.sprite, game_SB, False, pygame.sprite.collide_mask
                    ):
                        for sprite in SB_list:
                            sprite.kill()
                        scorex += 50
            # if there is a collision with the enemy
            else:
                cloud_flag, frozen, flag_c, fight_cloud = Collision_Enemy_T_result(
                    flag_c,
                    frozen,
                    D_Surface,
                    BG_capture,
                    x_collide,
                    y_collide,
                    fight,
                    collision_time,
                    cloud_flag,
                    fight_cloud,
                )
                heart.animate(hearts, D_Surface)

            heart.update_heart(D_Surface, hearts)
            # score disp
            Update_User(user_name, score)
            text_fnc(D_Surface, 50, "Score ", 1450, 50, 150, 105, 25)
            text_fnc(D_Surface, 70, score, 1575, 54, 150, 105, 25)
        # intro screen options
        elif not game_end:
            # bgmusic
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            s_screen.draw(D_Surface)
            s_screen.update()
            # game_name
            text_fnc(D_Surface, 150, "Hunting Cat", 840, 100, 150, 105, 25)
            if nameflag == 1:
                text_fnc(D_Surface, 75, "Enter Your Name", 840, 300, 150, 105, 25)
                text_fnc(D_Surface, 75, user_name, 840, 525, 150, 105, 25)
            else:
                # Start screen display
                new_score = Get_User(user_name)
                s_button.draw(D_Surface)
                s_button.update()
                text_fnc(D_Surface, 75, f"Last Score Was", 700, 800, 150, 105, 25)
                text_fnc(D_Surface, 150, int(float(new_score)), 1140, 805, 150, 105, 25)
        # end screen options
        else:
            game_BG.draw(D_Surface)
            game_BG.update()
            BG_capture = D_Surface.copy()
            print_const_text(D_Surface, user_name)
            y_sur, y_rect = text_fnc(D_Surface, 75, f"Yes", 340, 600, 150, 105, 25)
            n_sur, n_rect = text_fnc(D_Surface, 75, f"No", 1340, 600, 150, 105, 25)
            mouse_pos = pygame.mouse.get_pos()
            # return true or false
            if y_rect.collidepoint(mouse_pos):
                y_sur = pygame.transform.scale_by(y_sur, 4)
                D_Surface.blit(BG_capture, (0, 0))
                print_const_text(D_Surface, user_name)
                D_Surface.blit(y_sur, y_rect)
                # return a tuble of the state of each button wether pressed or not as in True or Flase
                fight.stop()
                if pygame.mouse.get_pressed()[0]:
                    scorex = 0
                    hearts = 3
                    game_Bonus_F.empty()
                    game_SB.empty()
                    game_Enemy_T.empty()
                    F_L.empty()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("Audio/Intro_Music.wav")
                    nameflag = 1
                    user_name = ""
                    game_end = False
                    BG_M_flag = 0
                    Repeater = 0
                    frozen = False
            elif n_rect.collidepoint(mouse_pos):
                n_sur = pygame.transform.scale_by(n_sur, 4)
                D_Surface.blit(BG_capture, (0, 0))
                print_const_text(D_Surface, user_name)
                D_Surface.blit(n_sur, n_rect)
                if pygame.mouse.get_pressed()[0]:
                    pygame.quit()
                    exit()
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
