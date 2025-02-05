import pytest
from typeguard import check_type
import pygame

from project import (
    New_User,
    Get_User,
    Update_User,
    Score_f,
    print_const_text,
    BoundaryError,
)


def test_New_User():
    with pytest.raises(TypeError):
        check_type("New_User", New_User, 123, "asds")


def test_Get_User():
    with pytest.raises(TypeError):
        check_type("Get_User", Get_User, 123)


def test_Update_User():
    with pytest.raises(TypeError):
        check_type("Update_User", Update_User, 123, "asds")


def test_Score_f():
    with pytest.raises(TypeError):
        check_type("Score_f", Score_f, 123, 123.5)


def test_print_const_text():
    surface = pygame.Surface((300, 300))
    pygame.init()
    with pytest.raises(BoundaryError):
        print_const_text(surface, "asdasdgrety")
