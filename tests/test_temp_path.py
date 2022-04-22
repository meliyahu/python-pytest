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
    audio_types = ["file1.wac", "file1.wav", "file1.flac"]
    audio_file_list = []
    for audio_type in audio_types:
        p_file = d_dir / audio_type
        p_file.write_text(CONTENT)
        audio_file_list.append(p_file)

    return audio_file_list


@pytest.fixture(name="site_config_fixture")
def generate_site_config(tmp_path):
    """Generate audio config fixture"""
    config = {}
    config["audio_file_types"] = [".wac", ".wav", ".flac"]
    config['site'] = {
        "base_source": tmp_path / "data/users",
        "base_target": tmp_path / "data/audio",
        "base_spectogram": tmp_path / "data/vis",
        "base_archive": tmp_path / "data/archive",
        "base_issues": tmp_path / "data/issues",
        "site_name": "alic",
        "enabled": True,
        "process_duplicates_published": True,
        "process_duplicates_source": True,
        "sensors": [
            {"source": "TTE/Sensor_ALIC01", "target": "tte-alic01"},
            {"source": "ASM/Sensor_Alic02", "target": "asm-alic02"},
        ],
    }
    return config


class TestTempPath:
    """Test class"""

    def test_create_file(self, audio_files_fixture, site_config_fixture):
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

        print(site_config_fixture)
