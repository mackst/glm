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

from glm.detail.type_vec3 import Vec3

class TestVec3(unittest.TestCase):

    def test_initialization(self):
        # none argument init
        v = Vec3()
        msg = 'none argument initialzation failure'
        self.assertEqual(v.x, 0.0, msg)
        self.assertEqual(v.y, 0.0, msg)
        self.assertEqual(v.z, 0.0, msg)

        # init with key words
        v = Vec3(x=1.)
        msg = 'key word initialzation failure'
        self.assertEqual(v.x, 1.0, msg)
        self.assertEqual(v.y, 0.0, msg)
        self.assertEqual(v.z, 0.0, msg)

        v = Vec3(y=5., x=2.)
        self.assertEqual(v.x, 2., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)

        v = Vec3(y=3., z=2., x=5.)
        self.assertEqual(v.x, 5., msg)
        self.assertEqual(v.y, 3., msg)
        self.assertEqual(v.z, 2.0, msg)

        # init with float argument
        v = Vec3(1.)
        self.assertEqual((v.x, v.y, v.z), (1., 1., 1.), 'float argument init failure')

        # init with list or tuple
        v = Vec3([1., 5.])
        msg = 'list init failure'
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)

        v = Vec3([1., 5., -2.])
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)

        v = Vec3((1., 5.))
        msg = 'tuple init failure'
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, 0.0, msg)

        v = Vec3((1., 5., -2.))
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)

        msg = 'Vec3 init failure'
        bv = Vec3(1., 5., -2.)
        v = Vec3(bv)
        self.assertEqual(v.x, 1., msg)
        self.assertEqual(v.y, 5., msg)
        self.assertEqual(v.z, -2.0, msg)

    def test_swizzle(self):
        v = Vec3(1., 3., 2.)
        msg = 'swizzle for Vec3'

        # xyzw swizzle
        sv = v.yzx
        self.assertTrue(isinstance(sv, Vec3), msg)
        self.assertEqual(sv.x, v.y, msg)
        self.assertEqual(sv.y, v.z, msg)
        self.assertEqual(sv.z, v.x, msg)

        # rgba swizzle
        sv = v.gbr
        self.assertTrue(isinstance(sv, Vec3), msg)
        self.assertEqual(sv.r, v.y, msg)
        self.assertEqual(sv.g, v.z, msg)
        self.assertEqual(sv.b, v.x, msg)

        # stpq swizzle
        sv = v.tps
        self.assertTrue(isinstance(sv, Vec3), msg)
        self.assertEqual(sv.s, v.y, msg)
        self.assertEqual(sv.t, v.z, msg)
        self.assertEqual(sv.p, v.x, msg)

        # mix all
        sv = v.ybr
        self.assertTrue(isinstance(sv, Vec3), msg)
        self.assertEqual(sv.x, v.y, msg)
        self.assertEqual(sv.y, v.z, msg)
        self.assertEqual(sv.z, v.x, msg)

    def test_indexGetNSet(self):
        v = Vec3(1., 3., -1.)

        msg = 'index get attribute failure'
        self.assertEqual(v[0], v.x, msg)
        self.assertEqual(v[1], v.y, msg)
        self.assertEqual(v[2], v.z, msg)
        self.assertEqual(v[-1], v.z, msg)
        self.assertEqual(v[-2], v.y, msg)
        self.assertEqual(v[-3], v.x, msg)
        self.assertRaises(IndexError, lambda i: v[i], 4)
        self.assertRaises(IndexError, lambda i: v[i], -5)

        msg = 'index set attribute failure'
        v[0] = 2.
        v[1] = 1.
        v[2] = 3.
        self.assertEqual(v.x, 2., msg)
        self.assertEqual(v.y, 1., msg)
        self.assertEqual(v.z, 3., msg)

        v[-3] = -1.
        v[-2] = -3.
        v[-1] = 1.0
        self.assertEqual(v.x, -1., msg)
        self.assertEqual(v.y, -3., msg)
        self.assertEqual(v.z, 1.0, msg)

if __name__ == '__main__':
    unittest.main()
