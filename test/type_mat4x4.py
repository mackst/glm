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

import unittest

from glm.type_mat4x4 import Mat4x4
from glm.type_vec4 import Vec4

class TestMat4x4(unittest.TestCase):

    def test_initialization(self):
        # none argument init
        m = Mat4x4()
        msg = 'none argument initialization failure'
        self.assertEqual(m[0], Vec4(x=1.), msg)
        self.assertEqual(m[1], Vec4(y=1.), msg)
        self.assertEqual(m[2], Vec4(z=1.), msg)
        self.assertEqual(m[3], Vec4(w=1.), msg)

        # init with key words
        m = Mat4x4(x0=2., x1=1.5, x2=3., x3=3.5,
                   y0=1., y1=2., y2=2.5, y3=3.,
                   z0=.5, z1=.5, z2=1., z3=3.5,
                   w0=3., w1=2., w2=.5, w3=1.)
        msg = 'key word initialization failure'
        self.assertEqual(m[0], Vec4(2., 1., .5, 3.), msg)
        self.assertEqual(m[1], Vec4(1.5, 2., .5, 2.), msg)
        self.assertEqual(m[2], Vec4(3., 2.5, 1., .5), msg)
        self.assertEqual(m[3], Vec4(3.5, 3., 3.5, 1.), msg)

        m = Mat4x4(x0=2., x1=1.5, x2=3., x3=3.5,
                   y0=1., y1=2., y2=2.5, y3=3.,
                   z0=.5, z1=.5, z2=1., z3=3.5,)
        self.assertEqual(m[0], Vec4(2., 1., .5), msg)
        self.assertEqual(m[1], Vec4(1.5, 2., .5), msg)
        self.assertEqual(m[2], Vec4(3., 2.5, 1.), msg)
        self.assertEqual(m[3], Vec4(3.5, 3., 3.5), msg)

        ml = [2., 1.5, 3., 3.5, 1., 2., 2.5, 3., .5, .5, 1.,
              3.5, 3., 2., .5, 1.]
        m = Mat4x4(ml)
        msg = 'list initialization failure'
        self.assertEqual(m[0], Vec4(2., 1., .5, 3.), msg)
        self.assertEqual(m[1], Vec4(1.5, 2., .5, 2.), msg)
        self.assertEqual(m[2], Vec4(3., 2.5, 1., .5), msg)
        self.assertEqual(m[3], Vec4(3.5, 3., 3.5, 1.), msg)

        v0 = Vec4(2., 1., .5, 3.)
        v1 = Vec4(1.5, 2., .5, 2.)
        v2 = Vec4(3., 2.5, 1., .5)
        v3 = Vec4(3.5, 3., 3.5, 1.)
        m = Mat4x4(v0, v1, v2, v3)
        msg = '4 vec4 initialization failure'
        self.assertEqual(m[0], Vec4(2., 1., .5, 3.), msg)
        self.assertEqual(m[1], Vec4(1.5, 2., .5, 2.), msg)
        self.assertEqual(m[2], Vec4(3., 2.5, 1., .5), msg)
        self.assertEqual(m[3], Vec4(3.5, 3., 3.5, 1.), msg)


if __name__ == '__main__':
    unittest.main()
