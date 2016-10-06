# -*- coding: utf-8 -*-
# @Author: aaronlai
# @Date:   2016-10-06 23:42:46
# @Last Modified by:   AaronLai
# @Last Modified time: 2016-10-06 23:47:40

from unittest import TestCase
from moviepy.editor import *    # noqa
from make_movie import export_movie

import os


class Test_make_movie(TestCase):

    def test_movie(self):
        result = export_movie('./test.mp4', fps=2)

        assert result.duration > 137
        assert result.duration < 138

        os.remove('./test.mp4')
