import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image_Player_List = [
            pygame.image.load(f"Player/{index}.gif").convert_alpha()
            for index in range(1, 15)
        ]
        self.image_Player_jump = pygame.image.load("Player/9.gif").convert_alpha()
        self.image_Player_index = 0
        self.gravity = 0
        self.image = self.image_Player_List[int(self.image_Player_index)]
        self.image = pygame.transform.scale(self.image, (589, 221))
        self.rect = self.image.get_rect(bottomleft=(-50, 860))
        self.mask = pygame.mask.from_surface(self.image)
        # F_Lsprite.rect.top = 450
        self.limiter = 600
        self.flag = False
        self.jump_sound = pygame.mixer.Sound("Audio/jump.mp3")
        self.jump_sound.set_volume(1)  # use a value between 0 and 1

    def jump_check(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and (
            self.rect.bottom >= 860 or self.rect.bottom == self.limiter
        ):
            self.gravity = -27
            self.jump_sound.play()

    def jumping(self):
        if not self.flag:
            self.rect.y += self.gravity
            self.gravity += 1
            if self.rect.right < 1680 and self.rect.bottom < 860:
                self.rect.x += 7
            elif self.rect.left >= -50:
                self.rect.x -= 7
            if self.rect.bottom >= 860:
                self.rect.bottom = 860
        else:
            self.rect.y += self.gravity
            self.gravity += 1
            if self.rect.right < 1680 and self.rect.bottom < self.limiter:
                self.rect.x += 7
            elif self.rect.left >= -50:
                self.rect.x -= 7
            if self.rect.bottom >= self.limiter:
                self.rect.bottom = self.limiter

    def animate(self):
        if not self.flag:
            if self.rect.bottom < 860:
                self.image = self.image_Player_jump
                self.image = pygame.transform.scale(self.image, (589, 221))
            elif self.image_Player_index >= len(self.image_Player_List):
                self.image_Player_index = 0
            else:
                self.image = self.image_Player_List[int(self.image_Player_index)]
                self.image = pygame.transform.scale(self.image, (589, 221))
                self.image_Player_index += 0.25
        else:
            if self.rect.bottom < self.limiter:
                self.image = self.image_Player_jump
                self.image = pygame.transform.scale(self.image, (589, 221))
            elif self.image_Player_index >= len(self.image_Player_List):
                self.image_Player_index = 0
            else:
                self.image = self.image_Player_List[int(self.image_Player_index)]
                self.image = pygame.transform.scale(self.image, (589, 221))
                self.image_Player_index += 0.25

    def update(self):
        if self.rect.bottom == self.limiter:
            self.flag = True
        else:
            self.flag = False
        self.jump_check()
        self.jumping()
        self.animate()


class Enemy_T(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image_Enemy_T_List = [
            pygame.image.load(f"Enemy_1/{index}.gif").convert_alpha()
            for index in range(1, 19)
        ]
        self.image_Enemy_T_index = 0
        self.image = self.image_Enemy_T_List[int(self.image_Enemy_T_index)]
        self.image = pygame.transform.scale(self.image, (413, 154))
        self.rect = self.image.get_rect(bottomleft=(1880, 850))
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        if self.image_Enemy_T_index >= len(self.image_Enemy_T_List):
            self.image_Enemy_T_index = 0
        else:
            self.image = self.image_Enemy_T_List[int(self.image_Enemy_T_index)]
            self.image = pygame.transform.scale(self.image, (413, 154))
            self.image_Enemy_T_index += 0.4

    def destroy(self):
        if self.rect.x < -100:
            # which is a sprite method that delete the sprite once called
            self.kill()

    def update(self):
        self.rect.x -= 12
        self.destroy()
        self.animate()


class cloud:
    def __init__(self, x: int, y: int) -> None:
        self.x_coord = x
        self.y_coord = y
        self.image_Cloud_List = [
            pygame.image.load(f"Fight_Cloud/{index}.gif").convert_alpha()
            for index in range(1, 19)
        ]
        self.image_Cloud_index = 0
        self.image = self.image_Cloud_List[int(self.image_Cloud_index)]
        self.image = pygame.transform.scale(self.image, (413, 154))
        self.rect = self.image.get_rect(center=(self.x_coord, self.y_coord))

    def animate(self, surface):
        if self.image_Cloud_index >= len(self.image_Cloud_List):
            self.image_Cloud_index = 0
        else:
            self.image = self.image_Cloud_List[int(self.image_Cloud_index)]
            self.image = pygame.transform.scale(self.image, (413, 154))
            self.image_Cloud_index += 1.5
        surface.blit(self.image, self.rect)


class heart_D:
    def __init__(self) -> None:
        self.image_H_1 = pygame.image.load("Decreasing_hearts/1.gif").convert_alpha()
        self.image_H_2 = pygame.image.load("Decreasing_hearts/2.gif").convert_alpha()
        self.image_H_3 = pygame.image.load("Decreasing_hearts/3.gif").convert_alpha()
        self.image_H_4 = pygame.image.load("Decreasing_hearts/4.gif").convert_alpha()
        self.image_H_5 = pygame.image.load("Decreasing_hearts/5.gif").convert_alpha()
        self.image_H_6 = pygame.image.load("Decreasing_hearts/6.gif").convert_alpha()
        self.image_H_7 = pygame.image.load("Decreasing_hearts/7.gif").convert_alpha()
        self.image_H_8 = pygame.image.load("Decreasing_hearts/8.gif").convert_alpha()
        self.image_H_9 = pygame.image.load("Decreasing_hearts/9.gif").convert_alpha()
        self.image_H_10 = pygame.image.load("Decreasing_hearts/10.gif").convert_alpha()

        self.rect_H = self.image_H_1.get_rect(topleft=(25, 5))

        self.image_Lossof3heart_List = [self.image_H_2, self.image_H_3, self.image_H_4]
        self.image_Lossof2heart_List = [self.image_H_5, self.image_H_6, self.image_H_7]
        self.image_Lossof1heart_List = [self.image_H_8, self.image_H_9, self.image_H_10]
        self.image_Lossof0heart_List = [self.image_H_8, self.image_H_10]

        self.image_Lossof3heart_index = 0
        self.image_Lossof2heart_index = 0
        self.image_Lossof1heart_index = 0
        self.image_Lossof0heart_index = 0

    def animate(self, hearts, surface):
        # couldnt use match cause i dont have python 3.10
        if hearts == 3:
            surface.blit(self.image_H_1, self.rect_H)
        elif hearts == 2:
            if self.image_Lossof3heart_index < len(self.image_Lossof3heart_List):
                self.image = self.image_Lossof3heart_List[
                    int(self.image_Lossof3heart_index)
                ]
                self.image_Lossof3heart_index += 0.1
                self.rect_H_3 = self.image.get_rect(topleft=(25, 5))
            surface.blit(self.image, self.rect_H_3)
        elif hearts == 1:
            if self.image_Lossof2heart_index < len(self.image_Lossof2heart_List):
                self.image = self.image_Lossof2heart_List[
                    int(self.image_Lossof2heart_index)
                ]
                self.image_Lossof2heart_index += 0.1
                self.rect_H_2 = self.image.get_rect(topleft=(25, 5))
            surface.blit(self.image, self.rect_H_2)
        elif hearts == 0:
            if self.image_Lossof1heart_index < len(self.image_Lossof1heart_List):
                self.image = self.image_Lossof1heart_List[
                    int(self.image_Lossof1heart_index)
                ]
                self.image_Lossof1heart_index += 0.1
                self.rect_H_1 = self.image.get_rect(topleft=(25, 5))
            surface.blit(self.image, self.rect_H_1)

    def update_heart(self, surface, hearts):
        if hearts == 3:
            rectx = self.image_H_1.get_rect(topleft=(25, 5))
            surface.blit(self.image_H_1, rectx)
        elif hearts == 2:
            rectx = self.image_H_4.get_rect(topleft=(25, 5))
            surface.blit(self.image_H_4, rectx)
        elif hearts == 1:
            rectx = self.image_H_7.get_rect(topleft=(25, 5))
            surface.blit(self.image_H_7, rectx)
        elif hearts == 0:
            if self.image_Lossof0heart_index >= len(self.image_Lossof0heart_List):
                self.image_Lossof0heart_index = 0
            else:
                self.image = self.image_Lossof0heart_List[
                    int(self.image_Lossof0heart_index)
                ]
                self.image_Lossof0heart_index += 0.25
                self.rect_H_0 = self.image.get_rect(topleft=(25, 5))
            surface.blit(self.image, self.rect_H_0)


class Bonus_F(pygame.sprite.Sprite):
    def __init__(self, yindex) -> None:
        super().__init__()
        self.image_Bonus_F_List = [
            pygame.image.load(f"Bonus/y ({index}).gif").convert_alpha()
            for index in range(1, 126)
        ]
        self.image_Bonus_F_index = 0
        self.image = self.image_Bonus_F_List[int(self.image_Bonus_F_index)]
        self.image = pygame.transform.scale(self.image, (160, 140))
        self.rect = self.image.get_rect(bottomleft=(1880, yindex))
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        if self.image_Bonus_F_index >= len(self.image_Bonus_F_List):
            self.image_Bonus_F_index = 0
        else:
            self.image = self.image_Bonus_F_List[int(self.image_Bonus_F_index)]
            self.image = pygame.transform.scale(self.image, (160, 140))
            self.image_Bonus_F_index += 0.25

    def destroy(self):
        if self.rect.x < -100:
            # which is a sprite method that delete the sprite once called
            self.kill()

    def update(self):
        self.rect.x -= 4
        self.destroy()
        self.animate()


class Sparkle_F(pygame.sprite.Sprite):
    def __init__(self, yindex) -> None:
        super().__init__()
        self.image_Sparkle_F_List = [
            pygame.image.load(f"Sparkle/x ({index}).gif").convert_alpha()
            for index in range(1, 251)
        ]
        self.image_Sparkle_F_index = 0
        self.image = self.image_Sparkle_F_List[int(self.image_Sparkle_F_index)]
        self.image = pygame.transform.scale(self.image, (133, 100))
        self.rect = self.image.get_rect(bottomleft=(1880, yindex))
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        if self.image_Sparkle_F_index >= len(self.image_Sparkle_F_List):
            self.image_Sparkle_F_index = 0
        else:
            self.image = self.image_Sparkle_F_List[int(self.image_Sparkle_F_index)]
            self.image = pygame.transform.scale(self.image, (133, 100))
            self.image_Sparkle_F_index += 0.25

    def destroy(self):
        if self.rect.x < -100:
            # which is a sprite method that delete the sprite once called
            self.kill()

    def update(self):
        self.rect.x -= 4
        self.destroy()
        self.animate()


class Score_Boost(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image_SB_List = [
            pygame.image.load(f"Score_Booster/z ({index}).gif").convert_alpha()
            for index in range(1, 38)
        ]
        self.image_SB_index = 0
        self.image = self.image_SB_List[int(self.image_SB_index)]
        self.image = pygame.transform.scale(self.image, (103, 160))
        self.rect = self.image.get_rect(bottomleft=(1880, 300))
        self.mask = pygame.mask.from_surface(self.image)

    def animate(self):
        if self.image_SB_index >= len(self.image_SB_List):
            self.image_SB_index = 0
        else:
            self.image = self.image_SB_List[int(self.image_SB_index)]
            self.image = pygame.transform.scale(self.image, (103, 160))
            self.image_SB_index += 0.25

    def destroy(self):
        if self.rect.x < -100:
            # which is a sprite method that delete the sprite once called
            self.kill()

    def update(self):
        self.rect.x -= 7
        self.destroy()
        self.animate()
