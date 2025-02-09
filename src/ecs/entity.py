# src/ecs/entity.py

class Entity:
    def __init__(self, entity_id: int):
        """Initialize the entity with a unique entity ID."""
        self.entity_id = entity_id  # This should be initialized here.
        self.components = {}

    def add_component(self, component):
        """Attach a component to this entity."""
        self.components[component.__class__.__name__] = component

    def get_component(self, component_class):
        """Get a component by its class."""
        return self.components.get(component_class.__name__)

    def __repr__(self):
        """String representation of the entity."""
        return f"Entity({self.entity_id})"
