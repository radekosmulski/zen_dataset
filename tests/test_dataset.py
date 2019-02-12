import pytest
from zen_dataset import Dataset
from unittest.mock import Mock, MagicMock

@pytest.fixture
def reader():
    reader_instance = Mock(return_value='some data')
    return Mock(return_value=reader_instance)

@pytest.fixture
def labeler():
    reader_instance = Mock(return_value='a target')
    return Mock(return_value=reader_instance)

def test_is_imported():
    Dataset

def test_returns_len_of_items_in_dataset(reader, labeler):
    items = MagicMock()
    items.__len__.return_value = 10
    dataset = Dataset(items, reader, labeler)
    assert len(dataset ) == 10
    items.__len__.assert_called()

def test_passes_item_to_reader_to_get_data(reader, labeler):
    dataset = Dataset([1,2,3], reader, labeler)
    assert dataset[1][0] == 'some data'

def test_passes_item_to_labeler_to_get_target(reader, labeler):
    dataset = Dataset([1,2,3], reader, labeler)
    assert dataset[1][1] == 'a target'
