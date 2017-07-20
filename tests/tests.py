#!/usr/bin/env python3
import sys
from pathlib import Path
import unittest
import itertools, re

sys.path.insert(0, str(Path(__file__).parent.parent))

from collections import OrderedDict

dict = OrderedDict

import more_lists
from more_lists import *


class Tests(unittest.TestCase):
	def testSilentList(self):
		a = SilentList()
		a[3] = 1
		a[5] = "a"
		self.assertEqual(tuple(a), (None, None, None, 1, None, "a"))

	def testCustomBaseList(self):
		class Base2List(CustomBaseList):
			base = 2

		l = Base2List(
			[
				"a",
				"b",
			]
		)
		self.assertEqual(l[3], "b")


if __name__ == "__main__":
	unittest.main()
