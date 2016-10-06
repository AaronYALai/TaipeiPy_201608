# -*- coding: utf-8 -*-
# @Author: aaronlai
# @Date:   2016-10-06 13:13:53
# @Last Modified by:   AaronLai
# @Last Modified time: 2016-10-06 18:53:34

from moviepy.editor import *
# load video
Truth = VideoFileClip('truth.mp4')

# use font WeibeiTCB to support Chinese
font = "WeibeiTCB"


# Screen 1 - TextClip
texts = [" 你     的時候腦袋有曾冒出過我嗎？",
         "  自為                          "]

# Text handle: TextClip
sub_text1 = TextClip(texts[0], fontsize=60, color='cyan',
                     stroke_color="#000000", stroke_width=1,
                     font=font).set_position((120, 600))

sub_text2 = TextClip(texts[1], fontsize=75, color='red',
                     font=font).set_position((120, 592))

# Mix two texts
text_1 = CompositeVideoClip([sub_text1, sub_text2],
                            size=Truth.size).set_duration(3)

# repeatedly apply methods (ex. clip.set_pos().set_duration()...)
text_2 = TextClip(" 自為的時候啊...", fontsize=60, color='cyan', stroke_color="#000000",
                  stroke_width=1, font=font).set_pos(("center", 600)).set_duration(1).set_start(3)

# combine(compose) clips
screen_1 = CompositeVideoClip([Truth.subclip(0, 4.5), text_1, text_2]).fadein(1)





# Screen 2 - Image and physical effects
text_3 = TextClip(" 有！", fontsize=80, color='red', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 590))

# Normal
clip0 = CompositeVideoClip([Truth.subclip(4.5, 6), text_3.set_duration(1.5)])

# split as 2x2 array and do mirror ( mirror_x, mirror_y )
clip = CompositeVideoClip([Truth.subclip(4.8, 5.7), text_3.set_duration(0.9)])
clip1 = clips_array([[clip.fx(vfx.mirror_x), clip],
                     [clip.fx(vfx.mirror_y).fx(vfx.mirror_x), clip.fx(vfx.mirror_y)]]).resize(clip.size)

# crop then resize, brighten 1.5x
clip2 = clip.fx(vfx.crop, x1=60, y1=30, x2=860, y2=480).resize(clip.size).fx(vfx.colorx, 1.5)

# slow to 0.4x and combine with an image
img = ImageClip('like.png').resize(2)
clip3 = CompositeVideoClip([clip.fx(vfx.speedx, 0.4), img.set_pos((700, 50)).set_duration(1.5).set_start(0.5)])

# concatenate 4 clips above
screen_2 = concatenate_videoclips([clip0, clip1, clip2, clip3])


