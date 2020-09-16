# method 1 

# exercise 7 :: Healthy programmer
#
# 9am - 5pm
# water - water.mp3 (3.5 litres) - drank - log
# eyes - eyes.mp3 - every 30 min - eyedone
# physical activity - physical.mp3 every - 45 min - exdone


from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")

if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyessecs = 10
    exercisesecs = 20
    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time .. Enter drank to stop the alarm ")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("drank water")

        if time() - init_eyes > eyessecs:
            print("eyes exercie time .. Enter eye to stop music")
            musiconloop('eyes.mp3','eyes')
            init_eyes = time()
            log_now("Eyes exercise done")

        if time() - init_exercise > exercisesecs:
            print("exercise time ... Enter exercise done to stop music")
            musiconloop('exercise.mp3','exdone')
            init_exercise = time()
            log_now("Exercise Done !! ")
            
           
           
           
           
# method 2           

from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}")

if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyessecs = 10
    exercisesecs = 20
    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time .. Enter drank to stop the alarm ")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("drank water")

        if time() - init_eyes > eyessecs:
            print("eyes exercie time .. Enter eye to stop music")
            musiconloop('eyes.mp3','eyes')
            init_eyes = time()
            log_now("Eyes exercise done")

        if time() - init_exercise > exercisesecs:
            print("exercise time ... Enter exercise done to stop music")
            musiconloop('exercise.mp3','exdone')
            init_exercise = time()
            log_now("Exercise Done !! ")
