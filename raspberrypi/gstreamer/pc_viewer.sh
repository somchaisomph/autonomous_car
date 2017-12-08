#!/usr/bin
FILE_SINK=xxxx.h264
LOCAL_PORT=xxxx

clear
gst-launch-1.0 udpsrc port=$LOCAL_PORT ! \
application/x-rtp, payload=96,encoding-name=H264 ! \
rtpjitterbuffer ! \
rtph264depay ! \
tee name=t ! \
queue ! \
mpegtsmux ! \
filesink location=$FILE_SINK t. ! \
queue ! \
avdec_h264 ! \
videoconvert ! \
autovideosink  sync=false
