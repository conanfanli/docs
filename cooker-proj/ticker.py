#!/usr/bin/env python3
from threading import Timer
import tmates


def tick():
    tmates.main()
    Timer(10, tmates.main).start()


tick()
