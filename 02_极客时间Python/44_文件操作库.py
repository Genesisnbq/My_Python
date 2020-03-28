from pathlib import Path
import os
print(os.path.abspath("../"))  # 当前所在的绝对路径
print(os.path.exists('/ Python_code'))
print(os.path.isfile('/Eternal'))
print(os.path.isdir('/Eternal'))
os.path.join('/Eternal/','a.txt')

p = Path('.')
print(p.resolve())  # 取得当前的完整路径

p.is_dir()

q= Path('/test1/')

Path.mkdir (q,parents=True)
