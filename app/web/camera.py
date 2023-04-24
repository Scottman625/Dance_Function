import cv2,os,urllib.request
from django.conf import settings
import mediapipe as mp
import numpy as np
from django.shortcuts import render ,redirect
from modelCore.tasks.tasks import calculate_angle
from modelCore.models import *
import json
import datetime

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose.Pose()

global judgement, i, DIC, score
judgement = ''
i = 0
DIC={"LEFTELBOW":[],
        "RIGHTELBOW":[],
        "LEFTSHOULDER":[],
        "RIGHTSHOULDER":[],
        "LEFTHIP":[],
        "RIGHTHIP":[],
        "LEFTKNEE":[],
        "RIGHTKNEE":[]
        }
list = [0]
score = 0
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

def Detect(Image ,Results,dic, judgement, i):
    # global LEFTELBOW,RIGHTELBOW, LEFTSHOULDER, RIGHTSHOULDER, LEFTHIP, RIGHTHIP,LEFTKNEE,RIGHTKNEE
    # Recolor image to RGB
    
    # Extract landmarks
        
    
    try:
        landmarks = Results.pose_landmarks.landmark
        if landmarks is not None:
            LEFT_SHOULDER = [landmarks[12].x,landmarks[12].y]
            LEFT_ELBOW = [landmarks[14].x,landmarks[14].y] 
            LEFT_WRIST = [landmarks[16].x,landmarks[16].y] 
            LEFT_HIP = [landmarks[24].x,landmarks[24].y] 
            LEFT_KNEE=[landmarks[26].x,landmarks[26].y] 
            LEFT_ANKLE=[landmarks[28].x,landmarks[28].y] 
            RIGHT_SHOULDER = [landmarks[11].x,landmarks[11].y]
            RIGHT_HIP = [landmarks[23].x,landmarks[23].y] 
            RIGHT_ELBOW = [landmarks[13].x,landmarks[13].y]
            RIGHT_WRIST = [landmarks[15].x,landmarks[15].y] 
            RIGHT_KNEE = [landmarks[25].x,landmarks[25].y] 
            RIGHT_ANKLE = [landmarks[27].x,landmarks[27].y] 
        
        # Calculate angle
        LEFTELBOW_angle = calculate_angle(LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST) if calculate_angle(LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST) else 0
        RIGHTELBOW_angle = calculate_angle(RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST) if calculate_angle(RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST) else 0
        LEFTSHOULDER_angle = calculate_angle(LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP) if calculate_angle(LEFT_ELBOW, LEFT_SHOULDER, LEFT_HIP) else 0
        RIGHTSHOULDER_angle = calculate_angle(RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP) if calculate_angle(RIGHT_ELBOW, RIGHT_SHOULDER, RIGHT_HIP) else 0
        LEFTHIP_angle = calculate_angle(LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE) if calculate_angle(LEFT_SHOULDER, LEFT_HIP, LEFT_KNEE) else 0
        RIGHTHIP_angle = calculate_angle(RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE) if calculate_angle(RIGHT_SHOULDER, RIGHT_HIP, RIGHT_KNEE) else 0
        LEFTKNEE_angle = calculate_angle(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE) if calculate_angle(LEFT_HIP, LEFT_KNEE, LEFT_ANKLE) else 0
        RIGHTKNEE_angle = calculate_angle(RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE) if calculate_angle(RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE) else 0

        if LEFTSHOULDER_angle != None:
            DIC["LEFTELBOW"].append(LEFTELBOW_angle)
        else:
            DIC["LEFTELBOW"].append(0)
        if RIGHTELBOW_angle != None:
            DIC["RIGHTELBOW"].append(RIGHTELBOW_angle)
        else:
            DIC["RIGHTELBOW"].append(0)
        if LEFTSHOULDER_angle != None:
            DIC["LEFTSHOULDER"].append(LEFTSHOULDER_angle)
        else:
            DIC["LEFTSHOULDER"].append(0)
        if RIGHTSHOULDER_angle != None:              
            DIC["RIGHTSHOULDER"].append(RIGHTSHOULDER_angle)
        else:
            DIC["RIGHTSHOULDER"].append(0)
        if LEFTHIP_angle != None:
            DIC["LEFTHIP"].append(LEFTHIP_angle)
        else:
            DIC["LEFTHIP"].append(0)
        if RIGHTHIP_angle !=None:
            DIC["RIGHTHIP"].append(RIGHTHIP_angle)
        else:
            DIC["RIGHTHIP"].append(0)
        if LEFTKNEE_angle != None:
            DIC["LEFTKNEE"].append(LEFTKNEE_angle)
        else:
            DIC["LEFTKNEE"].append(0)
        if RIGHTKNEE_angle != None:
            DIC["RIGHTKNEE"].append(RIGHTKNEE_angle)
        else:
            DIC["RIGHTKNEE"].append(0)
        
        
        i = len(DIC["LEFTELBOW"])-1

        # LEFTELBOW =  abs(int(DIC["LEFTELBOW"][i]) - int(dic["LEFTELBOW"][i]))
        # RIGHTELBOW =  abs(int(DIC["RIGHTELBOW"][i]) - int(dic["RIGHTELBOW"][i]))
        # LEFTSHOULDER =  abs(int(DIC["LEFTSHOULDER"][i]) - int(dic["LEFTSHOULDER"][i]))
        # RIGHTSHOULDER =  abs(int(DIC["RIGHTSHOULDER"][i]) - int(dic["RIGHTSHOULDER"][i]))
        # LEFTHIP =  abs(int(DIC["LEFTHIP"][i]) - int(dic["LEFTHIP"][i]))
        # RIGHTHIP =  abs(int(DIC["RIGHTHIP"][i]) - int(dic["RIGHTHIP"][i]))
        # LEFTKNEE =  abs(int(DIC["LEFTKNEE"][i]) - int(dic["LEFTKNEE"][i]))
        # RIGHTKNEE =  abs(int(DIC["RIGHTKNEE"][i]) - int(dic["RIGHTKNEE"][i]))

        
        difference = abs(int(DIC["LEFTELBOW"][i]) - int(dic["LEFTELBOW"][i])) + abs(int(DIC["RIGHTELBOW"][i]) - int(dic["RIGHTELBOW"][i])) + abs(int(DIC["LEFTSHOULDER"][i]) - int(dic["LEFTSHOULDER"][i])) +  abs(int(DIC["RIGHTSHOULDER"][i]) - int(dic["RIGHTSHOULDER"][i])) + abs(int(DIC["LEFTHIP"][i]) - int(dic["LEFTHIP"][i])) + abs(int(DIC["RIGHTHIP"][i]) - int(dic["RIGHTHIP"][i]))  + abs(int(DIC["LEFTKNEE"][i]) - int(dic["LEFTKNEE"][i]))  + abs(int(DIC["RIGHTKNEE"][i]) - int(dic["RIGHTKNEE"][i])) 
        if difference <= 70:
            judgement = "Marvelous"     
            list.append(list[i]+5)
        elif difference <= 140:
            judgement = "Perfect"
            list.append(list[i]+3)
                
        elif difference <= 200:
            judgement = "Good"
            list.append(list[i]+1)
        else:
            judgement = "Bad"
            list.append(list[i]+0)

        # print(len(DIC["LEFTELBOW"]))
    
    except:
        pass


        # Render detections
    # cv2.putText(Image, str(LEFTELBOW), 
    #                 tuple(np.multiply(LEFT_ELBOW, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )          
    # cv2.putText(Image, str(RIGHTELBOW), 
    #                 tuple(np.multiply(RIGHT_ELBOW, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(LEFTSHOULDER), 
    #                 tuple(np.multiply(LEFT_SHOULDER, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(RIGHTSHOULDER), 
    #                 tuple(np.multiply(RIGHT_SHOULDER, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(LEFTHIP), 
    #                 tuple(np.multiply(LEFT_HIP, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(RIGHTHIP), 
    #                 tuple(np.multiply(RIGHT_HIP, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(LEFTKNEE), 
    #                 tuple(np.multiply(LEFT_KNEE, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )
    # cv2.putText(Image, str(RIGHTKNEE), 
    #                 tuple(np.multiply(RIGHT_KNEE, [640, 480]).astype(int)), 
    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
    #                     )


    cv2.putText(Image, str(judgement), 
            (20,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

    cv2.putText(Image, str(list[i]), 
            (30,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
    
    return list[i]

class VideoCamera(object):
    
    def __init__(self,dic,video_path,video_id):
        self.video = cv2.VideoCapture(0)
        self.dic = dic
        self.cap = cv2.VideoCapture(video_path)
        self.count = 0
        self.i = i
        self.DIC = DIC
        self.judgement = ''
        self.list = list
        self.video_id = video_id
        self.score = score


    def __del__(self):
        self.video.release()
        self.cap.release()
        # self.judgement = ''
        # self.i = 0

    def get_frame(self,dic):
        # print(len(self.dic["LEFTELBOW"]))
        count = self.count
        while True:
            ret1, frame1 = self.video.read()
            ret2, frame2 = self.cap.read()
            
            if ret2:
                
                count += 1
                
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                frame1.flags.writeable = False
                frame1.flags.writeable = True
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_RGB2BGR)    
                frame1 = cv2.flip(frame1,1)
                cv2.rectangle(frame1, (0,0), (180,50), (255,255,255), -1)

                cv2.rectangle(frame1, (0,380), (150,480), (200,200,200), -1)
                cv2.putText(frame1, "SCORE", 
                        (20,420), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)
                
                
                # with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
                if count % 3 == 1:           
                    # Make detection
                    Results = mp_pose.process(frame1)
                    
                    # Recolor back to BGR           
                    # landmarks = Results.pose_landmarks
                    try:
                        self.score = Detect(frame1,Results,self.dic,self.judgement, self.i)
                        print(self.score)
                    except:
                        global judgement, i, DIC
                        judgement = ''
                        i = 0
                        DIC={"LEFTELBOW":[],
                                "RIGHTELBOW":[],
                                "LEFTSHOULDER":[],
                                "RIGHTSHOULDER":[],
                                "LEFTHIP":[],
                                "RIGHTHIP":[],
                                "LEFTKNEE":[],
                                "RIGHTKNEE":[]
                                }
                        print('except')

                frame1 = cv2.resize(frame1, (900, 540))
                frame2 = cv2.resize(frame2, (900, 540))
                combined = np.concatenate((frame2, frame1), axis=1)

                ret, jpeg = cv2.imencode(".jpg", combined)
                return jpeg.tobytes()

            else:
                self.video.release()
                self.cap.release()
                now = datetime.datetime.now()

                one_minute_ago = now - datetime.timedelta(minutes=1)
                print(one_minute_ago)
                print(score)
                if GameScore.objects.filter(user=User.objects.get(id=1),video=Video.objects.get(id=self.video_id),score=self.score).count() != 0:
                    print('break')
                    break
                print('finish')
                GameScore.objects.create(user=User.objects.get(id=1),video=Video.objects.get(id=self.video_id),score=self.score)
                frame1 = cv2.resize(frame1, (1800, 540))
                frame1[:] = (0,0,0)
                ret, jpeg = cv2.imencode(".jpg", frame1)
                return jpeg.tobytes()



