
import pyautogui, time, datetime

msg = input("Enter your messages: ")
print("-----Only Integer-----")
many = input("How many time?: ")
print("-----Only Decimal or Integer( 0 Is Support)-----")
Delay = input("Delay: ")

count = 5
manynow = int(0)

print("Please Cick at Place do you want to Spam!!")
print("start in..")

for i in range(5):
    print(count)
    count -= 1
    time.sleep(1)

for i in range(0, int(many)):
    pyautogui.typewrite(str(msg) + "\n")
    time.sleep(float(Delay))
    now = datetime.datetime.now()
    manynow += 1
    print("[" + str(now)  + "]" + " send " + msg + " " + str(manynow) + " times")