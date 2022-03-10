class Spawning():

    def __init__(self, x_cood, y_cood, spawn_number):
        self._num = spawn_number
        self._x = x_cood
        self._y = y_cood
        self._xdim = 15
        self._ydim = 5
        self._display = True

    def get_object(self):
        return self._num

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def get_xdim(self):
        return self._xdim

    def get_ydim(self):
        return self._ydim

    def get_display(self):
        return self._display
