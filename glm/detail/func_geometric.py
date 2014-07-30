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


from func_exponential import *


def length(x):
    """Returns the length of x, i.e., sqrt(x * x).

    :param x: Floating-point vector types.

    .. seealso::
        `GLSL length man page <http://www.opengl.org/sdk/docs/manglsl/xhtml/length.xml>`_
        `GLSL 4.20.8 specification, section 8.5 Geometric Functions <http://www.opengl.org/registry/doc/GLSLangSpec.4.20.8.pdf>`_"""
    # TODO: implement vec2 type
#     if isinstance(x, Vec2):
#         sqr = x.x * x.x + x.y * x.y
#         return math.sqrt(sqr)
    if isinstance(x, Vec3):
        sqr = x.x * x.x + x.y * x.y + x.z * x.z
        return math.sqrt(sqr)
    elif isinstance(x, Vec4):
        sqr = x.x * x.x + x.y * x.y + x.z * x.z + x.w * x.w
        return math.sqrt(sqr)
    elif isinstance(x, float) or isinstance(x, int) or isinstance(x, long):
        return abs(x)
    else:
        raise TypeError('unsupport type %s' % type(x))

def normalize(x):
    """Returns a vector in the same direction as x but with length of 1.
    .. seealso::
        `GLSL normalize man page <http://www.opengl.org/sdk/docs/manglsl/xhtml/normalize.xml>`_
        `GLSL 4.20.8 specification, section 8.5 Geometric Functions <http://www.opengl.org/registry/doc/GLSLangSpec.4.20.8.pdf>`_"""
    if isinstance(x, float) or isinstance(x, int) or isinstance(x, long):
        return -1.0 if x < 0.0 else 1.0
    #elif isinstance(x, Vec2):
        #sqr = x.x * x.x + x.y * x.y
        #return x * inversesqrt(sqr)
    elif isinstance(x, Vec3):
        sqr = x.x * x.x + x.y * x.y + x.z * x.z
        return x * inversesqrt(sqr)
    elif isinstance(x, Vec4):
        sqr = x.x * x.x + x.y * x.y + x.z * x.z + x.w * x.w
        return x * inversesqrt(sqr)
