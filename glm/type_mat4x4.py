# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014 mack stone
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from type_vec4 import Vec4

class Mat4x4(object):

    def __init__(self, *args, **kwargs):

        self.__value = ()

    def __len__(self):
        return 4

    def __getitem__(self, index):
        if (index < -4) or (index > 3):
            raise IndexError

        if index == 0 or index == -4:
            return self.__value[0]
        elif index == 1 or index == -3:
            return self.__value[1]
        elif index == 2 or index == -2:
            return self.__value[2]
        elif index == 3 or index == -1:
            return self.__value[3]

        return super(Mat4x4, self).__getItem(index)

    def __setitem__(self, index, value):
        if (index < -4) or (index > 3):
            raise IndexError

        if not isinstance(value, Vec4):
            raise TypeError('Must be a Vec4')

        if index == 0 or index == -4:
            self.__value[0] = value
        elif index == 1 or index == -3:
            self.__value[1] = value
        elif index == 2 or index == -2:
            self.__value[2] = value
        elif index == 3 or index == -1:
            self.__value[3] = value
