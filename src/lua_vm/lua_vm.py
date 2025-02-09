# src/lua_vm/lua_vm.py
import cffi

ffi = cffi.FFI()

# Load LuaJIT dynamically
lua = ffi.dlopen("libluajit-5.1.so")  # Adjust path based on where you found the library

ffi.cdef("""
    typedef void lua_State;
    lua_State* luaL_newstate();
    void luaL_openlibs(lua_State* L);
    int luaL_dostring(lua_State* L, const char* str);
    void lua_close(lua_State* L);
""")

class LuaVM:
    def __init__(self):
        self.L = lua.luaL_newstate()
        lua.luaL_openlibs(self.L)

    def execute(self, code: str):
        if lua.luaL_dostring(self.L, code.encode('utf-8')) != 0:
            print("Lua Error")

    def close(self):
        lua.lua_close(self.L)
