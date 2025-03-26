import pytest
import os
from filter_txt_lines import filter_lines

@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = "Hello world\nPython is great\nHello pytest\nTest automation\n"
    file_path.write_text(content, encoding="utf-8")
    return file_path

@pytest.mark.parametrize("keyword, expected_lines", [
    ("Hello", ["Hello world\n", "Hello pytest\n"]),
    ("Python", ["Python is great\n"]),
    ("Test", ["Test automation\n"]),
    ("Nonexistent", [])
])
def test_filter_lines(sample_file, keyword, expected_lines, tmp_path):
    output_file = tmp_path / "filtered_output.txt"
    filter_lines(sample_file, keyword, output_file)
    
    with open(output_file, "r", encoding="utf-8") as f:
        result_lines = f.readlines()
    
    assert result_lines == expected_lines

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        filter_lines("non_existent_file.txt", "Hello")