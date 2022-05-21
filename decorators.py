from datetime import datetime


def logger(func):
    """
    Для использования данного декоратора необходимо импортировать модуль datetime
    :param func:
    :return:
    """
    def decor(*args, **kwargs):
        something = func(*args, **kwargs)
        with open(f'Loging function {func.__name__}.txt', 'a', encoding='utf-8') as file:
            time_now = [i for i in datetime.timetuple(datetime.now())]
            file.writelines(f'Time call function: {time_now[3]}:{time_now[4]}:{time_now[5]}\n')
            file.writelines(f'Name function: {func.__name__}\n')
            file.writelines(f'Arguments in call function: {[arg for arg in args]}\n')
            file.writelines(f'Return value: {something}')
        return something
    return decor
