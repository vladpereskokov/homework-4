# -*- coding: utf-8 -*-

from like_tests.tests.base import BasePhotoTest
from like_tests.elements.likes.pages import *


class LikePhotoTest(BasePhotoTest):

    def test_like_page_photo(self):
        self.photo_page.open()
        assert(self.photo_page.has_empty_likes())
        self.photo_page.add_like_to_zero()
        assert(self.photo_page.non_zero_likes() == 1)
        self.photo_page.remove_like()
        assert(self.photo_page.has_empty_likes())