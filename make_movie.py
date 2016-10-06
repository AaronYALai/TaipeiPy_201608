# -*- coding: utf-8 -*-
# @Author: aaronlai
# @Date:   2016-10-06 13:13:53
# @Last Modified by:   AaronLai
# @Last Modified time: 2016-10-06 23:42:03

from moviepy.editor import *    # noqa


# Screen 1 - TextClip
def screen1(Truth, d_vars, d_pos):
    texts = [" 你     的時候腦袋有曾冒出過我嗎？",
             "  自為                          "]

    # Text handle: TextClip
    var = dict(d_vars)
    var['txt'] = texts[0]
    sub_text1 = TextClip(**var).set_position((120, 600))

    var = dict(d_vars)
    var['txt'] = texts[1]
    var['fontsize'] = 75
    var['color'] = 'red'
    sub_text2 = TextClip(**var).set_position((120, 592))

    # Mix two texts
    text_1 = CompositeVideoClip([sub_text1, sub_text2], size=Truth.size)
    text_1 = text_1.set_duration(3)

    # repeatedly apply methods (ex. clip.set_pos().set_duration()...)
    var = dict(d_vars)
    var['txt'] = " 自為的時候啊..."
    text_2 = TextClip(**var).set_pos(d_pos)
    text_2 = text_2.set_duration(1).set_start(3)

    # combine(compose) clips
    screen_1 = CompositeVideoClip([Truth.subclip(0, 4.5), text_1, text_2])
    screen_1 = screen_1.fadein(1)

    return screen_1


# Screen 2 - Image and physical effects
def screen2(Truth, d_vars, d_pos):
    var = dict(d_vars)
    var['txt'] = " 有！"
    var['fontsize'] = 80
    var['color'] = 'red'
    text_3 = TextClip(**var).set_pos(("center", 590))

    # Normal
    clips = [Truth.subclip(4.5, 6), text_3.set_duration(1.5)]
    clip0 = CompositeVideoClip(clips)

    # split as 2x2 array and do mirror ( mirror_x, mirror_y )
    clips = [Truth.subclip(4.8, 5.7), text_3.set_duration(0.9)]
    clip = CompositeVideoClip(clips)
    clip1 = clips_array([[clip.fx(vfx.mirror_x), clip],
                         [clip.fx(vfx.mirror_y).fx(vfx.mirror_x),
                          clip.fx(vfx.mirror_y)]]).resize(clip.size)

    # crop then resize, brighten 1.5x
    clip2 = clip.fx(vfx.crop, x1=60, y1=30, x2=860, y2=480)
    clip2 = clip2.resize(clip.size).fx(vfx.colorx, 1.5)

    # slow to 0.4x and combine with an image
    img = ImageClip('like.png').resize(2)
    img = img.set_pos((700, 50)).set_duration(1.5).set_start(0.5)
    clip3 = CompositeVideoClip([clip.fx(vfx.speedx, 0.4), img])

    # concatenate 4 clips above
    screen_2 = concatenate_videoclips([clip0, clip1, clip2, clip3])

    return screen_2


