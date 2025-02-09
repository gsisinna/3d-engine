# src/ecs/manager.py
from src.ecs.entity import Entity  # Add this import

class Manager:
    def __init__(self):
        self.entities = {}
        self.next_entity_id = 1

    def create_entity(self):
        """Create a new entity and assign it a unique entity ID."""
        entity_id = self.next_entity_id
        self.next_entity_id += 1
        entity = Entity(entity_id)  # Now, `Entity` is defined
        self.entities[entity_id] = entity
        return entity

    def add_component(self, entity, component):
        """Add a component to an entity."""
        entity.add_component(component)
