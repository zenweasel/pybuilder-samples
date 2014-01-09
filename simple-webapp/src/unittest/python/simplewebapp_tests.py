#!/usr/bin/env python
# -*- coding: utf-8 -*-

import server
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_returns_helloworld(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()