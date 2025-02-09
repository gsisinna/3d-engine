# src/ecs/component.py

class Component:
    def __init__(self, entity_id: int):
        """Initialize the component with the associated entity ID."""
        self.entity_id = entity_id

    def update(self):
        """This method will be called every frame to update the component's state."""
        pass

    def __repr__(self):
        """String representation of the component."""
        return f"{self.__class__.__name__}({self.entity_id})"
