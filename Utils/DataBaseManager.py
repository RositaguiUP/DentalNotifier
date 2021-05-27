class DentalTimeDB:
    def __init__(self):
        self.dentists = []
    
    def addDentist(self, dentist):
        self.dentists.append(dentist)
    
    def getDentist(self, id):
        return self.dentists[id-1]
    
    def getDentists(self):
        return self.dentists

class Dentist:
    def __init__(self, id, name, email, cellPhone):
        self.id = id
        self.name = name
        self.email = email
        self.cellPhone = cellPhone
        self.patients = []
        self.calendarId = ''

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getCellPhone(self):
        return self.cellPhone
    
    def addPatient(self, patient):
        self.patients.append(patient)

    def getPatient(self, id):
        return self.patients[id-1]
    
    def getPatients(self):
        return self.patients
    
    def getCalendarId(self):
        return self.calendarId
    
    def setCalendarId(self, calendarId):
        self.calendarId = calendarId

class Patient:
    def __init__(self, id, name, email, cellPhone):
        self.id = id
        self.name = name
        self.email = email
        self.cellPhone = cellPhone

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getCellPhone(self):
        return self.cellPhone

class Appointment:
    def __init__(self, id, idCalendar, dentist, patient, date, startTime, endTime):
        self.id = id
        self.idCalendar = idCalendar
        self.dentist = dentist
        self.patient = patient
        self.date = date
        self.startTime = startTime
        self.endTime = endTime

    def getId(self):
        return self.id

    def getIdCalendar(self):
        return self.idCalendar

    def getDentist(self):
        return self.dentist

    def getPatient(self):
        return self.patient

    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date
    
    def getStartTime(self):
        return self.startTime
    
    def setStartTime(self, startTime):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime
    
    def setEndTime(self, endTime):
        self.endTime = endTime
