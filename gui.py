import tkinter as tk
from tkinter import filedialog
from tkinter import *

from PIL import ImageTk, Image
import os
import numpy
from gtts import gTTS
import playsound
from keras.models import load_model
from pydub import AudioSegment
from pydub.generators import Sine
print("Current working directory:", os.getcwd())

global model 

try:
    model = load_model('traffic_classifier.h5')
except Exception as e:
    print("Error loading the model:",e)
#dictionary to label all traffic signs class.
classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)',      
            3:'Speed limit (50km/h)',       
            4:'Speed limit (60km/h)',      
            5:'Speed limit (70km/h)',    
            6:'Speed limit (80km/h)',      
            7:'End of speed limit (80km/h)',     
            # 8:'Speed limit (100km/h)',    
            # 9:'Speed limit (120km/h)',     
           10:'No passing',   
           11:'No passing veh over 3.5 tons',     
           12:'Right-of-way at intersection',     
           13:'Priority road',    
           14:'Yield',     
           15:'Stop',       
           16:'No vehicles',       
           17:'Veh > 3.5 tons prohibited',       
           18:'No entry',       
           19:'General caution',     
           20:'Dangerous curve left',      
           21:'Dangerous curve right',   
           22:'Double curve',      
           23:'Bumpy road',     
           24:'Slippery road',       
           25:'Road narrows on the right',  
           26:'Road work',    
           27:'Traffic signals',      
           28:'Pedestrians',     
           29:'Children crossing',     
           30:'Bicycles crossing',       
           31:'Beware of ice/snow',
           32:'Wild animals crossing',      
           33:'End speed + passing limits',      
           34:'Turn right ahead',     
           35:'Turn left ahead',       
           36:'Ahead only',      
           37:'Go straight or right',      
           38:'Go straight or left',      
           39:'Keep right',     
           40:'Keep left',      
           41:'Roundabout mandatory',     
           42:'End of no passing',      
           43:'End no passing veh > 3.5 tons' }
 
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)
import time
import os
if not os.path.exists("audio_outputs"):
    os.mkdir("audio_outputs")
audio_counter = 0
def classify(file_path):
    global model
    
    global label_packed
    global audio_counter
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    #pred = numpy.argmax(model.predict([image])[0])
    pred = numpy.argmax(model.predict([image])[0])
    #pred=model.predict([image])[0].astype("int32")
    #pred_x=model.predict([image])[0]
    # # classes_x=numpy.argmax(pred_x)
    #print(pred)
    sign = classes[pred + 1]
    print(sign)
    timestamp = int(time.time())
    audio_filename =  f'audio_outputs/output_{audio_counter}.mp3'
    audio_counter += 1
    if "Speed limit" in sign:
        speed_limit = sign.split("(")[1].split(")")[0]
        audio_message = f"BE ALERT, Speed limit {speed_limit} ahead. Please reduce your speed to {speed_limit} ."
    elif "Stop" in sign:
        audio_message = f"be alert, Stop sign ahead. Please come to a complete stop."
    elif "Yield" in sign:
        audio_message = f"be alert, Yield sign ahead. Please yield the right of way."
    elif "No passing" in sign:
        audio_message = f"be alert, No passing zone ahead. Please do not overtake other vehicles."
    elif "Right-of-way at intersection" in sign:
        audio_message = f"be alert, Right-of-way at intersection sign ahead. Please follow right-of-way rules."
    elif "Priority road" in sign:
        audio_message = f"be alert, Priority road ahead. Please yield the right of way if necessary."
    elif "General caution" in sign:
        audio_message = f"Be alert, General caution sign ahead. Please be alert and drive safely."
    elif "Dangerous curve left" in sign:
        audio_message = f"be alert, Dangerous curve to the left ahead. Please approach with caution."
    elif "Dangerous curve right" in sign:
        audio_message = f"be alert, Dangerous curve to the right ahead. Please approach with caution."
    elif "Double curve" in sign:
        audio_message = f"be alert, Double curve ahead. Please be prepared for multiple curves."
    elif "Bumpy road" in sign:
        audio_message = f" be alert, Bumpy road ahead. Please drive carefully."
    elif "Slippery road" in sign:
        audio_message = f"be alert, Slippery road ahead. Please reduce your speed and use caution."
    elif "Road narrows on the right" in sign:
        audio_message = f"be alert, Road narrows on the right ahead. Please be prepared to merge left."
    elif "Road work" in sign:
        audio_message = f"be alert, Road work ahead. Please slow down and follow posted signs."
    elif "Traffic signals" in sign:
        audio_message = f"be alert, Traffic signals ahead. Please obey traffic signals and signs."
    elif "Pedestrians" in sign:
        audio_message = f"be alert, Pedestrians ahead. Please watch for pedestrians and yield if necessary."
    elif "Children crossing" in sign:
        audio_message = f"be alert, Children crossing ahead. Please drive slowly and watch for children."
    elif "Bicycles crossing" in sign:
        audio_message = f"be alert, Bicycles crossing ahead. Please be alert and share the road with cyclists."
    elif "Beware of ice/snow" in sign:
        audio_message = f"be alert, Beware of ice or snow ahead. Please drive carefully in icy or snowy conditions."
    elif "Wild animals crossing" in sign:
        audio_message = f"be alert, Wild animals crossing ahead. Please be prepared to stop for animals."
    elif "End speed + passing limits" in sign:
        audio_message = f"be alert, End of speed and passing limits ahead. Please obey normal traffic rules."
    elif "Turn right ahead" in sign:
        audio_message = f" be alert, Turn right ahead. Please prepare to make a right turn."
    elif "Turn left ahead" in sign:
        audio_message = f"be alert, Turn left ahead. Please prepare to make a left turn."
    elif "Ahead only" in sign:
        audio_message = f"be alert, Ahead only. Please proceed straight ahead."
    elif "Go straight or right" in sign:
        audio_message = f"be alert, Go straight or turn right ahead. Please choose the appropriate lane."
    elif "Go straight or left" in sign:
        audio_message = f"be alert, Go straight or turn left ahead. Please choose the appropriate lane."
    elif "Keep right" in sign:
        audio_message = f"be alert, Keep right ahead. Please stay in the right lane."
    elif "Keep left" in sign:
        audio_message = f"be alert, Keep left ahead. Please stay in the left lane."
    elif "Roundabout mandatory" in sign:
        audio_message = f"be alert, Roundabout mandatory sign ahead. Please enter the roundabout if required."
    elif "End of no passing" in sign:
        audio_message = f"be alert, End of no passing zone ahead. You may resume passing if safe."
    elif "End no passing veh > 3.5 tons" in sign:
        audio_message = f"be alert, End of no passing zone for vehicles over 3.5 tons ahead."
    else:
        audio_message = f"be alert, {sign} ahead. Please exercise caution and drive safely."
    

    tts = gTTS(text=audio_message, lang='en')  # Change 'en' to the appropriate language code if needed
    tts.save(audio_filename)
    
    # Play the audio
    playsound.playsound(audio_filename)
    label.configure(foreground='#011638', text=sign) 
   

def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda:classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',12,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',12,'bold'))

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Know Your Traffic Sign",pady=20, font=('arial',22,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
