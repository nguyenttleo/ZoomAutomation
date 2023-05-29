import schedule
import time
from zoomFuncs import *
from testing import *

# time to join meeing
weekdayTimers = ['07:18', '09:03', '11:33']
weekdayEnd = ['08:50', '10:40', '12:46']
wedTimers = ['07:18', '08:48', '11:03']
wedEnd = ['08:35', '10:10', '12:01']

# codes and passwords to zoom rooms
classCode = 'YOUR-CODE'
classPass = 'YOUR-PASS'

schedule.every().wednesday.at('11:04').do(joinMeeting(classCode, classPass))
schedule.every().wednesday.at('11:04').do(leaveMeeting())
# schedule.every().tuesday.at('11:33').do(joinMeeting(classCode, classPass))
# schedule.every().thursday.at('11:33').do(joinMeeting(classCode, classPass))
# schedule.every().friday.at('11:33').do(joinMeeting(classCode, classPass))

while True:
    schedule.run_pending()
    time.sleep(1)
