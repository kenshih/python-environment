from . import hello_world

# https://setuptools.pypa.io/en/latest/userguide/entry_point.html
if __name__ == '__main__':
  hello_world()
  print("but called from __main__")