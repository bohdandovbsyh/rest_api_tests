class YouTube:
    def __init__(self, url: str, accounts: list = None, videos: list = None, favourite_videos: list = None):
        self.__url = url
        self.__accounts = accounts
        self.__videos = videos
        self.__favourite_videos = favourite_videos

    def create_new_account(self, new_account: dict):
        self.__accounts.append(new_account)

    @property
    def accounts(self):
        return self.__accounts

    def upload_video(self, video_name):
        if video_name == '':
            raise TypeError('Wrong_name')
        self.__videos.append(video_name)

    def remove_video(self, video_name):
        self.__videos.remove(video_name)

    @property
    def videos(self):
        return self.__videos

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    def add_favourite_video(self, video_name):
        self.__favourite_videos.append(video_name)

    @property
    def favourite_video(self):
        return self.__favourite_videos
