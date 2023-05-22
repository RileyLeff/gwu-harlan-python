# imports
import random as rand
import datetime as dt
import csv

# path 
out_path = 'data/cats.csv'

# parameters
datasize = 2000
start = dt.datetime(2019, 3, 13)
end = dt.datetime.now()

cats = ['otto', 'ozzy']

activities = [
    'jumped', 
    'purred', 
    'scratched', 
    'committed_crimes',
    'meowed',
    'snoozed',
    'hissed',
    'chomped',
    'pondered',
    'nibbled',
]

where = [
    'couch',
    'bed',
    'bathtub',
    'shelf',
    'kitchen',
    'national_mall',
    'seh',
    'bell_hall',
    'tastykabob',
    'white_house',
    'windowsill'
]



def get_random_bounded_date(start, end):
    return(start + (end - start) * rand.random())

date = []
cat = []
activity = []
location = []



while len(date) < datasize:
    date.append(str(get_random_bounded_date(start, end)))
    cat.append(cats[rand.randint(0,1)])
    activity.append(activities[rand.randint(0,len(activities) - 1)])
    location.append(where[rand.randint(0, len(where)  - 1)])

#open('file.txt', 'w').close()


with open(out_path, 'w', newline = '') as fil:
    catwriter = csv.writer(fil, delimiter=',')
    header = ['timestamp', 'cat', 'activity', 'location']
    catwriter.writerow(header)
    for i in range(0,datasize):
        outlist = [date[i], cat[i], activity[i], location[i]]
        catwriter.writerow(outlist)



#   which cat appears most frequently?
#   which cat/activity/location combo appears most frequently? 
#   what's the longest streak of one cat consecutively?
#   what's the longest streak of alternating cats?
#   do all unique combos occur?
#   which unique combo takes the longest to occur?