import doctest
import unittest

import discogs_finder

suite = unittest.TestSuite()
suite.addTest(doctest.DocTestSuite(discogs_finder.finder))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)