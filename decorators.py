from datetime import datetime
import os


def logger(func):
    """
    Для использования данного декоратора необходимо импортировать модули datetime и os
    :param func:
    :return:
    """
    LOGS_DIR = os.getcwd()
    def decor(*args, **kwargs):
        something = func(*args, **kwargs)
        func_name = f'Loging function {func.__name__}.txt'
        LOGS_PATH = os.path.join(LOGS_DIR, func_name)
        with open(func_name, 'a', encoding='utf-8') as file:
            time_now = [i for i in datetime.timetuple(datetime.now())]
            file.writelines(f'Time call function: {time_now[3]}:{time_now[4]}:{time_now[5]}\n')
            file.writelines(f'Name function: {func.__name__}\n')
            file.writelines(f'Arguments in call function: {[arg for arg in args]}\n')
            file.writelines(f'Return value: {something}\n')
            print(LOGS_PATH)
        return something
    return decor
