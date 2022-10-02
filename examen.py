import cv2

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)


if (webcam.isOpened() == False):
  print("Error abriendo la webcam")

while (webcam.isOpened()):

  ret, frame = webcam.read()
  if ret == True:
      color = cv2.bilateralFilter(frame, 9, 9, 7)
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      blur = cv2.medianBlur(gray, 7)
      edges = cv2.adaptiveThreshold(
          blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
      frame_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
      cartoon = cv2.bitwise_and(color, frame_edge)
  # MOSTRAR RESULTADO
      cv2.imshow('Cartoon', cartoon)
  # Q PARA SALIR
      if cv2.waitKey(25) == ord('q'):
          break
          # S PARA SREENSHOT
      elif cv2.waitKey(25) == ord('s'):
          cv2.imwrite('screenshot.png', cartoon)


webcam.release()

cv2.destroyAllWindows()
