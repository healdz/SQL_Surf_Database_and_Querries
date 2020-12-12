import numpy as np
import random
import string
from collections import defaultdict
uppers = list(string.ascii_uppercase)
lowers = list(string.ascii_lowercase)

# create the Client Data
numClients = 10001
outfile = open("tempClients.csv","w")
#nationalityList = ['USA','Eng','Mex','Fra','Cad','Spa','Bra','Aus','NZ','Ger','Nor']
languageList = ['English','English','English','English','English','English','English','English','English','Spanish','Spanish','Spanish','Spanish','French','Finnish','German',]
healthBool = ['No','No','No','No','No','No','No','No','No','No','Yes','Yes','Yes']
skillLevels = list(range(11))
groupSize = list(range(7))
clientIDList = []
for i in range(1,numClients):
    outString = ''
    clID = str(i)
    clientIDList.append(clID)
    outString += clID
    outString += ','
    firstNameLength = random.choice(range(3,7))
    lastNameLength = random.choice(range(5,8))
    nameList = [random.choice(uppers), ''.join(random.choices(lowers,k=firstNameLength)),' ', random.choice(uppers), ''.join(random.choices(lowers,k=lastNameLength))]
    name = ''.join(nameList)
    outString += name
    outString += ','
    age = str(np.random.randint(80))
    outString += age  # age
    outString += ','
    lang = random.choice(languageList)
    outString += lang
    outString += ','
    health = random.choice(healthBool)
    outString += health
    outString += ','
    outString += str(random.choice(skillLevels))
    outString += ','
    firstLesson = random.choice(healthBool)
    outString += firstLesson
    outString += ','
    outString += str(random.choice(groupSize)) #groupsize
    outString += "\n"
    outfile.write(outString)
outfile.close()


# create the Lessons Data
numLessons = 100
outfile = open("tempLessons.csv","w")
capacityList = list(range(16))
diffList = list(range(11))
boolList = ['No','No','No','No','Yes','Yes']
lessonsIDList = []
for i in range(1,numLessons):
    outString = ''
    lessID = str(i)
    lessonsIDList.append(lessID)
    outString += lessID
    outString += ','
    capacity = str(random.choice(capacityList))
    outString += capacity
    outString += ','
    difficulty = str(random.choice(diffList))
    outString += difficulty
    outString += ','
    outString += random.choice(boolList)
    outString += "\n"
    outfile.write(outString)
outfile.close()

#Create the SurfShop data
numBus = 200
ratingList = list(range(11))
employCountList = list(range(51))
lessCapcList = list(range(16))
loc =list(range(16))
outfile = open("tempSurfShop.csv","w")
businessIDList = []
for i in range(1,numBus):
    outString = ''
    busID = str(i)
    businessIDList.append(busID)
    outString += busID
    outString += ','
    nameLength = random.choice(range(9))
    nameList = [random.choice(uppers), ''.join(random.choices(lowers,k=nameLength))]
    name = ''.join(nameList)
    outString += name
    outString += ','
    locLength = random.choice(range(16))
    locList = [random.choice(uppers), ''.join(random.choices(lowers,k=locLength))]
    location = ''.join(locList)
    outString += location
    outString += ','
    rating = str(random.choice(ratingList))
    outString += rating
    outString += ','
    employeeCount = str(random.choice(employCountList))
    outString += employeeCount
    outString += ','
    lessCapacity = str(random.choice(lessCapcList))
    outString += lessCapacity
    outString += ','
    outString += random.choice(boolList) #rentals
    outString += "\n"
    outfile.write(outString)
outfile.close()

#create Instructor Data
numInstructors = 2000
outfile = open("tempInstructors.csv","w")
#nationalityList = ['USA','Eng','Mex','Fra','Cad','Spa','Bra','Aus','NZ','Ger','Nor']
languageList = ['English','English','English','English','English','English','English','English','English','Spanish','Spanish','Spanish','Spanish','French','Finnish','German',]
privBool = ['No','Yes','Yes','Yes','Yes']
ratingList = list(range(11))
groupSize = list(range(7))
yrsTeachingList = list(range(41))
instructorIDList = []
instructorNameList=[]
for i in range(1,numInstructors):
    outString = ''
    instrID = str(i)
    instructorIDList.append(instrID)
    outString += instrID
    outString += ','
    firstNameLength = random.choice(range(3,7))
    lastNameLength = random.choice(range(5,8))
    nameList = [random.choice(uppers), ''.join(random.choices(lowers,k=firstNameLength)),' ', random.choice(uppers), ''.join(random.choices(lowers,k=lastNameLength))]
    name = ''.join(nameList)
    outString += name
    instructorNameList.append(name)
    outString += ','
    age = str(np.random.randint(60))
    outString += age  # age
    outString += ','
    lang = random.choice(languageList)
    outString += lang
    outString += ','
    outString += str(random.choice(ratingList))
    outString += ','
    private = random.choice(privBool)
    outString += private
    outString += ','
    yrsTeaching = str(random.choice(yrsTeachingList))
    outString += yrsTeaching
    outString += ','
    locLength = random.choice(range(16))
    locList = [random.choice(uppers), ''.join(random.choices(lowers,k=locLength))]
    location = ''.join(locList)
    outString+=location
    outString += ','
    month = str(random.choice(range(1,13)))
    day = str(random.choice(range(1,31)))
    year = str(random.choice(range(1980,2020)))
    hireDate = month + '/'+day +'/'+year
    outString += hireDate
    outString += "\n"
    outfile.write(outString)
outfile.close()


