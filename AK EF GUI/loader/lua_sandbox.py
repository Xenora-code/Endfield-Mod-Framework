from lupa import LuaRuntime

def run_lua_script(script_path):
    lua = LuaRuntime(unpack_returned_tuples=True)

    lua.globals().print = print

    with open(script_path, "r", encoding="utf-8") as f:
        lua.execute(f.read())
