def capture_stream(args):
    # Handle image, video or webcam
    image_flag = False
    # Check if the input is a webcam
    if args.i == 'CAM':
        args.i = 0
    elif args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        image_flag = True

    # Get and open video capture

    capture = cv2.VideoCapture(args.i)
    capture.open(args.i)


    # Re-size the frame to 100*100
    frame = cv2.resize(frame,(100,100))

    # Add Canny Edge Detection to the frame,
    # with min & max values of 100 and 200
    # Make sure to use np.dstack after to make a 3-channel image

    frame = cv2.Canny(frame, 100, 200)
    frame = np.dstack(frame, frame, frame)

    # Write out the frame, depending on image or video
    if image_flag:
        frame = cv2.imwrite('output_image.jpg', frame)
    else:
        out.write(frame)

    # Close the stream and any windows at the end of the application
    if not image_flag:
        out.release()
    cap.release()
    cv2.DestroyAllWindows()