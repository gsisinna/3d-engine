# src/ecs/combat_component.py
from src.ecs.component import Component

class CombatComponent(Component):
    def __init__(self, entity_id: int, attack_damage: int, defense: int):
        super().__init__(entity_id)
        self.attack_damage = attack_damage
        self.defense = defense

    def attack(self, target_entity):
        """Attack another entity, reducing its health based on attack and defense."""
        target_health = target_entity.get_component('HealthComponent')
        if target_health:
            damage = max(0, self.attack_damage - target_entity.defense)
            target_health.take_damage(damage)

    def update(self):
        """Update combat (e.g., check cooldowns, apply buffs)."""
        pass

    def __repr__(self):
        return f"CombatComponent({self.entity_id}, Damage: {self.attack_damage}, Defense: {self.defense})"
