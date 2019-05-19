import datetime
from datetime import timedelta
sched1 = {'Mon':'Day Shift',
          'Tues':'Day Shift',
          'Wed':'Day Shift',
          'Thur':'off',
          'Fri':'off',
          'Sat':'off'}

sched2 = {'Mon':'Night Shift',
          'Tues':'Night Shift',
          'Wed':'off',
          'Thur':'off',
          'Fri':'off',
          'Sat':'off',
          'Sun':'Night Shift'}

sched3 = {'Mon':'off',
          'Tues':'off',
          'Wed':'off',
          'Thur':'Day Shift',
          'Fri':'Day Shift',
          'Sat':'Day Shift',
          'Sun':'off'}

sched4 = {'Mon':'off',
          'Tues':'off',
          'Wed':'Night Shift',
          'Thur':'Night Shift',
          'Fri':'Night Shift',
          'Sat':'off',
          'Sun':'Off'}

shift = int(input("Enter your shift nr: "))

pickdate1 = int(input("Enter a date in the year (YYYY)): "))
pickdate2 = int(input("Enter a date in the year (MM): "))
pickdate3 = int(input("Enter a date in the year (DD): "))

date = datetime.date(pickdate1,pickdate2,pickdate3)
weekno = datetime.date(pickdate1,pickdate2,pickdate3).isocalendar()[1] # numer tygodnia w roku
weekday = datetime.date.isoweekday(date) #numer dnia
sched = "Day Off"

if weekno % 2 != 0 and shift == 4:
        if weekday == 1:
            print ("It's monday, you are: %s" %  (sched1['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, you are: %s" %  (sched1['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, you are: %s" %  (sched1['Wed']))
        elif weekday == 4:
            print ("It's Thursday, you are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, you are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, you are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, you are: %s" %  (sched))

elif weekno % 3 == 0 and shift == 4:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched3['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched3['Fri']))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched3['Sat']))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))


elif weekno % 4 == 0 and shift == 4:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched4['Wed']))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched4['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched4['Fri']))
        elif weekday == 6:
            print ("It's Satday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))        



elif weekno % 2 == 0 and shift == 4:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched2['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched2['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched2['Sun']))


if weekno % 3 == 0 and shift == 1:
        if weekday == 1:
            print ("It's monday, you are: %s" %  (sched1['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, you are: %s" %  (sched1['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, you are: %s" %  (sched1['Wed']))
        elif weekday == 4:
            print ("It's Thursday, you are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, you are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, you are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, you are: %s" %  (sched))

elif weekno % 2 != 0 and shift == 1:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched3['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched3['Fri']))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched3['Sat']))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))


elif weekno % 2 == 0 and shift == 1:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched4['Wed']))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched4['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched4['Fri']))
        elif weekday == 6:
            print ("It's Satday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))        



elif weekno % 4 == 0 and shift == 1:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched2['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched2['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched2['Sun']))



if weekno % 4 == 0 and shift == 3:
        if weekday == 1:
            print ("It's monday, you are: %s" %  (sched1['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, you are: %s" %  (sched1['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, you are: %s" %  (sched1['Wed']))
        elif weekday == 4:
            print ("It's Thursday, you are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, you are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, you are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, you are: %s" %  (sched))

elif weekno % 2 == 0 and shift == 3:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched3['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched3['Fri']))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched3['Sat']))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))


elif weekno % 3 == 0 and shift == 3:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched4['Wed']))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched4['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched4['Fri']))
        elif weekday == 6:
            print ("It's Satday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))        



elif weekno % 2 != 0 and shift == 3:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched2['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched2['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched2['Sun']))




if weekno % 2 == 0 and shift == 2:
        if weekday == 1:
            print ("It's monday, you are: %s" %  (sched1['Mon']))
        elif weekday == 2:
            print ("It's Tuesday, you are: %s" %  (sched1['Tues']))
        elif weekday == 3:
            print ("It's Wednesday, you are: %s" %  (sched1['Wed']))
        elif weekday == 4:
            print ("It's Thursday, you are: %s" %  (sched))
        elif weekday == 5:
            print ("It's Friday, you are: %s" %  (sched))
        elif weekday == 6:
            print ("It's Saturday, you are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, you are: %s" %  (sched))

elif weekno % 4 == 0 and shift == 2:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched3['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched3['Fri']))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched3['Sat']))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))


elif weekno % 2 != 0 and shift == 2:
        if weekday == 1:
            print ("It's Monday, You are: %s" % (sched))
        elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched))
        elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched4['Wed']))
        elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched4['Thur']))
        elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched4['Fri']))
        elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched))
        elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched))        



elif weekno % 3 == 0 and shift == 2:
    if weekday == 1:
            print ("It's Monday, You are: %s" % (sched2['Mon']))
    elif weekday == 2:
            print ("It's Tuesday, You are: %s" % (sched2['Tues']))
    elif weekday == 3:
            print ("It's Wednesday, You are: %s" % (sched))
    elif weekday == 4:
            print ("It's Thursday, You are: %s" %  (sched))
    elif weekday == 5:
            print ("It's Friday, You are: %s" %  (sched))
    elif weekday == 6:
            print ("It's Saturday, You are: %s" %  (sched))
    elif weekday == 7:
            print ("It's Sunday, You are: %s" %  (sched2['Sun']))

