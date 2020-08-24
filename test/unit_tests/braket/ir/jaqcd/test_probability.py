# Copyright 2019-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import pytest
from pydantic import ValidationError

from braket.ir.jaqcd.shared_models import Probability


@pytest.mark.xfail(raises=ValidationError)
def test_missing_probability():
    Probability()


@pytest.mark.xfail(raises=ValidationError)
def test_non_float():
    Probability(probability="foo")


@pytest.mark.xfail(raises=ValidationError)
def test_nan_float():
    Probability(probability=float("nan"))


@pytest.mark.xfail(raises=ValidationError)
def test_inf_float():
    Probability(probability=float("inf"))


@pytest.mark.xfail(raises=ValidationError)
def test_negative_inf_float():
    Probability(probability=float("-inf"))


@pytest.mark.xfail(raises=ValidationError)
def test_negative_float():
    Probability(probability=float(-1.5))


@pytest.mark.xfail(raises=ValidationError)
def test_great_than_one_float():
    Probability(probability=float(2.1))


def test_float():
    probability = 0.15
    obj = Probability(probability=probability)
    assert obj.probability == probability


def test_extra_params():
    Probability(probability=0, foo="bar")