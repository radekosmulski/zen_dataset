import pytest
from zen_dataset import Dataset
from unittest.mock import MagicMock

def test_is_imported():
    Dataset

def test_delegates_len_to_items():
    items = MagicMock()
    items.__len__.return_value = 10
    zen = Dataset(items)
    assert len(zen) == 10
    items.__len__.assert_called()
