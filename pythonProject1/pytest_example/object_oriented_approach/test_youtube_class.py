from youtube import YouTube


class TestYoutube:

    def setup_class(self):
        pass

    def setup(self):
        print('Before test')
        self.youtube = YouTube(url='www.youtube.com')

    def test_add_new_account_to_app(self):
        new_account = {'user_name': 'New_User', 'password': '123'}
        self.youtube.create_new_account(new_account)

        assert self.youtube.accounts[0] == new_account, (f'New account was not added'
                                                         f'\nActual: {self.youtube.accounts[0]}'
                                                         f'\nExpected: {new_account}')

    def test_add_new_video_to_app(self):
        new_video = 'Funny Crocodiles'
        self.youtube.upload_video(new_video)

        assert self.youtube.videos[0] == new_video, (f'New video was not added'
                                                     f'\nActual: {self.youtube.videos[0]}'
                                                     f'\nExpected: {new_video}')

    def teardown(self):
        self.youtube = YouTube(url='www.youtube.com', accounts=[], videos=[], favourite_videos={})

    def teardown_class(self):
        print('Tear down class ++++++++++++++++++++++++')
