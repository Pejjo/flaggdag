import datetime
import dateutil.easter
class flaggdag:

  def __init__(self, year):
    self.initYear(year)
    self.easter=None
    self.midsummer=None
    self.allhelgon=None
    self.valdagen=None
    self.flagdays=[]
    self.holidays=[]

  def initYear(self, year): 
    print("Initializing year ", year)
    self.year=year

    self.easter = dateutil.easter.easter(year, method=3)
    print("Påsk: ", self.easter)

    midsummerStart = datetime.date(year, 6, 21) # Get timestamp of first day in midsummer week
    midsummerSunDay = 21 + (6-midsummerStart.weekday()) #Adjust to sunday
    self.midsummer = datetime.date(year, 6, (midsummerSunDay -1))
    print("Midsommar ", self.midsummer)

    allhelgonStart = datetime.date(year,11,1) # Get timestamp of first day in allhelgona week
    allhelgonSunDay= 1 + (6-allhelgonStart.weekday());
    self.allhelgon = datetime.date(year, 11, allhelgonSunDay) - datetime.timedelta(days=1)
    print("Allhelgon ", self.allhelgon)
 
    if ((year >= 2014) and (((year - 2014) % 4) ==0)): #Third sunday before 2014 and every third year before 1994. But too late to vote in those elections, so just skip. 
      valStart = datetime.date(year,9,8) # Get timestamp of first day that can be second synday of month
      valSunDay= 8 + (6-valStart.weekday());
      self.valdagen = datetime.datetime(year, 9, valSunDay)
      print("Valdagen ", self.valdagen)
    else:
      self.valdagen=None

   
    self.holidays=[]
    
    # First BOTH holiday and flagday 
    self.holidays.append({'date':datetime.date(year, 1, 1),'name':'Nyårsdagen'})
    self.holidays.append({'date':self.easter,'name':'Påskdagen'})
    self.holidays.append({'date':datetime.date(year, 5, 1),'name':'Första Maj'})
    self.holidays.append({'date':self.midsummer,'name':'Midsommardagen'})
    self.holidays.append({'date':datetime.date(year, 12, 25),'name':'Juldagen'})
    self.holidays.append({'date':datetime.date(year, 6, 6),'name':'Nationaldagen'})

    self.flagdays=self.holidays.copy() # Copy common days 

    # Only holidays
    self.holidays.append({'date':datetime.date(year, 1,6), 'name':'Trettondagen'})
    self.holidays.append({'date':self.easter - datetime.timedelta(days=2), 'name':'Långfredagen'})
    self.holidays.append({'date':self.easter + datetime.timedelta(days=1), 'name':'Annandag påsk'}),
    self.holidays.append({'date':self.easter + datetime.timedelta(days=(5*7+4)), 'name':'Kristi himmelsfärdsdag'})
    self.holidays.append({'date':self.allhelgon, 'name':'Alla helgons dag'})
    self.holidays.append({'date':datetime.date(year, 12, 26), 'name':'Annandag jul'})
#   self.holidays.append({'date':self.easter datetime.timedelta(days=(7*7+1)), 'name':'Annandag pingst'}) #Removed 2005. could check year, but why?

    self.flagdays.append({'date':datetime.date(year, 1,28), 'name':'Konungens namnsdag'})
    self.flagdays.append({'date':datetime.date(year, 3,12), 'name':'Kronprinsessans namnsdag'})
    self.flagdays.append({'date':datetime.date(year, 4,30), 'name':'Konungens födelsedag'})
    self.flagdays.append({'date':datetime.date(year, 7,14), 'name':'Kronprinsessans födelsedag'})
    self.flagdays.append({'date':datetime.date(year, 8,8), 'name':'Drottningens namnsdag'})
    self.flagdays.append({'date':datetime.date(year, 10,24), 'name':'FN-dagen'})
    self.flagdays.append({'date':datetime.date(year, 11,6), 'name':'Gustav Adolfsdagen'})
    self.flagdays.append({'date':datetime.date(year, 12,10), 'name':'Nobeldagen'})
    self.flagdays.append({'date':datetime.date(year, 12,23), 'name':'Drottningens Födelsedag'})
    if (self.valdagen):
      self.flagdays.append({'date':self.valdagen, 'name':'Valdagen'})


    print(self.holidays)
    print(self.flagdays)

  def isHoliday(self, date=None):
    if date==None:
      date=datetime.date.today()
    else:
      date=date.date()

    if (self.year!=date.year):
      self.initYear(date.year)
    print(date)
    return next((item for item in self.holidays if item["date"] == date), None)

  def isFlagday(self, date=None):
    if date==None:
      date=datetime.date.today()
    else:
      date=date.date()
    
    if (self.year!=date.year):
      self.initYear(date.year)

    print(date)
    return next((item for item in self.flagdays if item["date"] == date), None)

if __name__ == '__main__':

  today = datetime.date.today()
  year = today.year

  flagga=flaggdag(year)
  print ("Flaggdag")

  for x in range(2022, 2031):
    flagga.initYear(x)
 
  print(flagga.isHoliday(datetime.datetime(year=2022, month=12, day=25)))
  print(flagga.isFlagday(datetime.datetime.now()))
  print(flagga.isFlagday())
