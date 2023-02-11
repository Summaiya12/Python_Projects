from time import *
import random as r

def mistake(partest,usertest):
      error=0
      for i in range(len(partest)):
            try:
                  if partest[i] != usertest[i]:
                        error = error + 1
            except:
                  error = error + 1
      return error

def speed_time(time_s,time_e,userinput):
      time_delay = time_e-time_s
      time_R = round(time_delay,2)
      speed=len(userinput)/time_R
      return round(speed)
if __name__ == '__main__':
 while True:
      ck=input("Ready to test: yes/no : ")
      if ck == "yes":
          test=["Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
                "Lorem Ipsum has been the industry's standard dummy text.",
                " when an unknown printer took a galley of type and scrambled.",
                "It has survived not only five centuries, but also the leap into electronic typesetting.",
                "1960s with the release of Letraset sheets containing Lorem Ipsum passages." ]
          test1 = r.choice(test)
          print("******** Typing Speed Calculator ********")
          print(test1)
          print()#line vreak
          print()#line break
          time_1 = time()
          testinput=input("Enter :")
          time_2 = time()
          print( 'Speed:',speed_time(time_1,time_2,testinput),"w/sec")
          print("Error:",mistake(test1,testinput))
      elif ck == 'no':
            print("Thank You...!")
            break
      else:
            print("Wrong Input")


yes
