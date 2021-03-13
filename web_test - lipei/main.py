# -*- coding: utf-8 -*-
"""
    Create Time: 2019/9/1 10:55
    Author: 作者
"""
import pytest

if __name__=='__main__':
    pytest.main(['-s',
                 '-m login',
                 '-q',
                 '--alluredir',
                 './report'
                 # '--html=report/webresult.html',
                 # '--alluredir=alluredir/'
                 ])