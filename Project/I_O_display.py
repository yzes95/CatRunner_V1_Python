import pygame
from random import randint


class StartScreen(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        image_ST_S_1 = pygame.image.load("Login_screen/1.gif").convert_alpha()
        image_ST_S_2 = pygame.image.load("Login_screen/2.gif").convert_alpha()
        image_ST_S_3 = pygame.image.load("Login_screen/3.gif").convert_alpha()
        image_ST_S_4 = pygame.image.load("Login_screen/4.gif").convert_alpha()
        image_ST_S_5 = pygame.image.load("Login_screen/5.gif").convert_alpha()
        image_ST_S_6 = pygame.image.load("Login_screen/6.gif").convert_alpha()
        image_ST_S_7 = pygame.image.load("Login_screen/7.gif").convert_alpha()
        image_ST_S_8 = pygame.image.load("Login_screen/8.gif").convert_alpha()
        image_ST_S_9 = pygame.image.load("Login_screen/9.gif").convert_alpha()
        image_ST_S_10 = pygame.image.load("Login_screen/10.gif").convert_alpha()
        image_ST_S_11 = pygame.image.load("Login_screen/11.gif").convert_alpha()
        image_ST_S_12 = pygame.image.load("Login_screen/12.gif").convert_alpha()
        image_ST_S_13 = pygame.image.load("Login_screen/13.gif").convert_alpha()
        image_ST_S_14 = pygame.image.load("Login_screen/14.gif").convert_alpha()
        image_ST_S_15 = pygame.image.load("Login_screen/15.gif").convert_alpha()
        image_ST_S_16 = pygame.image.load("Login_screen/16.gif").convert_alpha()
        image_ST_S_17 = pygame.image.load("Login_screen/17.gif").convert_alpha()
        image_ST_S_18 = pygame.image.load("Login_screen/18.gif").convert_alpha()
        self.image_ST_S_index = 0
        self.image_ST_S_List = [
            image_ST_S_1,
            image_ST_S_2,
            image_ST_S_3,
            image_ST_S_4,
            image_ST_S_5,
            image_ST_S_6,
            image_ST_S_7,
            image_ST_S_8,
            image_ST_S_9,
            image_ST_S_10,
            image_ST_S_11,
            image_ST_S_12,
            image_ST_S_13,
            image_ST_S_14,
            image_ST_S_15,
            image_ST_S_16,
            image_ST_S_17,
            image_ST_S_18,
        ]
        self.image = self.image_ST_S_List[int(self.image_ST_S_index)]
        self.rect = self.image.get_rect(center=(840, 525))

    def animate(self):
        if self.image_ST_S_index >= len(self.image_ST_S_List):
            self.image_ST_S_index = 0
        else:
            self.image = self.image_ST_S_List[int(self.image_ST_S_index)]
            self.image_ST_S_index += 0.15

    def update(self):
        self.animate()


class StartButton(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        image_ST_B_1 = pygame.image.load("Start/1.gif").convert_alpha()
        image_ST_B_2 = pygame.image.load("Start/2.gif").convert_alpha()
        image_ST_B_3 = pygame.image.load("Start/3.gif").convert_alpha()
        image_ST_B_4 = pygame.image.load("Start/4.gif").convert_alpha()
        image_ST_B_5 = pygame.image.load("Start/5.gif").convert_alpha()
        image_ST_B_6 = pygame.image.load("Start/6.gif").convert_alpha()
        image_ST_B_7 = pygame.image.load("Start/7.gif").convert_alpha()
        image_ST_B_8 = pygame.image.load("Start/8.gif").convert_alpha()
        image_ST_B_9 = pygame.image.load("Start/9.gif").convert_alpha()
        image_ST_B_10 = pygame.image.load("Start/10.gif").convert_alpha()
        image_ST_B_11 = pygame.image.load("Start/11.gif").convert_alpha()
        image_ST_B_12 = pygame.image.load("Start/12.gif").convert_alpha()
        image_ST_B_13 = pygame.image.load("Start/13.gif").convert_alpha()
        image_ST_B_14 = pygame.image.load("Start/14.gif").convert_alpha()
        image_ST_B_15 = pygame.image.load("Start/15.gif").convert_alpha()
        image_ST_B_16 = pygame.image.load("Start/16.gif").convert_alpha()
        image_ST_B_17 = pygame.image.load("Start/17.gif").convert_alpha()
        image_ST_B_18 = pygame.image.load("Start/18.gif").convert_alpha()
        image_ST_B_19 = pygame.image.load("Start/19.gif").convert_alpha()
        image_ST_B_20 = pygame.image.load("Start/20.gif").convert_alpha()
        image_ST_B_21 = pygame.image.load("Start/21.gif").convert_alpha()
        image_ST_B_22 = pygame.image.load("Start/22.gif").convert_alpha()
        image_ST_B_23 = pygame.image.load("Start/23.gif").convert_alpha()
        image_ST_B_24 = pygame.image.load("Start/24.gif").convert_alpha()
        image_ST_B_25 = pygame.image.load("Start/25.gif").convert_alpha()
        image_ST_B_26 = pygame.image.load("Start/26.gif").convert_alpha()
        image_ST_B_27 = pygame.image.load("Start/27.gif").convert_alpha()
        image_ST_B_28 = pygame.image.load("Start/28.gif").convert_alpha()
        image_ST_B_29 = pygame.image.load("Start/29.gif").convert_alpha()
        image_ST_B_30 = pygame.image.load("Start/30.gif").convert_alpha()

        self.image_ST_B_index = 0
        self.image_ST_B_List = [
            image_ST_B_1,
            image_ST_B_2,
            image_ST_B_3,
            image_ST_B_4,
            image_ST_B_5,
            image_ST_B_6,
            image_ST_B_7,
            image_ST_B_8,
            image_ST_B_9,
            image_ST_B_10,
            image_ST_B_11,
            image_ST_B_12,
            image_ST_B_13,
            image_ST_B_14,
            image_ST_B_15,
            image_ST_B_16,
            image_ST_B_17,
            image_ST_B_18,
            image_ST_B_19,
            image_ST_B_20,
            image_ST_B_21,
            image_ST_B_22,
            image_ST_B_23,
            image_ST_B_24,
            image_ST_B_25,
            image_ST_B_26,
            image_ST_B_27,
            image_ST_B_28,
            image_ST_B_29,
            image_ST_B_30,
        ]
        self.image = self.image_ST_B_List[int(self.image_ST_B_index)]
        self.rect = self.image.get_rect(center=(840, 525))

    def animate(self):
        if self.image_ST_B_index >= len(self.image_ST_B_List):
            self.image_ST_B_index = 0
        else:
            self.image = self.image_ST_B_List[int(self.image_ST_B_index)]
            self.image_ST_B_index += 0.15

    def update(self):
        self.animate()


class Game_BackG(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        image_BG_g_1 = pygame.image.load("Game_BG/1.gif").convert_alpha()
        image_BG_g_2 = pygame.image.load("Game_BG/2.gif").convert_alpha()
        image_BG_g_3 = pygame.image.load("Game_BG/3.gif").convert_alpha()
        image_BG_g_4 = pygame.image.load("Game_BG/4.gif").convert_alpha()
        image_BG_g_5 = pygame.image.load("Game_BG/5.gif").convert_alpha()
        image_BG_g_6 = pygame.image.load("Game_BG/6.gif").convert_alpha()
        image_BG_g_7 = pygame.image.load("Game_BG/7.gif").convert_alpha()
        image_BG_g_8 = pygame.image.load("Game_BG/8.gif").convert_alpha()
        image_BG_g_9 = pygame.image.load("Game_BG/9.gif").convert_alpha()
        image_BG_g_10 = pygame.image.load("Game_BG/10.gif").convert_alpha()
        image_BG_g_11 = pygame.image.load("Game_BG/11.gif").convert_alpha()
        image_BG_g_12 = pygame.image.load("Game_BG/12.gif").convert_alpha()
        image_BG_g_13 = pygame.image.load("Game_BG/13.gif").convert_alpha()
        image_BG_g_14 = pygame.image.load("Game_BG/14.gif").convert_alpha()
        image_BG_g_15 = pygame.image.load("Game_BG/15.gif").convert_alpha()
        image_BG_g_16 = pygame.image.load("Game_BG/16.gif").convert_alpha()
        image_BG_g_17 = pygame.image.load("Game_BG/17.gif").convert_alpha()
        image_BG_g_18 = pygame.image.load("Game_BG/18.gif").convert_alpha()
        image_BG_g_19 = pygame.image.load("Game_BG/19.gif").convert_alpha()
        image_BG_g_20 = pygame.image.load("Game_BG/20.gif").convert_alpha()
        image_BG_g_21 = pygame.image.load("Game_BG/21.gif").convert_alpha()
        image_BG_g_22 = pygame.image.load("Game_BG/22.gif").convert_alpha()
        image_BG_g_23 = pygame.image.load("Game_BG/23.gif").convert_alpha()
        image_BG_g_24 = pygame.image.load("Game_BG/24.gif").convert_alpha()
        image_BG_g_25 = pygame.image.load("Game_BG/25.gif").convert_alpha()
        image_BG_g_26 = pygame.image.load("Game_BG/26.gif").convert_alpha()
        image_BG_g_27 = pygame.image.load("Game_BG/27.gif").convert_alpha()
        image_BG_g_28 = pygame.image.load("Game_BG/28.gif").convert_alpha()
        image_BG_g_29 = pygame.image.load("Game_BG/29.gif").convert_alpha()
        image_BG_g_30 = pygame.image.load("Game_BG/30.gif").convert_alpha()
        image_BG_g_31 = pygame.image.load("Game_BG/31.gif").convert_alpha()
        image_BG_g_32 = pygame.image.load("Game_BG/32.gif").convert_alpha()
        image_BG_g_33 = pygame.image.load("Game_BG/33.gif").convert_alpha()
        image_BG_g_34 = pygame.image.load("Game_BG/34.gif").convert_alpha()
        image_BG_g_35 = pygame.image.load("Game_BG/35.gif").convert_alpha()
        image_BG_g_36 = pygame.image.load("Game_BG/36.gif").convert_alpha()
        image_BG_g_37 = pygame.image.load("Game_BG/37.gif").convert_alpha()
        image_BG_g_38 = pygame.image.load("Game_BG/38.gif").convert_alpha()
        image_BG_g_39 = pygame.image.load("Game_BG/39.gif").convert_alpha()
        image_BG_g_40 = pygame.image.load("Game_BG/40.gif").convert_alpha()
        image_BG_g_41 = pygame.image.load("Game_BG/41.gif").convert_alpha()
        image_BG_g_42 = pygame.image.load("Game_BG/42.gif").convert_alpha()
        image_BG_g_43 = pygame.image.load("Game_BG/43.gif").convert_alpha()
        image_BG_g_44 = pygame.image.load("Game_BG/44.gif").convert_alpha()
        image_BG_g_45 = pygame.image.load("Game_BG/45.gif").convert_alpha()
        image_BG_g_46 = pygame.image.load("Game_BG/46.gif").convert_alpha()
        image_BG_g_47 = pygame.image.load("Game_BG/47.gif").convert_alpha()
        image_BG_g_48 = pygame.image.load("Game_BG/48.gif").convert_alpha()
        image_BG_g_49 = pygame.image.load("Game_BG/49.gif").convert_alpha()
        image_BG_g_50 = pygame.image.load("Game_BG/50.gif").convert_alpha()
        image_BG_g_51 = pygame.image.load("Game_BG/51.gif").convert_alpha()
        image_BG_g_52 = pygame.image.load("Game_BG/52.gif").convert_alpha()
        image_BG_g_53 = pygame.image.load("Game_BG/53.gif").convert_alpha()
        image_BG_g_54 = pygame.image.load("Game_BG/54.gif").convert_alpha()

        self.image_BG_g_index = 0
        self.image_BG_g_List = [
            image_BG_g_1,
            image_BG_g_2,
            image_BG_g_3,
            image_BG_g_4,
            image_BG_g_5,
            image_BG_g_6,
            image_BG_g_7,
            image_BG_g_8,
            image_BG_g_9,
            image_BG_g_10,
            image_BG_g_11,
            image_BG_g_12,
            image_BG_g_13,
            image_BG_g_14,
            image_BG_g_15,
            image_BG_g_16,
            image_BG_g_17,
            image_BG_g_18,
            image_BG_g_19,
            image_BG_g_20,
            image_BG_g_21,
            image_BG_g_22,
            image_BG_g_23,
            image_BG_g_24,
            image_BG_g_25,
            image_BG_g_26,
            image_BG_g_27,
            image_BG_g_28,
            image_BG_g_29,
            image_BG_g_30,
            image_BG_g_31,
            image_BG_g_32,
            image_BG_g_33,
            image_BG_g_34,
            image_BG_g_35,
            image_BG_g_36,
            image_BG_g_37,
            image_BG_g_38,
            image_BG_g_39,
            image_BG_g_40,
            image_BG_g_41,
            image_BG_g_42,
            image_BG_g_43,
            image_BG_g_44,
            image_BG_g_45,
            image_BG_g_46,
            image_BG_g_47,
            image_BG_g_48,
            image_BG_g_49,
            image_BG_g_50,
            image_BG_g_51,
            image_BG_g_52,
            image_BG_g_53,
            image_BG_g_54,
        ]
        self.image = self.image_BG_g_List[int(self.image_BG_g_index)]
        self.image = pygame.transform.scale(self.image, (1680, 1050))
        self.rect = self.image.get_rect(midtop=(840, 0))

    def animate(self):
        if self.image_BG_g_index >= len(self.image_BG_g_List):
            self.image_BG_g_index = 0
        else:
            self.image = self.image_BG_g_List[int(self.image_BG_g_index)]
            self.image = pygame.transform.scale(self.image, (1680, 1050))
            self.rect = self.image.get_rect(midtop=(840, 0))
            self.image_BG_g_index += 0.25

    def update(self):
        self.animate()


class Draw_Ground:
    def __init__(self) -> None:
        image_BG_g_55 = pygame.transform.scale(
            pygame.image.load("Game_BG/x2.jpg"), (1680, 200)
        ).convert_alpha()
        image_BG_g_56 = pygame.transform.scale(
            pygame.image.load("Game_BG/x1.jpg"), (1680, 200)
        ).convert_alpha()
        image_BG_g_list = [image_BG_g_55, image_BG_g_56]
        self.image_1 = image_BG_g_list[0]
        self.image_1 = pygame.transform.scale(self.image_1, (1680, 1050))
        self.rect_1 = self.image_1.get_rect(bottomleft=(0, 1050))

        self.image_2 = image_BG_g_list[1]
        self.image_2 = pygame.transform.scale(self.image_2, (1680, 1050))
        self.rect_2 = self.image_2.get_rect(bottomleft=(1680, 1050))

    def movment(self, surface):
        self.rect_1.right -= 4
        self.rect_2.left -= 4
        if self.rect_1.right == 0 and self.rect_2.left == 0:
            self.rect_1.left = 1680
        elif self.rect_2.right == 0 and self.rect_1.left == 0:
            self.rect_2.left = 1680
        surface.blit(self.image_1, self.rect_1)
        surface.blit(self.image_2, self.rect_2)


class Flying_Grounds(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        image_GF_Big1 = pygame.transform.scale(
            pygame.image.load("Landing_Floors/Big1.png"), (1500, 300)
        ).convert_alpha()
        image_GF_Big2 = pygame.transform.scale(
            pygame.image.load("Landing_Floors/Big2.png"), (1200, 300)
        ).convert_alpha()
        image_GF_Big3 = pygame.transform.scale(
            pygame.image.load("Landing_Floors/Big3.png"), (980, 300)
        ).convert_alpha()
        self.image_list = [image_GF_Big1, image_GF_Big2, image_GF_Big3]
        self.image = self.image_list[randint(0, 2)]
        self.rect = self.image.get_rect(topleft=(randint(1750, 1900), 450))
        self.mask = pygame.mask.from_surface(self.image)

    def destroy(self):
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.rect.x -= 3
        self.destroy()
