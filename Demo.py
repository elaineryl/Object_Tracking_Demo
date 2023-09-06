import sys
import cv2

# creating tracker
tracker = cv2.legacy.TrackerMOSSE.create()
print(tracker)

# loading in the video file
video = cv2.VideoCapture("SpaceX.mp4")

if not video.isOpened():
    print("oops video not opened")
    sys.exit()

# reading the first frame of the video
ok, frame = video.read()

# define our output video
frame_height, frame_width = frame.shape[:2]

# Resize the video for a more convinient view
# frame = cv2.resize(frame, [frame_width//2, frame_height//2])

fps = int(video.get(cv2.CAP_PROP_FPS))
video_codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
output = cv2.VideoWriter("output.mp4", video_codec, fps, (frame_width, frame_height))

# define bounding box using the first frame
bbox = cv2.selectROI(frame)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

while True:
    # constantly reading frames
    ok, frame = video.read()
    # frame = cv2.resize(frame, [frame_width//2, frame_height//2])

    if not ok:
        print("End of the video")
        break

    # update tracker at each frame with ROI
    ok, bbox = tracker.update(frame)

    # drawing out the boundary box
    if ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        print(True, bbox)
        output.write(frame)
    else:
        # display error message
        cv2.putText(frame, "No object detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 225), 2)

    # Display tracker type
    cv2.putText(frame, "MOSSE Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(fps), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2);
    cv2.imshow("tracking", frame)

    # quit when ESC is pressed
    k = cv2.waitKey(2) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
