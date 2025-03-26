import pytest
import os
from filter_txt_lines import filter_lines

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = "Hello world\nPython is great\nHello pytest\nTest automation\n"
    file_path.write_text(content, encoding="utf-8")
    return file_path

