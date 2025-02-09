#!/bin/bash

# Set up the main project directory
PROJECT_NAME="3d-engine"
mkdir $PROJECT_NAME
cd $PROJECT_NAME

# Create the main directories
mkdir -p assets/{models,textures,shaders}
mkdir -p src/{ecs,renderer,physics,lua_vm,game,utils}
mkdir -p tests
mkdir -p assets_manager
mkdir -p docs

# Create basic files for documentation
touch docs/architecture.md
touch docs/setup.md
touch docs/usage.md
echo "# 3D Game Engine" > README.md
echo "This is a 3D game engine for an RPG game using Python, OpenGL, Bullet, and Lua." >> README.md

# Create .gitignore file
echo "__pycache__/" > .gitignore
echo "venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "*.pyo" >> .gitignore
echo "*.pyd" >> .gitignore
echo "*/__pycache__/" >> .gitignore
echo ".DS_Store" >> .gitignore

# Create the requirements.txt file
echo "cffi>=1.15.0" > requirements.txt
echo "pybullet>=3.0.8" >> requirements.txt
echo "pyopengl>=3.1.6" >> requirements.txt
echo "glfw>=2.5.0" >> requirements.txt

# Create the config.py file
touch config.py
echo "# Configuration for the game engine" > config.py
echo "SCREEN_WIDTH = 800" >> config.py
echo "SCREEN_HEIGHT = 600" >> config.py
echo "FPS = 60" >> config.py

# Create main.py
touch main.py
echo "from src.game.game import Game" > main.py
echo "def main():" >> main.py
echo "    game = Game()" >> main.py
echo "    game.run()" >> main.py
echo "if __name__ == '__main__':" >> main.py
echo "    main()" >> main.py

# Create the ECS files
touch src/ecs/{__init__.py,entity.py,component.py,system.py,manager.py,lua_integration.py}
echo "class Entity:" > src/ecs/entity.py
echo "    _id_counter = 0" >> src/ecs/entity.py
echo "    def __init__(self):" >> src/ecs/entity.py
echo "        self.id = Entity._id_counter" >> src/ecs/entity.py
echo "        Entity._id_counter += 1" >> src/ecs/entity.py

echo "class Component:" > src/ecs/component.py
echo "    pass" >> src/ecs/component.py

echo "class System:" > src/ecs/system.py
echo "    def update(self, entities):" >> src/ecs/system.py
echo "        pass" >> src/ecs/system.py

echo "class Manager:" > src/ecs/manager.py
echo "    def __init__(self):" >> src/ecs/manager.py
echo "        self.entities = []" >> src/ecs/manager.py
echo "        self.components = {}" >> src/ecs/manager.py
echo "    def create_entity(self):" >> src/ecs/manager.py
echo "        entity = Entity()" >> src/ecs/manager.py
echo "        self.entities.append(entity)" >> src/ecs/manager.py
echo "        return entity" >> src/ecs/manager.py
echo "    def add_component(self, entity, component):" >> src/ecs/manager.py
echo "        self.components.setdefault(entity.id, []).append(component)" >> src/ecs/manager.py
echo "    def get_components(self, entity):" >> src/ecs/manager.py
echo "        return self.components.get(entity.id, [])" >> src/ecs/manager.py
echo "    def update(self):" >> src/ecs/manager.py
echo "        for system in self.systems:" >> src/ecs/manager.py
echo "            system.update(self.entities)" >> src/ecs/manager.py

echo "class LuaECSIntegration:" > src/ecs/lua_integration.py
echo "    def __init__(self, lua_vm):" >> src/ecs/lua_integration.py
echo "        self.lua_vm = lua_vm" >> src/ecs/lua_integration.py
echo "        self.manager = Manager()" >> src/ecs/lua_integration.py
echo "    def create_entity_from_lua(self, lua_code):" >> src/ecs/lua_integration.py
echo "        entity = self.manager.create_entity()" >> src/ecs/lua_integration.py
echo "        self.lua_vm.execute(lua_code)" >> src/ecs/lua_integration.py
echo "        return entity" >> src/ecs/lua_integration.py

