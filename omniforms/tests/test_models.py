# -*- coding: utf-8 -*-
"""
Tests the omniforms models
"""
from __future__ import unicode_literals
from django.db import models
from django.test import TestCase
from omniforms.models import OmniFormBase


class OmniFormBaseTestCase(TestCase):
    """
    Tests the OmniFormBase class
    """
    def test_title_field(self):
        """
        The model should have a title field
        """
        field = OmniFormBase._meta.get_field('title')
        self.assertIsInstance(field, models.CharField)
        self.assertEqual(field.max_length, 255)
        self.assertFalse(field.blank)
        self.assertFalse(field.null)

    def test_string_representation(self):
        """
        The models title should be used as the string representation
        """
        instance = OmniFormBase(title='test')
        self.assertEqual('{0}'.format(instance), instance.title)

    def test_is_abstract(self):
        """
        The model should be abstract
        """
        self.assertTrue(OmniFormBase._meta.abstract)
