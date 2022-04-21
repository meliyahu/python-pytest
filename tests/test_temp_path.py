"""Temp path"""
from pathlib import Path

import pytest

# content of test_tmp_path.py
CONTENT = "content"


@pytest.fixture(name="audio_files_fixture")
def create_audio_files(tmp_path):
    """create list of files"""
    d_dir = tmp_path / "sub"
    d_dir.mkdir()
    audio_types = ['file1.wac', 'file1.wav', 'file1.flac']
    audio_file_list = []
    for audio_type in audio_types:
        p_file = d_dir / audio_type
        p_file.write_text(CONTENT)
        audio_file_list.append(p_file)

    return audio_file_list



class TestTempPath:
    """Test class"""
    def test_create_file(self, audio_files_fixture):
        """Create a file"""

        # d_dir = tmp_path / "sub"
        # d_dir.mkdir()
        # print(f'd_dir={d_dir}')
        # p_file = d_dir / "hello.txt"
        # print(f'p_file={p_file}')
        # p_file.write_text(CONTENT)
        # assert p_file.read_text() == CONTENT
        # assert len(list(tmp_path.iterdir())) == 1
        # assert 0
        for file in audio_files_fixture:
            assert Path(file).is_file()
        # print (create_audio_files)
