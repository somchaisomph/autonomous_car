#!/bin/bash
REMOTE_ADDR=xxx.xxxx.xxxx.xxxx
REMOTE_PORT=xxxx
VIDEO_WIDTH=xxx
VIDEO_HEIGHT=xxxx

clear
gst-launch-1.0  v4l2src device=/dev/video0  ! \
video/x-h264,width=$VIDEO_WIDTH,height=$VIDEO_HEIGHT !  \
h264parse ! rtph264pay config-interval=1 pt=96 ! \
udpsink host=$REMOTE_ADDR port=$REMOTE_PORT
