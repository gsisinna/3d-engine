# src/assets/asset_loader.py
import os
import json
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from pygame.image import load as load_image

class AssetLoader:
    def __init__(self):
        self.textures = {}
        self.models = {}
        self.sounds = {}

    def load_texture(self, path: str):
        """Load texture from file and return OpenGL texture ID."""
        if path in self.textures:
            return self.textures[path]
        
        texture = pygame.image.load(path)
        texture_data = pygame.image.tostring(texture, "RGBA", 1)

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texture.get_width(), texture.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
        glGenerateMipmap(GL_TEXTURE_2D)
        
        self.textures[path] = texture_id
        return texture_id

    def load_model(self, path: str):
        """Load 3D model (e.g., .obj format). Placeholder for actual model loading."""
        if path in self.models:
            return self.models[path]

        model = self._load_obj_model(path)
        self.models[path] = model
        return model

    def _load_obj_model(self, path: str):
        """Placeholder for loading .obj files."""
        # You can integrate a proper OBJ loader here (e.g., PyWavefront)
        # For now, it's a dummy placeholder
        print(f"Loading model from {path}")
        return {}

    def load_sound(self, path: str):
        """Load sound from file."""
        if path in self.sounds:
            return self.sounds[path]

        sound = pygame.mixer.Sound(path)
        self.sounds[path] = sound
        return sound

    def load_json(self, path: str):
        """Load JSON asset for configuration or other purposes."""
        if os.path.exists(path):
            with open(path, 'r') as f:
                return json.load(f)
        else:
            print(f"Error: File {path} does not exist.")
            return None
