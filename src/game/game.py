# src/game/game.py
from src.renderer.renderer import Renderer
from src.physics.physics import PhysicsSystem
from src.ecs.manager import Manager
from src.lua_vm.lua_vm import LuaVM
from src.ecs.components.position_component import PositionComponent  # Import the component

class Game:
    def __init__(self):
        self.renderer = Renderer()
        self.physics = PhysicsSystem()
        self.ecs_manager = Manager()
        self.lua_vm = LuaVM()

    def run(self):
        # Example: Creating an entity and attaching components
        player = self.ecs_manager.create_entity()
        self.ecs_manager.add_component(player, PositionComponent(player.entity_id, x=0, y=0))  # Corrected
        while True:
            self.physics.simulate()
            self.renderer.start()