#create supplier data
numSup = 1001
productCountList = list(range(11))
employCountList = list(range(201))
outfile = open("tempSupplier.csv","w")
supplierIDList = []
for i in range(1,numSup):
    outString = ''
    supID = str(i)
    supplierIDList.append(supID)
    outString += supID
    outString += ','
    locLength = random.choice(range(16))
    locList = [random.choice(uppers), ''.join(random.choices(lowers,k=locLength))]
    location = ''.join(locList)
    outString += location
    outString += ','
    products = str(random.choice(productCountList))
    outString += products
    outString += ','
    employeeCount = str(random.choice(employCountList))
    outString += employeeCount
    outString += "\n"
    outfile.write(outString)
outfile.close()


#create supplies relation data
numSupplies = 2000
costList = list(range(10001))
timeList = list(range(21))
outfile = open("relationSupplies.csv","w")
for i in range(numSupplies):
    outString = ''
    supID = str(random.choice(supplierIDList))
    outString += supID
    outString += ','
    busID = str(random.choice(businessIDList))
    outString += busID
    outString += ','
    cost = str(random.choice(costList))
    outString += '$' + cost
    outString += ','
    prodLength = random.choice(range(16))
    prodList = [random.choice(uppers), ''.join(random.choices(lowers,k=prodLength))]
    productType = ''.join(prodList)
    outString += productType
    outString += ','
    time = str(random.choice(timeList))
    outString += time + '' + 'days'
    outString += ','
    month = str(random.choice(range(1,13)))
    day = str(random.choice(range(1,31)))
    year = str(random.choice(range(1980,2020)))
    shipDate = month + '/'+day +'/'+year
    outString += shipDate
    outString += "\n"
    outfile.write(outString)
outfile.close()

#create schedules data
numSchedules = 10000
outfile = open("relationSchedule.csv","w")
for i in range(numSchedules):
    outString = ''
    lessID = str(random.choice(lessonsIDList))
    outString += lessID
    outString += ','
    busID = str(random.choice(businessIDList))
    outString += busID
    outString += ','
    month = str(random.choice(range(1,13)))
    day = str(random.choice(range(1,31)))
    year = str(random.choice(range(2020,2022)))
    schedDate = month + '/'+day +'/'+year
    outString += str(schedDate)
    outString += "\n"
    outfile.write(outString)
outfile.close()

#create employs relation data
numEmploys = 2500
wageList = list(range(10,100))
hoursList = list(range(5,51))
contractorBool = ['Yes','No','No','No','No','No']
outfile = open("relationEmploys.csv","w")
for i in range(numEmploys):
    outString = ''
    employeeID = str(random.choice(instructorIDList))
    outString += employeeID
    outString += ','
    busID = str(random.choice(businessIDList))
    outString += busID
    outString += ','
    wage = str(random.choice(wageList))
    outString += wage +'/'+'hour'
    outString += ','
    hours = str(random.choice(hoursList))
    outString += hours
    outString += ','
    contractor = random.choice(contractorBool)
    outString += contractor
    outString += "\n"
    outfile.write(outString)
outfile.close()

#create teaches database
#need to get rid of language key in the database ----
numTeaches = 2000
durationList = list(range(8))
sizeList = list(range(16))
outfile = open("relationTeaches.csv","w")
for i in range(numTeaches):
    outString = ''
    instrID = str(random.choice(instructorIDList))
    outString += instrID
    outString += ','
    lessID = str(random.choice(lessonsIDList))
    outString += busID
    outString += ','
    durr = str(random.choice(durationList))
    outString += durr
    outString += ','
    size = str(random.choice(sizeList))
    outString += size
    outString += "\n"
    outfile.write(outString)
outfile.close()

#xreate surfsWith data
numsurfswith = 20000
waveSizeList = list(range(10))
injuriesBool = ['Yes','No','No','No','No','No','No','No','No','No','No','No','No','No','No','No']
tipList = list(range(35))
weatherList = ['Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Rain','Rain','Rain','Cloudy','Cloudy','Cloudy','Cloudy','Windy','Windy','Lightning']
outfile = open("relationSurfsWith.csv","w")
for i in range(numsurfswith):
    outString = ''
    instrID = str(random.choice(instructorIDList))
    outString += instrID
    outString += ','
    clientID = str(random.choice(clientIDList))
    outString += clientID
    outString += ','
    wSize = str(random.choice(waveSizeList))
    outString += wSize
    outString += ','
    injur = str(random.choice(injuriesBool))
    outString += injur
    outString += ','
    weather = random.choice(weatherList)
    outString += weather
    outString += ','
    tip = str(random.choice(tipList))
    outString += tip + '%'
    outString += "\n"
    outfile.write(outString)
outfile.close()

#create reserves relation data
numReserves = 15000
paymentTypeList = ['Credit Card','Credit Card','Credit Card','Cash','Cash','Cash','Cash','Check','Bank Transfer']
instructorRequestBool = ['No','No','No','No','Yes','Yes']
priceList = list(range(50,500))
outfile = open("relationReserves.csv","w")
for i in range(numReserves):
    outString = ''
    lessID = str(random.choice(lessonsIDList))
    outString += lessID
    outString += ','
    clientID = str(random.choice(clientIDList))
    outString += clientID
    outString += ','
    paymentType = random.choice(paymentTypeList)
    outString += paymentType
    outString += ','
    insRequest = random.choice(instructorRequestBool)
    if insRequest == 'Yes':
        insRequest = random.choice(instructorNameList)
    outString += insRequest
    outString += ','
    month = str(random.choice(range(1,13)))
    day = str(random.choice(range(1,31)))
    year = str(random.choice(range(2020,2022)))
    resDate = month+day+year
    outString += str(resDate)
    outString += ','
    price = str(random.choice(priceList))
    outString += price
    outString += "\n"
    outfile.write(outString)
outfile.close()
