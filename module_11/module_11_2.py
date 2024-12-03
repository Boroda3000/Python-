import inspect
from pprint import pprint


def introspection_info(obj):
    obj_dir = {}
    for i in dir(obj):
        j = getattr(obj, i)
        obj_dir[i] = repr(j)

    attributes = {}
    methods = {}
    type_ = None

    for key, val in obj_dir.items():
        if 'method' in val:
            methods[key] = val
        elif 'class' in key:
            type_ = val
        else:
            attributes[key] = val
    
    module = inspect.getmodule(obj)
    info = {'Тип объекта': type_, 'Атрибуты объекта': attributes, 'Методы объекта': methods, 'Модуль, к которому объект принадлежит': module}
    return info

pprint(introspection_info(42))