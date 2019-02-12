import pytest
from zen_dataset.utils import *
import tempfile

class TestPathsToFilesIn:
    def test_recursively_collects_file_paths_in_nested_directories(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with tempfile.NamedTemporaryFile(dir=tmpdir):
                with tempfile.TemporaryDirectory(dir=tmpdir) as tmpdir_inner:
                    with tempfile.NamedTemporaryFile(dir=tmpdir_inner):
                        assert len(paths_to_files_in(tmpdir)) == 2
