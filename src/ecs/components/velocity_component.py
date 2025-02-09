# src/ecs/velocity_component.py
from src.ecs.component import Component

class VelocityComponent(Component):
    def __init__(self, entity_id: int, vx: float, vy: float):
        super().__init__(entity_id)
        self.vx = vx
        self.vy = vy

    def update(self):
        """Update the velocity (could be influenced by player input or physics)."""
        pass

    def __repr__(self):
        return f"VelocityComponent({self.entity_id}, {self.vx}, {self.vy})"
