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
        v0 = Vec4(x=1.0)
        v1 = Vec4(y=1.0)
        v2 = Vec4(z=1.0)
        v3 = Vec4(w=1.0)
        if kwargs:
            v0.x = kwargs.get('x0', 0.0)
            v0.y = kwargs.get('y0', 0.0)
            v0.z = kwargs.get('z0', 0.0)
            v0.w = kwargs.get('w0', 0.0)
            v1.x = kwargs.get('x1', 0.0)
            v1.y = kwargs.get('y1', 0.0)
            v1.z = kwargs.get('z1', 0.0)
            v1.w = kwargs.get('w1', 0.0)
            v2.x = kwargs.get('x2', 0.0)
            v2.y = kwargs.get('y2', 0.0)
            v2.z = kwargs.get('z2', 0.0)
            v2.w = kwargs.get('w2', 0.0)
            v3.x = kwargs.get('x3', 0.0)
            v3.y = kwargs.get('y3', 0.0)
            v3.z = kwargs.get('z3', 0.0)
            v3.w = kwargs.get('w3', 0.0)
        elif args:
            lenArgs = len(args)
            if lenArgs == 1:
                m = args[0]
                if isinstance(m, Mat4x4):
                    v0 = m[0]
                    v1 = m[1]
                    v2 = m[2]
                    v3 = m[3]
                elif isinstance(m, list) or isinstance(m, tuple):
                    if len(m) != 16:
                        raise TypeError('list or tuple must have 16 items')
                    v0.x = m[0]
                    v1.x = m[1]
                    v2.x = m[2]
                    v3.x = m[3]
                    v0.y = m[4]
                    v1.y = m[5]
                    v2.y = m[6]
                    v3.y = m[7]
                    v0.z = m[8]
                    v1.z = m[9]
                    v2.z = m[10]
                    v3.z = m[11]
                    v0.w = m[12]
                    v1.w = m[13]
                    v2.w = m[14]
                    v3.w = m[15]
                elif isinstance(m, float) or isinstance(m, int) or isinstance(m, long):
                    v0 = Vec4(x=m)
                    v1 = Vec4(y=m)
                    v2 = Vec4(z=m)
                    v3 = Vec4(w=m)
            elif lenArgs == 4:
                if isinstance(args[0], Vec4):
                    v0 = args[0]
                elif isinstance(args[0], list) or isinstance(args[0], tuple):
                    v0 = Vec4(args[0])

                if isinstance(args[1], Vec4):
                    v1 = args[1]
                elif isinstance(args[1], list) or isinstance(args[1], tuple):
                    v1 = Vec4(args[1])

                if isinstance(args[2], Vec4):
                    v2 = args[2]
                elif isinstance(args[2], list) or isinstance(args[2], tuple):
                    v2 = Vec4(args[2])

                if isinstance(args[3], Vec4):
                    v3 = args[3]
                elif isinstance(args[3], list) or isinstance(args[3], tuple):
                    v3 = Vec4(args[3])

        self.__value = (v0, v1, v2, v3)

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
