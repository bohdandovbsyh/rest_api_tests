import pytest

from youtube import YouTube


@pytest.fixture(scope='session', autouse=False)
def session_print() -> YouTube:
    print('Session fixture run only once before all tests')


@pytest.fixture()
def create_youtube_instance() -> YouTube:
    yield YouTube('www.youtube.com', [], [], {})


@pytest.fixture()
def create_youtube_with_video(create_youtube_instance) -> tuple:
    video_name = 'My Video'
    youtube = create_youtube_instance
    youtube.upload_video(video_name)
    return youtube, video_name


@pytest.fixture()
def create_youtube_with_video_and_favourite_videos(create_youtube_with_video):
    youtube, video_name = create_youtube_with_video
    youtube.add_favourite_video(video_name)
    return youtube, video_name


@pytest.fixture()
def create_custom_youtube_instance():
    def create_youtube(url, accounts, videos, favourite_videos):
        return YouTube(url, accounts, videos, favourite_videos)

    return create_youtube


# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "smoke: smoke test"
#     )
#     config.addinivalue_line(
#         "markers", "performance: performance tests"
#     )
