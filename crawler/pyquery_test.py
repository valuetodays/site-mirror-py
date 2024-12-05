# !/usr/bin/env python3
# encoding: utf-8
from pyquery import PyQuery


def test_a():
    d = PyQuery('<div><span class="red">toto</span> rocks <span class="aaa">useless text</span></div>')
    print('')
    print(d('span'))
    print(d('span').outer_html())
    d('span.aaa').remove()
    print(d)
