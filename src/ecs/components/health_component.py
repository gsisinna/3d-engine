# src/ecs/health_component.py
from src.ecs.component import Component

class HealthComponent(Component):
    def __init__(self, entity_id: int, health: int, max_health: int):
        super().__init__(entity_id)
        self.health = health
        self.max_health = max_health

    def take_damage(self, damage: int):
        """Reduce health by damage amount."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount: int):
        """Heal the entity by a certain amount."""
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def update(self):
        """Update health (e.g., check for death, healing over time)."""
        pass

    def __repr__(self):
        return f"HealthComponent({self.entity_id}, {self.health}/{self.max_health})"
