#!/usr/bin/env python3

import skilstak.colors as c


def hello(message):
  """Print Hello World"""   
  print(c.clear + (message))

def multi(message):
    """Prints hello world in multicolored letters"""
    while True:
        print(c.clear + c.multi(message))

def random(message):
    """Prints hello world in pretty colors"""
    while True:
        print(c.clear + c.rc() + (message))

