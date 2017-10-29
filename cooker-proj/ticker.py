#!/usr/bin/env python3
from threading import Timer
import tmates


def tick():
    tmate = tmates.Tmate()
    tmate.update_session()
    Timer(30, tick).start()


tick()
