from ursina import *
import cv2
from PIL import Image as im
import mediapipe as mp
from direct.actor.Actor import Actor


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands=mp_hands.Hands(model_complexity=1,min_detection_confidence=0.6,min_tracking_confidence=0.6)

app = Ursina()
window.size=(800,800)
v=Entity(model="quad",position=(0,0,10),scale=15,color=color.white)
cap = cv2.VideoCapture(0)
ent=Entity(position=(0,0,-1),scale=25,collider="mesh")

actor = Actor('minonew.glb')
actor.setPos(0,-0.05,0)
#actor.setHpr(actor,0,90,180)

actor.reparent_to(ent)
actor.loop(actor.get_anim_names()[0])


def update():    
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    
    frame.flags.writeable = True
    
    fingerCount = 0
    if results.multi_hand_landmarks:
        
        for hand_landmarks in results.multi_hand_landmarks: 
            
            handIndex = results.multi_hand_landmarks.index(hand_landmarks)
            handLabel = results.multi_handedness[handIndex].classification[0].label
            thumb_tip=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            thumb_ip=hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
            index_tip=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_pip=hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
            middle_tip=hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            middle_pip=hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
            ring_tip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
            ring_pip=hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
           
            if handLabel == "Left" and thumb_tip.x > thumb_ip.x:
                fingerCount = fingerCount+1
            elif handLabel == "Right" and thumb_tip.x < thumb_ip.x:
                fingerCount = fingerCount+1

            if index_tip.y < index_pip.y:
                
                indf = True
            else:
                indf=False

            if middle_tip.y < middle_pip.y:     
                mf = True
            else:
                mf=False
            if ring_tip.y < ring_pip.y:
                rf=True
            else:
                rf=False
                
            #if handLandmarks[20][1] < handLandmarks[18][1]:     #Pinky
            #    fingerCount = fingerCount+1
                    
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            if indf==True and mf==True and rf==False:
                nx=(0.5-index_tip.x)*10
                ny=(0.5-index_tip.y)*10 
                ent.world_position=(nx,ny,1)
                #print(index_tip.z)
            if  indf==True and mf==False and rf==False:
                nx=(0.5-index_tip.x)*180
                ny=(0.5-index_tip.y)*180
                nz=-(index_tip.z*180)
                ent.world_rotation=(nx,ny,nz)
            if  indf==True and mf==True and rf==True:
                ent.world_scale=int(index_tip.y*50)
            

    frame=cv2.flip(frame, 1)
    data = im.fromarray(frame)
    data= data.convert("RGBA")
    av=Texture(data)
    v.texture=av
    
def input(key):
    if key=='q':
        application.quit()

EditorCamera()
app.run()