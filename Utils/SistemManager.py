from Plugin.DentalNotifier import DentalNotifierPlugin
from Utils.DataBaseManager import Appointment

class SistemManager:
    def __init__(self, database):
        self.database = database
        self.dentalNotifier = DentalNotifierPlugin()

    def mainMenu(self):
        print(
            "\n\t***MENU PRINCIPAL***\n\nSeleccione una opción:"
            + "\n\t1) Agendar Cita\n\t2) Salir"
        )
        return input()

    def scheduleAppointment(self):
        dentistId = self.dentistsMenu()
        dentist = self.database.getDentist(dentistId)
        patientId = self.patientsMenu(dentist)
        patient = dentist.getPatient(patientId)
        date = self.pickDate()
        print('\nHORA DE INICIO')
        startTime = self.pickTime()
        print('\nHORA DE FIN')
        endTime = self.pickTime()

        appointment = Appointment(0, dentist.getCalendarId(), dentist, patient, date, startTime, endTime)

        summary = 'Cita dentista'
        description = 'Cita del paciente ' + patient.getName()

        self.dentalNotifier.createEvent(date[2], date[1], date[0], startTime[0], startTime[1], endTime[0],
            endTime[1], summary, description, patient.getName(), patient.getEmail(), dentist.getCalendarId())
        
        if (startTime[0] < 10):
            hour = '0' + str(startTime[0])
        else:
            hour = str(startTime[0])
        
        if (startTime[1] < 10):
            minutes = '0' + str(startTime[1])
        else:
            minutes = str(startTime[1])
        
        message = 'Su cita quedó agendada para la fecha ' + str(date[0]) + '/' + str(date[1]) + ' a las ' + hour + ':' + minutes + '.\nDentalTime le desea un buen día'
        self.dentalNotifier.sendWhatsappMsg(patient.getCellPhone(), message)

        print('Cita agendada')

    def dentistsMenu(self):
        dentists = self.database.getDentists()

        opc = 0
        while(opc <= 0 or opc > len(dentists)):
            print("\nSeleccione el/la dentista:")
            for d in dentists:
                print("\t" + str(d.id) + ") " + d.name)
            opc = int(input())

        return opc

    def patientsMenu(self, dentist):
        patients = dentist.getPatients()

        opc = 0
        while(opc <= 0 or opc > len(patients)):
            print("\nSeleccione el paciente:")
            for p in dentist.getPatients():
                print("\t" + str(p.id) + ") " + p.name)
            opc = int(input())

        return opc

    def pickDate(self):
        opc = 0
        while(opc <= 0 or opc > 31):
            print("\nIngrese el día (entre 1 y 31):")
            opc = int(input())

        date = [opc]

        opc = 0
        while(opc <= 0 or opc > 12):
            print("\nIngrese el mes (entre 1 y 12):")
            opc = int(input())
            
        date.append(opc)
            
        date.append(2021)

        return date

    def pickTime(self):
        opc = 0
        while(opc < 6 or opc > 21):
            print("\nIngrese la hora (entre 6 y 21 hrs): ")
            opc = int(input())
        
        time = [opc]

        if (opc < 10):
            hour = '0' + str(opc) + ':'
        else:
            hour = str(opc) + ':'

        opc = 0
        while(True):
            print("\nSeleccione la hora exacta:\n\t1) " + hour + "00\n\t2) " + hour +
                "15\n\t3) " + hour + "30\n\t4) " + hour + "45")
            opc = input()
            if opc == "1":
                time.append(0)
                break
            elif opc == "2":
                time.append(15)
                break
            elif opc == "3":
                time.append(30)
                break
            elif opc == "4":
                time.append(45)
                break
            else:
                "\n\tSelección inválida\n"
        
        return time
