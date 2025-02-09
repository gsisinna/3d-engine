# src/ecs/inventory_component.py
from src.ecs.component import Component

class InventoryComponent(Component):
    def __init__(self, entity_id: int):
        super().__init__(entity_id)
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def remove_item(self, item):
        """Remove an item from the inventory."""
        if item in self.items:
            self.items.remove(item)

    def update(self):
        """Update inventory (e.g., remove expired items, handle use)."""
        pass

    def __repr__(self):
        return f"InventoryComponent({self.entity_id}, {len(self.items)} items)"
