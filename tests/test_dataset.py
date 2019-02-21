import pytest
from zen_dataset import Dataset
from unittest.mock import Mock, MagicMock, call

@pytest.fixture
def reader():
    return Mock(return_value='some data')

@pytest.fixture
def labeler():
    return Mock(return_value='a target')

def test_is_imported():
    Dataset

def test_returns_len_of_items_in_dataset(reader, labeler):
    items = MagicMock()
    items.__len__.return_value = 10
    dataset = Dataset(items, reader, labeler)
    assert len(dataset) == 10

def test_passes_item_to_reader_to_get_data(reader, labeler):
    dataset = Dataset([1,2,3], reader, labeler)
    assert dataset[1][0] == 'some data'
    assert reader.call_args == call(2)

def test_passes_item_to_labeler_to_get_target(reader, labeler):
    dataset = Dataset([1,2,3], reader, labeler)
    assert dataset[1][1] == 'a target'
    assert reader.call_args == call(2)
