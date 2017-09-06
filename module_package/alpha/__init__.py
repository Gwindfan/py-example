# -*- coding: utf-8 -*-
import sys
"""
添加上级目录至 sys.path，以便包 alpha 下模块能访问到 包 bravo 下模块
"""
sys.path.append('../')