from cx_Freeze import setup, Executable
setup( name = "exp.py",
       version = "1.1",
       description = "Description of the app here.",
       executables = [Executable("exp.py")]
     )