# Create the Renderer files
touch src/renderer/{__init__.py,renderer.py,shaders.py}
echo "import glfw" > src/renderer/renderer.py
echo "from OpenGL.GL import *" >> src/renderer/renderer.py
echo "from OpenGL.GL.shaders import compileProgram, compileShader" >> src/renderer/renderer.py
echo "class Renderer:" >> src/renderer/renderer.py
echo "    def __init__(self):" >> src/renderer/renderer.py
echo "        if not glfw.init():" >> src/renderer/renderer.py
echo "            raise Exception('GLFW can not be initialized!')" >> src/renderer/renderer.py
echo "        self.window = glfw.create_window(800, 600, '3D Game Engine', None, None)" >> src/renderer/renderer.py
echo "        if not self.window:" >> src/renderer/renderer.py
echo "            glfw.terminate()" >> src/renderer/renderer.py
echo "            raise Exception('GLFW window can not be created!')" >> src/renderer/renderer.py
echo "        glfw.make_context_current(self.window)" >> src/renderer/renderer.py
echo "    def start(self):" >> src/renderer/renderer.py
echo "        while not glfw.window_should_close(self.window):" >> src/renderer/renderer.py
echo "            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)" >> src/renderer/renderer.py
echo "            self.render()" >> src/renderer/renderer.py
echo "            glfw.swap_buffers(self.window)" >> src/renderer/renderer.py
echo "            glfw.poll_events()" >> src/renderer/renderer.py
echo "    def render(self):" >> src/renderer/renderer.py
echo "        pass" >> src/renderer/renderer.py

# Create Physics file
touch src/physics/physics.py
echo "import pybullet as p" > src/physics/physics.py
echo "class PhysicsSystem:" >> src/physics/physics.py
echo "    def __init__(self):" >> src/physics/physics.py
echo "        self.physics_client = p.connect(p.DIRECT)" >> src/physics/physics.py
echo "    def simulate(self):" >> src/physics/physics.py
echo "        p.stepSimulation()" >> src/physics/physics.py
echo "    def add_rigid_body(self, body):" >> src/physics/physics.py
echo "        p.createMultiBody(baseMass=1, basePosition=[0, 0, 1])" >> src/physics/physics.py

# Create Lua VM file
touch src/lua_vm/lua_vm.py
echo "import cffi" > src/lua_vm/lua_vm.py
echo "ffi = cffi.FFI()" >> src/lua_vm/lua_vm.py
echo "lua = ffi.dlopen('libluajit-5.1.so')" >> src/lua_vm/lua_vm.py
echo "ffi.cdef(\"\"" >> src/lua_vm/lua_vm.py
echo "    typedef void lua_State;" >> src/lua_vm/lua_vm.py
echo "    lua_State* luaL_newstate();" >> src/lua_vm/lua_vm.py
echo "    void luaL_openlibs(lua_State* L);" >> src/lua_vm/lua_vm.py
echo "    int luaL_dostring(lua_State* L, const char* str);" >> src/lua_vm/lua_vm.py
echo "    void lua_close(lua_State* L);" >> src/lua_vm/lua_vm.py
echo "\"\"" >> src/lua_vm/lua_vm.py
echo "class LuaVM:" >> src/lua_vm/lua_vm.py
echo "    def __init__(self):" >> src/lua_vm/lua_vm.py
echo "        self.L = lua.luaL_newstate()" >> src/lua_vm/lua_vm.py
echo "        lua.luaL_openlibs(self.L)" >> src/lua_vm/lua_vm.py
echo "    def execute(self, code: str):" >> src/lua_vm/lua_vm.py
echo "        if lua.luaL_dostring(self.L, code.encode('utf-8')) != 0:" >> src/lua_vm/lua_vm.py
echo "            print('Lua Error')" >> src/lua_vm/lua_vm.py
echo "    def close(self):" >> src/lua_vm/lua_vm.py
echo "        lua.lua_close(self.L)" >> src/lua_vm/lua_vm.py

# Create Game file
touch src/game/game.py
echo "class Game:" > src/game/game.py
echo "    def __init__(self):" >> src/game/game.py
echo "        pass" >> src/game/game.py
echo "    def run(self):" >> src/game/game.py
echo "        pass" >> src/game/game.py

# Create the tests
touch tests/{test_renderer.py,test_physics.py,test_ecs.py,test_lua_vm.py}
echo "def test_renderer():" > tests/test_renderer.py
echo "    pass" >> tests/test_renderer.py

echo "def test_physics():" > tests/test_physics.py
echo "    pass" >> tests/test_physics.py

echo "def test_ecs():" > tests/test_ecs.py
echo "    pass" >> tests/test_ecs.py

echo "def test_lua_vm():" > tests/test_lua_vm.py
echo "    pass" >> tests/test_lua_vm.py

# Create the assets manager files
touch assets_manager/{__init__.py,asset_loader.py,texture_manager.py}
echo "class AssetLoader:" > assets_manager/asset_loader.py
echo "    pass" >> assets_manager/asset_loader.py

echo "class TextureManager:" > assets_manager/texture_manager.py
echo "    pass" >> assets_manager/texture_manager.py

echo "Setup complete! Project structure is ready!"
