# src/assets/texture_manager.py
from OpenGL.GL import *
import pygame
from pygame.image import load as load_image
from src.assets.asset_loader import AssetLoader

class TextureManager:
    def __init__(self):
        self.asset_loader = AssetLoader()
        self.textures = {}

    def load_texture(self, path: str):
        """Load texture from file, cache it, and return OpenGL texture ID."""
        if path in self.textures:
            return self.textures[path]

        texture_id = self.asset_loader.load_texture(path)
        self.textures[path] = texture_id
        return texture_id

    def bind_texture(self, texture_id):
        """Bind a texture to the OpenGL context."""
        glBindTexture(GL_TEXTURE_2D, texture_id)

    def set_texture_parameters(self):
        """Set default texture parameters (e.g., filtering, wrapping)."""
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    def clear_textures(self):
        """Clear loaded textures cache."""
        self.textures.clear()
