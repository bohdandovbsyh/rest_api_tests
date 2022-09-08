import os

if not os.system('mypy mypy_and_anotations.py'):
    os.system('python mypy_and_anotations.py')
