#!/usr/env python
# -*- coding: utf-8 -*-

import os
from datetime import datetime as dt
from pynamodb.attributes import (
    UnicodeAttribute, UTCDateTimeAttribute
)
from pynamodb.models import Model
from logzero import logger

AWS_DYNAMO_TABLE_NAME_USERS = os.getenv('AWS_DYNAMO_TABLE_NAME_USERS') or 'test-Users'
LOCAL_DEBUG = bool(os.getenv('LOCAL_DEBUG')) or False
ID_PREFIX = 'user'


class User(Model):
    class Meta:
        table_name = AWS_DYNAMO_TABLE_NAME_USERS
        write_capacity_units = 1
        read_capacity_units = 1

        if LOCAL_DEBUG:
            host = 'http://localhost:4569'

    user_id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute()
    password = UnicodeAttribute(null=True)
    created_at = UTCDateTimeAttribute()
    updated_at = UTCDateTimeAttribute()


    @classmethod
    def new_item(cls, email, password, save=True):
        now = dt.now()
        user_id = '{}::{}'.format(ID_PREFIX, email)
        user = User(
            user_id,
            None,
            email=email,
            password=password,
            created_at=now,
            updated_at=now
        )

        if save:
            try:
                user.save()
            except Exception as e:
                logger.error("save failed")
                return None

        return user

    @classmethod
    def to_string(cls):
        return {
            "user_id": cls.user_id,
            "email": cls.email,
            "password": cls.password,
            "created_at": cls.created_at,
            "updated_at": cls.updated_at
        }
