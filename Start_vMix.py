import requests
import time
import os

get_status_url = 'http://192.168.254.25:8088/api'
recording_on = 'multiCorder>True</multiCorder>'
lauchvMixProfile = '''start "" "C:\\Users\\frank\Documents\\vMixStorage\\user_data\\Good_Setup.vmix"'''

launchAttempt = 0

print('code started')



#check if vmix is launched
while 1:
    
    try:
        response = requests.get(get_status_url)
        print(response)
        if response.status_code == 200:
            break

    
    except:
        if launchAttempt<5:
            print("no response from vMix. Launching profule attempt");
            #attempt to open profile
            os.system(lauchvMixProfile)
            launchAttempt+=1
            time.sleep(10)
        else:
            print('max amount of vMix launch attempts.')
            #put error notification here
            
            print('code halted')
            exit()

    time.sleep(5)



print('vMix is active')
#check for recording

recordAttempt = 0 

while 1:


    response = requests.get(get_status_url).content
    if recording_on in response.decode():
        print("recording!!!")

        break
    elif recordAttempt<5:
        print("not recording attempting to record")
        #start recording!
        requests.get('http://192.168.254.25:8088/api/?Function=StartMultiCorder')
        recordAttempt+=1
    else:
        print('max amount of recording attempts achieved. Halting program')
        exit()


    time.sleep(5)


print("done")

