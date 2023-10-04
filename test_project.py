import pytest
from project import youtube_link, downloader_full, downloader_audio

def test_valid_youtube_link():
    valid_link = "https://www.youtube.com/watch?v=abc123"
    assert youtube_link(valid_link) == valid_link

def test_invalid_youtube_link():
    invalid_link = "https://example.com"
    assert youtube_link(invalid_link) is None

def test_downloader_full():
    valid_link = "https://www.youtube.com/watch?v=eZQyVUTcpM4&list=RDeZQyVUTcpM4"
    result = downloader_full(valid_link)
    assert result is not None


def test_downloader_audio():
    valid_link = "https://www.youtube.com/watch?v=eZQyVUTcpM4&list=RDeZQyVUTcpM4"
    result = downloader_full(valid_link)
    assert result is not None



if __name__ == "__main__":
    pytest.main()