# Screen 3 - volume and motion effects
def screen3(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 有喔"
    text_4 = TextClip(**var).set_pos(d_pos)
    text_4 = text_4.set_duration(1).set_start(2)

    var = dict(d_vars)
    var['txt'] = " 正點！"
    var['fontsize'] = 80
    var['color'] = 'yellow'
    text_5 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(3.2)
    # ##################### subtitles #####################

    # zoom in the image
    img = ImageClip('power.jpg').set_duration(1.5).set_start(0.5)
    img = img.resize(lambda t: 1 + 0.3*t).set_pos((50, 100))

    # audio volume 2x
    clips = [Truth.subclip(6, 10.2), text_4, text_5, img]
    screen_3 = CompositeVideoClip(clips).volumex(2)

    return screen_3


# Screen 4
def screen4(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 《真心話喝一杯》前男女友篇"
    var['fontsize'] = 70
    var['color'] = 'yellow'
    text_6 = TextClip(**var).set_pos(d_pos).set_duration(2)

    var = dict(d_vars)
    var['txt'] = " 八月份Taipei.Py"
    var['fontsize'] = 80
    var['color'] = 'red'
    text_7 = TextClip(**var).set_pos(("center", 10)).set_duration(2)

    var = dict(d_vars)
    var['txt'] = " 前任情侶隨機問彼此一系列問題"
    var['fontsize'] = 80
    var['color'] = 'yellow'
    text_8 = TextClip(**var).set_pos(d_pos).set_duration(2.85).set_start(2)

    var = dict(d_vars)
    var['txt'] = " 他們可以選擇回答問題或是喝一杯"
    text_9 = TextClip(**var).set_pos(d_pos).set_duration(2.5).set_start(4.85)

    var = dict(d_vars)
    var['txt'] = " 我們曾經是男女朋友"
    text_10 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(10)

    var = dict(d_vars)
    var['txt'] = " 我們是短暫的夏日愛火"
    text_11 = TextClip(**var).set_pos(d_pos).set_duration(2).set_start(11)

    var = dict(d_vars)
    var['txt'] = " 我們交往一年半"
    text_12 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(13)

    var = dict(d_vars)
    var['txt'] = " 她和我的室友約會過"
    text_13 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(15)

    var = dict(d_vars)
    var['txt'] = " 我和他的死黨約過一次會"
    text_14 = TextClip(**var).set_pos(d_pos).set_duration(2).set_start(16.5)

    var = dict(d_vars)
    var['txt'] = " 才會認識他"
    text_15 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(18.5)

    var = dict(d_vars)
    var['txt'] = " 然後九個月之後 我們開始交往"
    text_16 = TextClip(**var).set_pos(d_pos).set_duration(2.5).set_start(20)
    # ##################### subtitles #####################

    all_clips = [Truth.subclip(10.2, "00:00:32.9"), text_6, text_7, text_8,
                 text_9, text_10, text_11, text_12, text_13, text_14, text_15,
                 text_16]
    screen_4 = CompositeVideoClip(all_clips)

    return screen_4


# Screen 5
def screen5(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 你敢不敢把酒放在我身上然後喝光"
    text_17 = TextClip(**var).set_pos(d_pos).set_duration(3).set_start(0.5)

    var = dict(d_vars)
    var['txt'] = " 如果你不敢 你就要罰兩杯"
    text_18 = TextClip(**var).set_pos(d_pos).set_duration(3).set_start(3.5)

    var = dict(d_vars)
    var['txt'] = " 什麼意思啊(內心暗爽)"
    text_19 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(6.5)

    var = dict(d_vars)
    var['txt'] = " 放身上是哪招"
    text_20 = TextClip(**var).set_pos(d_pos).set_duration(1.2).set_start(7.5)

    var = dict(d_vars)
    var['txt'] = " 例如放在你的肚臍上喝嗎"
    text_21 = TextClip(**var).set_pos(d_pos).set_duration(2.8).set_start(8.7)

    var = dict(d_vars)
    var['txt'] = " 不"
    text_22 = TextClip(**var).set_pos(d_pos).set_duration(0.8).set_start(13.5)

    var = dict(d_vars)
    var['txt'] = " 她灑出來了！"
    var['fontsize'] = 70
    var['color'] = 'red'
    text_23 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(14.3)

    var = dict(d_vars)
    var['txt'] = " 我喝不了啦 (ＸＤ)"
    var['fontsize'] = 70
    var['color'] = 'yellow'
    text_24 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(19.5)

    var = dict(d_vars)
    var['txt'] = " 好 來吧 我來了！"
    text_25 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(21)

    var = dict(d_vars)
    var['txt'] = " 頭往右邊轉"
    text_26 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(23.5)

    var = dict(d_vars)
    var['txt'] = " 不是不是 那是妳的左邊"
    text_27 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(25)
    # ##################### subtitles #####################

    img2 = ImageClip('shy.png').resize(0.5).set_pos((780, 260))
    img2 = img2.set_duration(1).set_start(29.7)

    screen_5 = CompositeVideoClip([Truth.subclip("00:02:15", "00:02:47"),
                                  text_17, text_18, text_19, text_20, text_21,
                                  text_22, text_23, text_24, text_25, text_26,
                                  text_27, img2])

    return screen_5


# Screen 6
def screen6(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 喔 拜託不要..."
    text_28 = TextClip(**var).set_pos(d_pos).set_duration(1.2)

    var = dict(d_vars)
    var['txt'] = " 你自慰的時候腦袋有曾冒出過我嗎？"
    text_29 = TextClip(**var).set_pos(d_pos).set_duration(2.3).set_start(1.2)

    var = dict(d_vars)
    var['txt'] = " 拜託喝了吧"
    text_30 = TextClip(**var).set_pos(d_pos).set_duration(1.2).set_start(3.5)

    var = dict(d_vars)
    var['txt'] = " 爸拖喝吧 OTZ"
    text_31 = TextClip(**var).set_pos(d_pos).set_duration(1.2).set_start(5.7)

    var = dict(d_vars)
    var['txt'] = " 不管答案是什麼我都不想知道"
    text_32 = TextClip(**var).set_pos(d_pos).set_duration(1.8).set_start(7.2)

    var = dict(d_vars)
    var['txt'] = " 謝謝你"
    text_33 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(10.3)

    var = dict(d_vars)
    var['txt'] = " 有啊！        "
    var['fontsize'] = 70
    var['color'] = 'yellow'
    text_34 = TextClip(**var).set_pos(("center", 595))
    text_34 = text_34.set_duration(0.6).set_start(12.4)

    var = dict(d_vars)
    var['txt'] = "        真的嗎？"
    var['fontsize'] = 90
    var['color'] = 'red'
    text_35 = TextClip(**var).set_pos(("center", 580))
    text_35 = text_35.set_duration(1.3).set_start(12.7)

    var = dict(d_vars)
    var['txt'] = "            有嗎？"
    text_36 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(14)

    var = dict(d_vars)
    var['txt'] = " 有時候會啊              "
    text_37 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(14.5)

    var = dict(d_vars)
    var['txt'] = " 妳知道妳可以打給我的 (A__A)"
    var['fontsize'] = 70
    var['color'] = 'yellow'
    text_38 = TextClip(**var).set_pos(("center", 595))
    text_38 = text_38.set_duration(1.5).set_start(16.2)

    var = dict(d_vars)
    var['txt'] = " 當妳想到的時候"
    text_39 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(18)

    var = dict(d_vars)
    var['txt'] = " 才不要！"
    text_40 = TextClip(**var).set_pos(("center", 595))
    text_40 = text_40.set_duration(1).set_start(19.5)

    var = dict(d_vars)
    var['txt'] = " 這是... 這是我『獨處』的時間！"
    text_41 = TextClip(**var).set_pos(("center", 595))
    text_41 = text_41.set_duration(2).set_start(20.5)
    # ##################### subtitles #####################

    img3 = ImageClip('shy.png').resize(0.7).set_pos((720, 120))
    img3 = img3.set_duration(1.8).set_start(21)

    all_clips = [Truth.subclip("00:03:41.7", "00:04:04.7"), text_28, text_29,
                 text_30, text_31, text_32, text_33, text_34, text_35,
                 text_36, text_37, text_38, text_39, text_40, text_41, img3]
    screen_6 = CompositeVideoClip(all_clips)

    return screen_6


# Screen 7 - 1
def screen7_1(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 妳敢不敢..."
    text_42 = TextClip(**var).set_pos(d_pos).set_duration(1.8).set_start(0.4)

    var = dict(d_vars)
    var['txt'] = " 跟我接吻"
    text_43 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(3.3)

    var = dict(d_vars)
    var['txt'] = " 什麼？！"
    var['fontsize'] = 70
    var['color'] = 'yellow'
    text_44 = TextClip(**var).set_pos(("center", 595))
    text_44 = text_44.set_duration(0.8).set_start(9)
    # ##################### subtitles #####################

    screen_7_1 = CompositeVideoClip([Truth.subclip("00:04:55.7", "00:05:05.7"),
                                    text_42, text_43, text_44])

    return screen_7_1


# Screen 7 - 2
def screen7_2(Truth, d_vars, d_pos):
    # ##################### subtitles #####################
    var = dict(d_vars)
    var['txt'] = " 我寧願親你的嘴也不要喝那杯純的威士忌"
    text_45 = TextClip(**var).set_pos(("center", 580))
    text_45 = text_45.set_duration(3.1).set_start(0.2)

    var = dict(d_vars)
    var['txt'] = " 好 那就來吧！"
    text_46 = TextClip(**var).set_pos(d_pos).set_duration(0.8).set_start(3.6)

    var = dict(d_vars)
    var['txt'] = " 好 來吧"
    text_47 = TextClip(**var).set_pos(d_pos).set_duration(0.8).set_start(4.4)

    var = dict(d_vars)
    var['txt'] = " 來啊"
    text_48 = TextClip(**var).set_pos(d_pos).set_duration(0.6).set_start(5.6)

    var = dict(d_vars)
    var['txt'] = " 1 2 3 來！"
    var['fontsize'] = 80
    var['color'] = 'red'
    text_49 = TextClip(**var).set_pos(("center", 590))
    text_49 = text_49.set_duration(1).set_start(6.2)

    var = dict(d_vars)
    var['txt'] = " 喝酒囉！"
    text_50 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(17)

    var = dict(d_vars)
    var['txt'] = " 我們應該給你們拍拍手"
    text_51 = TextClip(**var).set_pos(("center", 510))
    text_51 = text_51.set_duration(2.3).set_start(18)

    var = dict(d_vars)
    var['txt'] = " 好朋友啦"
    text_52 = TextClip(**var).set_pos(d_pos).set_duration(1).set_start(22)

    var = dict(d_vars)
    var['txt'] = " 敬友誼！"
    text_53 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(23.5)

    var = dict(d_vars)
    var['txt'] = " 還有親親"
    text_54 = TextClip(**var).set_pos(d_pos).set_duration(1.5).set_start(25.5)
    # ##################### subtitles #####################

    all_clips = [Truth.subclip("00:05:24.3", "00:05:53"), text_45, text_46,
                 text_47, text_48, text_49, text_50, text_51, text_52,
                 text_53, text_54]
    screen_7_2 = CompositeVideoClip(all_clips)

    # concatenate ending
    sub_clip = Truth.subclip("00:05:50.3", "00:05:53")
    sub_clip2 = sub_clip.fx(vfx.time_mirror)

    # speedup, time_mirror, brighten and fade_out
    clip1 = concatenate_videoclips([sub_clip2.speedx(1.2),
                                    sub_clip.speedx(1.5).fx(vfx.colorx, 1.2)])
    clip2 = concatenate_videoclips([sub_clip2.speedx(1.8).fx(vfx.colorx, 1.3),
                                   sub_clip.speedx(2).fx(vfx.colorx, 1.5)])

    ending = concatenate_videoclips([clip1, clip2]).fadeout(1)
    screen_7_2 = concatenate_videoclips([screen_7_2, ending])

    return screen_7_2


def export_movie(filename, fps):
    # load video
    Truth = VideoFileClip('truth.mp4')

    # use font WeibeiTCB to support Chinese
    d_vars = {
        'font': 'WeibeiTCB',
        'stroke_color': '#000000',
        'stroke_width': 1,
        'color': 'cyan',
        'fontsize': 60
    }
    d_pos = ("center", 600)

    screen_1 = screen1(Truth, d_vars, d_pos)
    screen_2 = screen2(Truth, d_vars, d_pos)
    screen_3 = screen3(Truth, d_vars, d_pos)
    screen_4 = screen4(Truth, d_vars, d_pos)
    screen_5 = screen5(Truth, d_vars, d_pos)
    screen_6 = screen6(Truth, d_vars, d_pos)
    screen_7_1 = screen7_1(Truth, d_vars, d_pos)
    screen_7_2 = screen7_2(Truth, d_vars, d_pos)

    # Export final movie
    final_movie = concatenate_videoclips([screen_1, screen_2, screen_3,
                                         screen_4, screen_5, screen_6,
                                         screen_7_1, screen_7_2])

    final_movie.write_videofile(filename, fps=fps)

    return final_movie


def main():
    result = export_movie("taipeipy_demo.mp4", 12)
    print(result.duration)


if __name__ == '__main__':
    main()
