import cv2
from google.colab.patches import cv2_imshow

helmet_detector = cv2.CascadeClassifier('/content/haarcascade_helmet (2).xml')
person_detector = cv2.CascadeClassifier('/content/haarcascade_upperbody.xml')

image = cv2.imread('/content/mini1.jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

helmets = helmet_detector.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
persons = person_detector.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

for (x, y, w, h) in helmets:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

for (x, y, w, h) in persons:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2_imshow(image)

if len(persons) >= 2:
    print("Only two people are allowed on the bike.")
    print("Only two people are allowed on the bike.")
else:
    print("Alert: Only two people are allowed on the bike.")

if len(helmets) > 0:
    print("Good to go! Helmets are being worn.")
    print("Alert: Helmets should be worn.")
!pip install twilio
from twilio.rest import Client

account_sid = 'AC7abc6f943d38421eb275785401199ba7'
auth_token = 'aba206202afd72e29502ccd25466d1aa'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18577464011',
  to='+918688620129',
  body="Alert: Only two people are allowed on a bike! have a safe ride and please wear the helmet." # Add the body parameter here
)

print(message.sid)# MiniProject
