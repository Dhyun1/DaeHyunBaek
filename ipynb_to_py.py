import os
import subprocess
## ipynb를 py로 저장
def ipynb_to_py(dir, notebookNm):
    if os.path.isfile(os.path.join(dir, f'{notebookNm}.py')): # 기존 파일 삭제 =
        os.remove(os.path.join(dir, f'{notebookNm}.py'))
    os.chdir(dir) # change directory
    # subprocess module to run multiple commands in same shell
    subprocess.run(f'jupyter nbconvert --to script {notebookNm}.ipynb', shell=True) # True for window commands
    return