import os
import datetime


def logger(path):
    
    file_path = path
    
    def __logger(old_function):
        def new_function(*args, **kwargs):
            
            with open(file_path, 'a') as file: 
                file.write(f'Start date and time: {datetime.datetime.now()}\n')
                file.write(f'Name function: {old_function}\n')
                file.write(f'Positional parametrs: {args}\n')
                file.write(f'Named parametrs: {kwargs}\n')
                rez = old_function(*args, **kwargs)
                file.write(f'Result: {rez}\n\n')
            return rez

        return new_function

    return __logger