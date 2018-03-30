#!/usr/env python
# -*- coding: utf-8 -*-

import unittest
from localstack.services import infra
from logzero import logger
from users import User



class TestCase(unittest.TestCase):
    def setUp(self):
        infra.start_infra(async=True)
        User.create_table(wait=True)

    def teardown(self):
        infra.stop_infra()
        User.delete_table()

    def test__sample(self):
        user = User.new_item(email='sample@sample.com', password='sample')
        logger.info(user.to_string())
        user2 = User.get(user.user_id)
        logger.info(user2.to_string())

        self.assertEqual(user.email, user2.email)


if __name__ == '__main__':
    unittest.main()