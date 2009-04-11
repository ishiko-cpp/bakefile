#
#  This file is part of Bakefile (http://www.bakefile.org)
#
#  Copyright (C) 2008-2009 Vaclav Slavik
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
#  IN THE SOFTWARE.
#

import antlr3
import ast
from BakefileLexer import BakefileLexer
from BakefileParser import BakefileParser
from BakefileTokenSource import BakefileTokenSource

def parse(code):
    """
    Reads Bakefile code from string argument passed in and returns parsed AST.
    """
    cStream = antlr3.StringStream(code)
    lexer = BakefileLexer(cStream)
    tStream = antlr3.CommonTokenStream(BakefileTokenSource(lexer))
    parser = BakefileParser(tStream)
    parser.adaptor = ast._TreeAdaptor()
    # FIXME: error handling
    return parser.program().tree


def parse_file(filename):
    """
    Reads Bakefile code from given file returns parsed AST.
    """
    f = file(filename, 'rt')
    try:
        return parse(f.read())
    finally:
        f.close()
