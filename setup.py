from cx_Freeze import setup, Executable

setup(name='scratch',
      version='0.1',
      description='test file',
      executables = [Executable('scratch.py')])

