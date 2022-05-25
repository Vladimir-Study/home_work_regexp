from datetime import datetime
import os


def logger(func):
    """
    Для использования данного декоратора необходимо импортировать модули datetime и os
    :param func:
    :return:
    """

    def decor(*args, **kwargs):
        something = func(*args, **kwargs)
        func_name = f'Loging function {func.__name__}.txt'
        with open(func_name, 'a', encoding='utf-8') as file:
            time_now = [i for i in datetime.timetuple(datetime.now())]
            file.writelines(f'Time call function: {time_now[3]}:{time_now[4]}:{time_now[5]}\n')
            file.writelines(f'Name function: {func.__name__}\n')
            file.writelines(f'Arguments in call function: {[arg for arg in args]}\n')
            file.writelines(f'Return value: {something}\n')

    return decor


def logger_with_save_path(path_save):
    def logger(func):
        def decor_with_patch(*args, **kwargs):
            something = func(*args, **kwargs)
            func_name = f'Loging function {func.__name__}.txt'
            save_path = os.path.join(path_save, func_name)
            with open(save_path, 'a', encoding='utf-8') as file:
                time_now = [i for i in datetime.timetuple(datetime.now())]
                file.writelines(f'Time call function: {time_now[3]}:{time_now[4]}:{time_now[5]}\n')
                file.writelines(f'Name function: {func.__name__}\n')
                file.writelines(f'Arguments in call function: {[arg for arg in args]}\n')
                file.writelines(f'Return value: {something}\n')
                print(save_path)

        return decor_with_patch

    return logger
