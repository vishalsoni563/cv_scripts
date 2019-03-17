import cv2 as c

def main():
    cap = c.VideoCapture(0)
    filename = "/home/vishal/test/cv/output/saved_feed.mp4"
    codec = c.VideoWriter_fourcc('X', 'V', 'I','D')
    framerate = 60
    resolution = (640, 480)
    VideoFileOutput = c.VideoWriter(filename, codec, framerate, resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:
      ret, frame = cap.read()
      #grey video conversion
      output = c.cvtColor(frame, c.COLOR_BGR2GRAY)
      VideoFileOutput.write(frame)
      c.imshow('window', output)
      #termination when escape is pressed
      if c.waitKey(1) == 27:
          break
    c.destroyAllWindows()
    VideoFileOutput.release()
    cap.release()

#execution begins 
main()
