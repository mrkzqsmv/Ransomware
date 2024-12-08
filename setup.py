from cx_Freeze import setup, Executable

# Setup script to build the executable
setup(
    name="MyApp",
    version="1.0",
    description="Python to ELF",
    executables=[Executable("main_v2.py", target="my_app")]  # targetName -> target
)