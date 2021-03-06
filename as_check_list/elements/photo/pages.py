# -*- coding: utf-8 -*-

from urlparse import urljoin

from as_check_list.elements.page import Page
from as_check_list.elements.photo.components import *
from as_check_list.elements.like.components import *


class AlbumPage(Page):
    def __init__(self, driver, user_path=''):
        super(AlbumPage, self).__init__(driver, urljoin(user_path, 'pphotos'))

    @property
    def photo(self):
        return AlbumPhoto(self.driver)


class PhotoUploadPage(Page):
    def __init__(self, driver):
        super(PhotoUploadPage, self).__init__(driver)
        self.photo_url = None

    def load_photo(self, path):
        PhotoUploadButton(self.driver).load_photo(path)
        UserAlbumButton(self.driver).click()
        self.photo_url = AlbumPage(self.driver).photo.url
        return self


class OwnPhotoPage(Page):
    def add_like(self, wait_for_completion=False):
        self.like_button.click_disabled(wait_for_completion)

    def remove_like(self, wait_for_completion=False):
        self.like_button.click_active(wait_for_completion)

    def delete(self):
        self.delete_button.click()
        DeletedPhotoStub(self.driver).find()

    def close(self):
        url = self.driver.current_url
        self.close_button.click()
        WebDriverWait(self.driver, Component.TIMEOUT, Component.POLL_FREQUENCY).until(
            lambda d: d.current_url != url
        )

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, CompactPhotoLikeButton.ACTIVE, CompactPhotoLikeButton.DISABLED)

    @property
    def like_button(self):
        return CompactPhotoLikeButton(self.driver)

    @property
    def delete_button(self):
        return PhotoDeleteButton(self.driver)

    @property
    def close_button(self):
        return PhotoCloseButton(self.driver)


class FeedPhotoPage(Clickable):
    def add_like(self, wait_for_completion=False):
        self.like_button.click_disabled(wait_for_completion)

    def remove_like(self, wait_for_completion=False):
        self.like_button.click_active(wait_for_completion)

    @property
    def like_counter(self):
        return PhotoLikeCounter(self.driver, NonCompactPhotoLikeButton.ACTIVE, NonCompactPhotoLikeButton.DISABLED)

    @property
    def like_button(self):
        return NonCompactPhotoLikeButton(self.driver)
