import pytest
from zen_dataset.utils import *
import tempfile

def test_paths_to_files_in():
    with tempfile.TemporaryDirectory() as tmpdir:
        with tempfile.NamedTemporaryFile(dir=tmpdir):
            with tempfile.TemporaryDirectory(dir=tmpdir) as tmpdir_inner:
                with tempfile.NamedTemporaryFile(dir=tmpdir_inner):
                    assert len(paths_to_files_in(tmpdir)) == 2
