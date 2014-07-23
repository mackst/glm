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


class Vec4(object):

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.x = kwargs.get('x', .0)
            self.y = kwargs.get('y', .0)
            self.z = kwargs.get('z', .0)
            self.w = kwargs.get('w', .0)
        elif args:
            lenArgs = len(args)
            if lenArgs == 1:
                inarg = args[0]
                if isinstance(inarg, Vec4):
                    self.x = inarg.x
                    self.y = inarg.y
                    self.z = inarg.z
                    self.w = inarg.w
                # TODO: implement vec3 and vec2
                #if isinstance(inarg, Vec3):
                elif isinstance(inarg, list) or isinstance(inarg, tuple):
                    il = []
                    if len(inarg) == 1:
                        il.append(inarg[0])
                        il += [.0, .0, .0]
                    elif len(inarg) == 2:
                        il = list(inarg) + [.0, .0]
                    elif len(inarg) == 3:
                        il = list(inarg) + [.0,]
                    elif len(inarg) == 4:
                        il = inarg
                    else:
                        il = inarg[:4]
                    self.x, self.y, self.z, self.w = il
                elif isinstance(inarg, int) or isinstance(inarg, float) or isinstance(inarg, long):
                    self.x = inarg
                    self.y = inarg
                    self.z = inarg
                    self.w = inarg
            elif lenArgs == 2:
                # TODO: implement one of the arg is vec3
                # or two vec2 as args
                self.x, self.y = args
                self.z = .0
                self.w = .0
            elif lenArgs == 3:
                # TODO: implement one of the arg is vec2
                self.x, self.y, self.z = args
                self.w = .0
            elif lenArgs == 4:
                self.x, self.y, self.z, self.w = args
            else:
                self.x, self.y, self.z, self.w = args[:4]
        else:
            self.x = .0
            self.y = .0
            self.z = .0
            self.w = .0

    def __len__(self):
        return 4

    def __getitem__(self, index):
        if index > 3 or index < -4:
            raise IndexError('out of range')

        if index == 0 or index == -4:
            return self.x
        elif index == 1 or index == -3:
            return self.y
        elif index == 2 or index == -2:
            return self.z
        elif index == 3 or index == -1:
            return self.w
        return super(Vec4, self).__getitem__(index)

    def __setitem__(self, index, value):
        if index > 3 or index < -4:
            raise IndexError('out of range')

        if index == 0 or index == -4:
            self.x = value
        elif index == 1 or index == -3:
            self.y = value
        elif index == 2 or index == -2:
            self.z = value
        elif index == 3 or index == -1:
            self.w = value

        #return super(Vec4, self).__setitem__(index, value)

    def __iadd__(self, value):
        if isinstance(value, Vec4):
            self.x += value.x
            self.y += value.y
            self.z += value.z
            self.w += value.w
        else:
            self.x += value
            self.y += value
            self.z += value
            self.w += value
        return self

    def __isub__(self, value):
        if isinstance(value, Vec4):
            self.x -= value.x
            self.y -= value.y
            self.z -= value.z
            self.w -= value.w
        else:
            self.x -= value
            self.y -= value
            self.z -= value
            self.w -= value
        return self

    def __imul__(self, value):
        if isinstance(value, Vec4):
            self.x *= value.x
            self.y *= value.y
            self.z *= value.z
            self.w *= value.w
        else:
            self.x *= value
            self.y *= value
            self.z *= value
            self.w *= value
        return self

    def __idiv__(self, value):
        if isinstance(value, Vec4):
            self.x /= value.x
            self.y /= value.y
            self.z /= value.z
            self.w /= value.w
        else:
            self.x /= value
            self.y /= value
            self.z /= value
            self.w /= value
        return self

    def __itruediv__(self, value):
        if isinstance(value, Vec4):
            self.x /= float(value.x)
            self.y /= float(value.y)
            self.z /= float(value.z)
            self.w /= float(value.w)
        else:
            self.x /= float(value)
            self.y /= float(value)
            self.z /= float(value)
            self.w /= float(value)
        return self

    def __imod__(self, value):
        if isinstance(value, Vec4):
            self.x %= value.x
            self.y %= value.y
            self.z %= value.z
            self.w %= value.w
        else:
            self.x %= value
            self.y %= value
            self.z %= value
            self.w %= value
        return self

    def __iand__(self, value):
        if isinstance(value, Vec4):
            self.x &= value.x
            self.y &= value.y
            self.z &= value.z
            self.w &= value.w
        else:
            self.x &= value
            self.y &= value
            self.z &= value
            self.w &= value
        return self

    def __ior__(self, value):
        if isinstance(value, Vec4):
            self.x |= value.x
            self.y |= value.y
            self.z |= value.z
            self.w |= value.w
        else:
            self.x |= value
            self.y |= value
            self.z |= value
            self.w |= value
        return self

    def __ixor__(self, value):
        if isinstance(value, Vec4):
            self.x ^= value.x
            self.y ^= value.y
            self.z ^= value.z
            self.w ^= value.w
        else:
            self.x ^= value
            self.y ^= value
            self.z ^= value
            self.w ^= value
        return self

    def __ilshift__(self, value):
        if isinstance(value, Vec4):
            self.x <<= value.x
            self.y <<= value.y
            self.z <<= value.z
            self.w <<= value.w
        else:
            self.x <<= value
            self.y <<= value
            self.z <<= value
            self.w <<= value
        return self

    def __irshift__(self, value):
        if isinstance(value, Vec4):
            self.x >>= value.x
            self.y >>= value.y
            self.z >>= value.z
            self.w >>= value.w
        else:
            self.x >>= value
            self.y >>= value
            self.z >>= value
            self.w >>= value
        return self

    def __add__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x + value.x, self.y + value.y,
                        self.z + value.z, self.w + value.w)
        else:
            return Vec4(self.x + value, self.y + value,
                        self.z + value, self.w + value)

    def __radd__(self, value):
        return Vec4(value + self.x, value + self.y,
                    value + self.z, value + self.w)

    def __sub__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x - value.x, self.y - value.y,
                        self.z - value.z, self.w - value.w)
        else:
            return Vec4(self.x - value, self.y - value,
                        self.z - value, self.w - value)

    def __rsub__(self, value):
        return Vec4(value - self.x, value - self.y,
                    value - self.z, value - self.w)

    def __mul__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x * value.x, self.y * value.y,
                        self.z * value.z, self.w * value.w)
        else:
            return Vec4(self.x * value, self.y * value,
                        self.z * value, self.w * value)

    def __rmul__(self, value):
        return Vec4(value * self.x, value * self.y,
                    value * self.z, value * self.w)

    def __div__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x / value.x, self.y / value.y,
                        self.z / value.z, self.w / value.w)
        else:
            return Vec4(self.x / value, self.y / value,
                        self.z / value, self.w / value)

    def __rdiv__(self, value):
        return Vec4(value / self.x, value / self.y,
                    value / self.z, value / self.w)

    def __truediv__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x / float(value.x), self.y / float(value.y),
                        self.z / float(value.z), self.w / float(value.w))
        else:
            return Vec4(self.x / float(value), self.y / float(value),
                        self.z / float(value), self.w / float(value))

    def __rtruediv__(self, value):
        v = float(value)
        return Vec4(v / self.x, v / self.y, v / self.z, v / self.w)

    def __neg__(self):
        return Vec4(-self.x, -self.y, -self.z, -self.w)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y and self.z != other.z and self.w != other.w

    def __mod__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x % value.x, self.y % value.y,
                        self.z % value.z, self.w % value.w)
        else:
            return Vec4(self.x % value, self.y % value,
                        self.z % value, self.w % value)

    def __rmod__(self, value):
        return Vec4(value % self.x, value % self.y, value % self.z, value.w % self.w)

    def __and__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x & value.x, self.y & value.y,
                        self.z & value.z, self.w & value.w)
        else:
            return Vec4(self.x & value, self.y & value,
                        self.z & value, self.w & value)

    def __rand__(self, value):
        return Vec4(value & self.x, value & self.y, value & self.z, value & self.w)

    def __or__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x | value.x, self.y | value.y,
                        self.z | value.z, self.w | value.w)
        else:
            return Vec4(self.x | value, self.y | value,
                        self.z | value, self.w | value)

    def __ror__(self, value):
        return Vec4(value | self.x, value | self.y, value | self.z, value | self.w)

    def __xor__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x ^ value.x, self.y ^ value.y,
                        self.z ^ value.z, self.w ^ value.w)
        else:
            return Vec4(self.x ^ value, self.y ^ value,
                        self.z ^ value, self.w ^ value)

    def __rxor__(self, value):
        return Vec4(value ^ self.x, value ^ self.y, value ^ self.z, value ^ self.w)

    def __lshift__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x << value.x, self.y << value.y,
                        self.z << value.z, self.w << value.w)
        else:
            return Vec4(self.x << value, self.y << value,
                        self.z << value, self.w << value)

    def __rlshift__(self, value):
        return Vec4(value << self.x, value << self.y,
                    value << self.z, value << self.w)

    def __rshift__(self, value):
        if isinstance(value, Vec4):
            return Vec4(self.x >> value.x, self.y >> value.y,
                        self.z >> value.z, self.w >> value.w)
        else:
            return Vec4(self.x >> value, self.y >> value,
                        self.z >> value, self.w >> value)

    def __rrshift__(self, value):
        return Vec4(value >> self.x, value >> self.y,
                    value >> self.z, value >> self.w)

    def __invert__(self):
        return Vec4(~self.x, ~self.y, ~self.z, ~self.w)

    @property
    def r(self):
        '''r attribute'''
        return self.x

    @r.setter
    def r(self, value):
        '''set r attribute'''
        self.x = value

    @property
    def g(self):
        '''g attribute'''
        return self.y

    @g.setter
    def g(self, value):
        '''set g attribute'''
        self.y = value

    @property
    def b(self):
        '''b attribute'''
        return self.z

    @b.setter
    def b(self, value):
        '''set b attribute'''
        self.z = value

    @property
    def a(self):
        '''a attribute'''
        return self.w

    @a.setter
    def a(self, value):
        '''set a attribute'''
        self.w = value

    s = r
    t = g
    p = b
    q = a

    def __iter__(self):
        return iter((self.x, self.y, self.z, self.w))

    def __nonzero__(self):
        return self.x == 0 and self.y == 0 and self.z == 0 and self.w == 0

    def __str__(self):
        return "Vec4(%.3f, %.3f, %.3f, %.3f)" % (self.x, self.y, self.z, self.w)

    __repr__ = __str__

    # implement swizzle,
    # etc, v.xxxx, v.arg, v.qpst
    def __getattribute__(self, name):
        # TODO: implement swizzle for vec2 and vec3
        if len(name) == 4:
            xyzw = (self.x, self.y, self.z, self.w) * 3
            return Vec4([xyzw['xyzwrgbastpq'.index(i)] for i in name])

        return super(Vec4, self).__getattribute__(name)
