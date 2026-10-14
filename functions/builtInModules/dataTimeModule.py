### Importing a module 
import datetime as nnnn

# nnnn.datetime()
# datetime.date()
# datetime.time()

# from datetime import *

# datetime()
# date()
# time()

# from datetime import datetime as xyz , date as dt , time as tm

# xyz()
# dt()
# tm()
#### Datetime Object ###
from datetime import datetime , date , time
from time import time as tm
### Creating datetime object
dtObj = datetime(2000 , 3 , 12 , 14, 23,11, 234)
print("Created Date And Time Object ",dtObj)
### Creating date object
dateObj = date(2000 , 3 , 12)
print("Created Date Object ",dateObj)

tmObj = time(2, 45,34, 1111)
print("Time Object " , tmObj)

### Creating current datetime Object
curDtObj = datetime.today()
print("Current Date and Time ", curDtObj)

### Creating current date Object
curDateObj = date.today()
print("Current Date  ", curDateObj)

### Creating current time Object
curTmObj = tm()
print("Current Date  ", curTmObj)

