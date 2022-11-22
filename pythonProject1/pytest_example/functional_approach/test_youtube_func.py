import pytest


def test_fake_data(faker):
    print('\n')
    print(faker.name())
    print(faker.address())
    print('\n')
    print(faker.text())


@pytest.mark.performance
def test_add_video(create_youtube_instance):
    youtube = create_youtube_instance
    new_video = 'Funny Crocodiles'
    youtube.upload_video('Funny Crocodiles')
    assert youtube.videos[0] == new_video, (f'New video was not added'
                                            f'\nActual: {youtube.videos[0]}'
                                            f'\nExpected: {new_video}')


@pytest.mark.performance
@pytest.mark.smoke
def test_add_new_account(create_youtube_instance):
    youtube = create_youtube_instance
    new_account = {'user_name': 'New_User', 'password': '123'}
    youtube.create_new_account(new_account)

    assert youtube.accounts[0] == new_account, (f'New account was not added'
                                                f'\nActual: {youtube.accounts[0]}'
                                                f'\nExpected: {new_account}')


@pytest.mark.smoke
def test_remove_video(create_youtube_with_video):
    """
    Summary: Test remove video from YouTube
    Pre_conditions: Video is uploaded
    Steps: 1. Remove video from YouTube
    Expected: Video removed
    """
    youtube, video_name = create_youtube_with_video
    youtube.remove_video(video_name)
    assert video_name not in youtube.videos, f'Video {video_name} was not removed'


@pytest.mark.skip(reason='Skip because true')
def test_create_custom_youtube(create_custom_youtube_instance):
    youtube = create_custom_youtube_instance('www.youtube.com/accounts', [1, 2], [2, 3], [3, 4])
    assert youtube.url == 'www.youtube.com/accounts'
    youtube_1 = create_custom_youtube_instance('www.youtube.com/videos', [1, 2], [2, 3], [3, 4])
    assert youtube_1.url == 'www.youtube.com/videos'


@pytest.mark.parametrize("link,expected", [('www.youtube.com/accounts', True), ("youtube.com/accounts", False)],
                         ids=['with_www', 'without_www'])
def test_create_youtube_www(create_custom_youtube_instance, link, expected):
    youtube = create_custom_youtube_instance(link, [], [], [])
    actual_result = 'www' in youtube.url
    assert actual_result is expected


def test_error_on_invalid_video_name(create_youtube_instance):
    youtube = create_youtube_instance
    with pytest.raises(TypeError):
        youtube.upload_video('')
