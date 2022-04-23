#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

import copy
import sys
import tempfile
from io import BytesIO

import av

import common.thread_safe_fork
import pycurl
import ti.urlgen.everstore_url_py as everstore_url_py

common.thread_safe_fork.threadSafeForkRegisterAtFork()


def get_video_container(handle, multi_thread_decode=False):
    # Use local data.
    with open(handle, "rb") as fp:
        container = fp.read()
    return container
