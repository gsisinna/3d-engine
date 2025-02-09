# src/ecs/lua_integration.py
class LuaECSIntegration:
    def __init__(self, lua_vm, ecs_manager):
        self.lua_vm = lua_vm
        self.ecs_manager = ecs_manager

    def create_entity_from_lua(self, lua_code):
        entity = self.ecs_manager.create_entity()
        self.lua_vm.execute(lua_code)  # Execute Lua script to interact with entity
        return entity
