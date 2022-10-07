import importlib
import import_ipynb

def reload_module(importNm): # importNm은 *.py (=모듈 이름)
    mod = importlib.import_module(importNm)
    importlib.reload(mod)
    try:
        module = importlib.import_module(importNm)
    except Exception as e:
        raise Exception(e)
    return module

    
# def reload_module(importNm, fromNm=None):
#     mod = importlib.import_module(importNm)
#     importlib.reload(mod)
#     if fromNm is not None:
#         fullModuleNm = f'{fromNm}.{importNm}'
#     else:
#         fullModuleNm = importNm
#     try:
#         # from fromNm
#         module = importlib.import_module(fullModuleNm)
#     except Exception as e:
#         raise Exception(e)
    
#     return module