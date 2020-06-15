# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test_haversine():
    assert haversine(48.865070, 2.380009,50.864080, 4.390007) == 314.93472143074104
