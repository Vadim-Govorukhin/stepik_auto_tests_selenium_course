import os 

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
print(__file__)
print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))