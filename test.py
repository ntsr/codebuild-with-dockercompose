#!/usr/env python
# -*- coding: utf-8 -*-

import unittest
from localstack.services import infra


class TestCase(unittest.TestCase):
    def setUp(self):
        infra.start_infra(async=True)

    def teardown(self):
        infra.stop_infra()

    def test__sample(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()