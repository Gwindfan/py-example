# -*- coding: utf-8 -*-
import sys
import pprint

"""
在 import 模块的时候，python是通过系统路径找到这些模块的，即 sys.path
"""
pprint.pprint(sys.path)

"""
那么，我们放进这些路径里的模块或包，就可以不需指定路径，直接使用import导入了
特别的，/usr/local/lib/python2.7/site-packages(路径依据安装时指定差异会有不同)，我们常用的应该放在这里

将一个路径加入到python系统路径下，避免每次通过代码指定路径
1. 利用系统环境变量 export PYTHONPATH=$PYTHONPATH:your_module_path
2. 直接将这个路径链接到类似 /usr/local/lib/python2.7/site-packages 目录下
"""

"""
if __name__ == '__main__'，保证 package 既可以 import 又可以独立运行，用于调试
console 调试通过 python -m xxx.py
"""
if __name__ == '__main__':
    pass

"""
为了组织好模块，将多个模块分为一个包
包的组成：module 文件 + __init__.py + 目录。 例如：

alpha
├── __init__.py
├── amy.py
└── bruce.py
bravo
├── __init__.py
├── cici.py
└── david.py
"""

"""
引用 alpha 包下 amy 模块
注意 namespace
"""
from alpha import amy
pprint.pprint(amy.sayhi)
"""
或者
"""
import alpha.bruce as bruce
pprint.pprint(bruce.sayhi)


"""
如果 alpha 中的 amy 需要引用 bravo，那么默认情况下，python 是找不到包 bravo。需作操作
1. 包 alpha 中的 __init__.py 添加 sys.path.append('../')，
2. 该包下得所有 module 都添加* import __init__
"""