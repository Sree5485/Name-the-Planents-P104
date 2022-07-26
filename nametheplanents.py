import cv2

img=cv2.imread("solar-system.jpg")
text="Sun"
cv2.putText( img,text,(120,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 2,color=(00,00,255))
planet1="Mercury"
cv2.putText( img,planet1,(110,240),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.7,color=(255,255,255))
planet2="Venus"
cv2.putText( img,planet2,(190,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.7,color=(255,255,255))
planet3="Earth"
cv2.putText( img,planet3,(290,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.7,color=(255,255,255))
Moon="Moon"
cv2.putText( img,Moon,(320,155),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.7,color=(255,255))
planet4="Mars"
cv2.putText( img,planet4,(380,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.7,color=(255,255,255))
planet5="Jupiter"
cv2.putText( img,planet5,(530,380),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.9,color=(255,255,255))
planet6="Saturn"
cv2.putText( img,planet6,(750,310),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.9,color=(255,255,255))
planet7="Uranus"
cv2.putText( img,planet7,(960,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.9,color=(255,255,255))
planet8="Neptune"
cv2.putText( img,planet8,(1100,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale= 0.9,color=(255,255,255))
cv2.imshow("OUTPUT",img)
cv2.waitKey(0)