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

from glm.type_vec4 import Vec4

class TestVec4(unittest.TestCase):

    def test_initialization(self):
        # none argument init
        v = Vec4()
        msg = 'none argument initialzation failure'
        self.assertEqual(v.x, 0.0, msg)
        self.assertEqual(v.y, 0.0, msg)
        self.assertEqual(v.z, 0.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        # init with key words
        v = Vec4(x=1.)
        msg = 'key word initialzation failure'
        self.assertEqual(v.x, 1.0, msg)
        self.assertEqual(v.y, 0.0, msg)
        self.assertEqual(v.z, 0.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4(y=5., x=2.)
        self.assertEqual(v.x, 2., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4(y=3., z=2., x=5.)
        self.assertEqual(v.x, 5., msg)
        self.assertEqual(v.y, 3., msg)
        self.assertEqual(v.z, 2.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4(x=1., y=5., z=2., w=.5)
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 2.0, msg)
        self.assertEqual(v.w, .5, msg)

        # init with float argument
        v = Vec4(1.)
        self.assertEqual((v.x, v.y, v.z, v.w), (1., 1., 1., 1.), 'float argument init failure')

        # init with list or tuple
        v = Vec4([1., 5.])
        msg = 'list init failure'
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4([1., 5., -2.])
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4([1., 5., -2., .5])
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)
        self.assertEqual(v.w, 0.5, msg)

        v = Vec4((1., 5.))
        msg = 'tuple init failure'
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4((1., 5., -2.))
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)
        self.assertEqual(v.w, 0.0, msg)

        v = Vec4((1., 5., -2., .5))
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)
        self.assertEqual(v.w, 0.5, msg)

        msg = 'Vec4 init failure'
        bv = Vec4(1., 5., -2., .5)
        v = Vec4(bv)
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)
        self.assertEqual(v.w, 0.5, msg)

if __name__ == '__main__':
    unittest.main()
