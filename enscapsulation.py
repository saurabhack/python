class base:
   def  __init__(self):
      self._a=2


class vista(base):
   def __init__(self):
      base.__init__(self)

      print("calling potected member of the base class=\n",self._a)

      self._a=3

      print("calling the modified variable=\n",self._a)



obj=vista()

obj.__init__()