# src/ecs/position_component.py
from src.ecs.component import Component

class PositionComponent(Component):
    def __init__(self, entity_id: int, x: float, y: float):
        super().__init__(entity_id)
        self.x = x
        self.y = y

    def update(self):
        """Update the position (could be moved by velocity or input)."""
        pass

    def __repr__(self):
        return f"PositionComponent({self.entity_id}, {self.x}, {self.y})"
