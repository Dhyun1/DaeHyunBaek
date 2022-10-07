import os
import import_ipynb
import importlib
from global_function import ipynb_to_py
from global_function import reload_module

a = '44123'
a[-2:]
# 자동화 module import (benepia, walkerhill.. etc.)
moduleNm = 'benepia' # file name (.py)
bene = reload_module(moduleNm) # import A as B
gf = reload_module('global_fun') # import global_function as gf

# .ipynb > .py file export
dir = r'c:\\Users\\monan\\++python\\selenium' # ipynb 파일 경로
notebookNm = 'benepia' # ipynb 파일 이름
gf.ipynb_to_py(dir, notebookNm)

bene = reload_module(moduleNm) # import A as B