# Screen 3 - volume and motion effects
# ##################### subtitles #####################
text_4 = TextClip(" 有喔", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(2)

text_5 = TextClip(" 正點！", fontsize=80, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(3.2)
# ##################### subtitles #####################

# zoom in the image
img = ImageClip('power.jpg').set_duration(1.5).set_start(0.5).resize(lambda t: 1 + 0.3*t).set_pos((50, 100))

# audio volume 2x
screen_3 = CompositeVideoClip([Truth.subclip(6, 10.2), text_4, text_5, img]).volumex(2)



# Screen 4

# ##################### subtitles #####################
text_6 = TextClip(" 《真心話喝一杯》前男女友篇", fontsize=70, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2)

text_7 = TextClip(" 八月份Taipei.Py", fontsize=80, color='red', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 10)).set_duration(2)

text_8 = TextClip(" 前任情侶隨機問彼此一系列問題", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2.85).set_start(2)

text_9 = TextClip(" 他們可以選擇回答問題或是喝一杯", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2.5).set_start(4.85)

text_10 = TextClip(" 我們曾經是男女朋友", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(10)

text_11 = TextClip(" 我們是短暫的夏日愛火", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2).set_start(11)

text_12 = TextClip(" 我們交往一年半", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(13)

text_13 = TextClip(" 她和我的室友約會過", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(15)

text_14 = TextClip(" 我和他的死黨約過一次會", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2).set_start(16.5)

text_15 = TextClip(" 才會認識他", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(18.5)

text_16 = TextClip(" 然後九個月之後 我們開始交往", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2.5).set_start(20)
# ##################### subtitles #####################

screen_4 = CompositeVideoClip([Truth.subclip(10.2, "00:00:32.9"), text_6, text_7,
                               text_8, text_9, text_10, text_11, text_12, text_13,
                               text_14, text_15, text_16])




# Screen 5
# ##################### subtitles #####################
text_17 = TextClip(" 你敢不敢把酒放在我身上然後喝光", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(3).set_start(0.5)

text_18 = TextClip(" 如果你不敢 你就要罰兩杯", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(3).set_start(3.5)

text_19 = TextClip(" 什麼意思啊(內心暗爽)", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(6.5)

text_20 = TextClip(" 放身上是哪招", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.2).set_start(7.5)

text_21 = TextClip(" 例如放在你的肚臍上喝嗎", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2.8).set_start(8.7)

text_22 = TextClip(" 不", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(0.8).set_start(13.5)

text_23 = TextClip(" 她灑出來了！", fontsize=70, color='red', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(14.3)

text_24 = TextClip(" 我喝不了啦 (ＸＤ)", fontsize=70, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(19.5)

text_25 = TextClip(" 好 來吧 我來了！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(21)

text_26 = TextClip(" 頭往右邊轉", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(23.5)

text_27 = TextClip(" 不是不是 那是妳的左邊", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(25)
# ##################### subtitles #####################

img2 = ImageClip('shy.png').resize(0.5).set_pos((780, 260)).set_duration(1).set_start(29.7)

screen_5 = CompositeVideoClip([Truth.subclip("00:02:15", "00:02:47"), text_17, text_18,
                               text_19, text_20, text_21, text_22, text_23, text_24,
                               text_25, text_26, text_27, img2])





# Screen 6
# ##################### subtitles #####################
text_28 = TextClip(" 喔 拜託不要...", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.2)

text_29 = TextClip(" 你自慰的時候腦袋有曾冒出過我嗎？", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(2.3).set_start(1.2)

text_30 = TextClip(" 拜託喝了吧", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.2).set_start(3.5)

text_31 = TextClip(" 爸拖喝吧 OTZ", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.2).set_start(5.7)

text_32 = TextClip(" 不管答案是什麼我都不想知道", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.8).set_start(7.2)

text_33 = TextClip(" 謝謝你", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(10.3)

text_34 = TextClip(" 有啊！        ", fontsize=70, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 595)).set_duration(0.6).set_start(12.4)

text_35 = TextClip("        真的嗎？", fontsize=90, color='red', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 580)).set_duration(1.3).set_start(12.7)

text_36 = TextClip("            有嗎？", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(14)

text_37 = TextClip(" 有時候會啊              ", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(14.5)

text_38 = TextClip(" 妳知道妳可以打給我的 (A__A)", fontsize=70, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 595)).set_duration(1.5).set_start(16.2)

text_39 = TextClip(" 當妳想到的時候", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(18)

text_40 = TextClip(" 才不要！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 595)).set_duration(1).set_start(19.5)

text_41 = TextClip(" 這是... 這是我『獨處』的時間！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 595)).set_duration(2).set_start(20.5)
# ##################### subtitles #####################

img3 = ImageClip('shy.png').resize(0.7).set_pos((720, 120)).set_duration(1.8).set_start(21)

screen_6 = CompositeVideoClip([Truth.subclip("00:03:41.7", "00:04:04.7"), text_28, text_29,
                               text_30, text_31, text_32, text_33, text_34, text_35,
                               text_36, text_37, text_38, text_39, text_40, text_41, img3])



# Screen 7 - 1
# ##################### subtitles #####################
text_42 = TextClip(" 妳敢不敢...", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.8).set_start(0.4)

text_43 = TextClip(" 跟我接吻", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(3.3)

text_44 = TextClip(" 什麼？！", fontsize=70, color='yellow', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 595)).set_duration(0.8).set_start(9)
# ##################### subtitles #####################

screen_7_1 = CompositeVideoClip([Truth.subclip("00:04:55.7", "00:05:05.7"), text_42, text_43, text_44])


# Screen 7 - 2
# ##################### subtitles #####################
text_45 = TextClip(" 我寧願親你的嘴也不要喝那杯純的威士忌", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 580)).set_duration(3.1).set_start(0.2)

text_46 = TextClip(" 好 那就來吧！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(0.8).set_start(3.6)

text_47 = TextClip(" 好 來吧", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(0.8).set_start(4.4)

text_48 = TextClip(" 來啊", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(0.6).set_start(5.6)

text_49 = TextClip(" 1 2 3 來！", fontsize=80, color='red', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 590)).set_duration(1).set_start(6.2)

text_50 = TextClip(" 喝酒囉！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(17)

text_51 = TextClip(" 我們應該給你們拍拍手", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 510)).set_duration(2.3).set_start(18)

text_52 = TextClip(" 好朋友啦", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1).set_start(22)

text_53 = TextClip(" 敬友誼！", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(23.5)

text_54 = TextClip(" 還有親親", fontsize=60, color='cyan', stroke_color="#000000", stroke_width=1,
                 font=font).set_pos(("center", 600)).set_duration(1.5).set_start(25.5)
# ##################### subtitles #####################

screen_7_2 = CompositeVideoClip([Truth.subclip("00:05:24.3", "00:05:53"), text_45, text_46, text_47,
                                 text_48, text_49, text_50, text_51, text_52, text_53, text_54])

sub_clip = Truth.subclip("00:05:50.3", "00:05:53")
sub_clip2 = sub_clip.fx(vfx.time_mirror)

# speedup, time_mirror, brighten and fade_out
clip1 = concatenate_videoclips([sub_clip2.speedx(1.2), sub_clip.speedx(1.5).fx(vfx.colorx, 1.2)])
clip2 = concatenate_videoclips([sub_clip2.speedx(1.8).fx(vfx.colorx, 1.3), sub_clip.speedx(2).fx(vfx.colorx, 1.5)])
ending = concatenate_videoclips([clip1, clip2]).fadeout(1)

screen_7_2 = concatenate_videoclips([screen_7_2, ending])



# Export final movie
final_movie = concatenate_videoclips([screen_1, screen_2, screen_3, screen_4, screen_5, screen_6,
                                      screen_7_1, screen_7_2])

final_movie.write_videofile("taipeipy_demo.mp4", fps=4)
