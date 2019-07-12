#!/usr/bin/env python3

"""Tests for the package."""

# pylint: disable=line-too-long

import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..")))
import libhockey


class LibraryTests(unittest.TestCase):
    """Basic tests."""

    def test_construction(self):
        """Test construction."""
        client = libhockey.HockeyClient(access_token="")
        self.assertIsNotNone(client)
