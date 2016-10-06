Taipei Python User Group: 2016 August
========

[![Build Status](https://travis-ci.org/AaronYALai/TaipeiPy_201608.svg?branch=master)](https://travis-ci.org/AaronYALai/TaipeiPy_201608)
[![Coverage Status](https://coveralls.io/repos/github/AaronYALai/TaipeiPy_201608/badge.svg?branch=master)](https://coveralls.io/github/AaronYALai/TaipeiPy_201608?branch=master)

#### MoviePy: video editing by scripts 

About
--------
This repo is about the talk shared in August, 2016 on **Taipei Python User Group** (Taipei.Py) monthly meetup.

Meetup Link: [taipeipy201608](http://www.meetup.com/Taipei-py/events/233525778/)

Introduce a Python module to edit and compose videos or create special effects by scripts, which could play as the backend to empower the automatic AI video editing.

Content
--------
- Basics: TextClip, ImageClip, VideoClip, AudioClip
- Properties: set_position, set_duration, set_start, set_opacity
- Texts: fontsize, color, font, stroke
- Effects: fadein, crop, mirror, brighten, speedup
- Screens: CompositeVideo, concatenate, resize, clips_array
- Audio: adjust volume
- Export: fps, codec, bitrate, audio_fps, audio_codec, audio_bitrate

Usage
--------
Clone the repo and use the [virtualenv](http://www.virtualenv.org/):

    git clone https://github.com/AaronYALai/TaipeiPy_201608

    cd TaipeiPy_201608

    virtualenv venv

    source venv/bin/activate

Install all dependencies and run the model:

    pip install -r requirements.txt

    python make_movie.py


Sources
--------

[**Video Source**](https://www.youtube.com/watch?v=pxYpvNMbdXQ)

[**Subtitle Source**](https://www.youtube.com/watch?v=H62IK-V73jw)

Not owning the rights to the source video.

No copyright infringement intended.

The video is only for this practice.
