import os
import pygame

sprites = {}
audios = {}


def load_sprites():
    path = os.path.join("assets", "images")
    for file in os.listdir(path):
        sprites[file.split(".")[0]] = pygame.image.load(os.path.join(path, file))


def get_sprites(name):
    return sprites[name]

def load_audio():
    path = os.path.join("assets", "audio")
    for file in os.listdir(path):
        audios[file.split(".")[0]] = os.path.join(path, file)
    

def get_audio(name):
    return audios[name]

