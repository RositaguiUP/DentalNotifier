from Utils.DataBaseManager import DentalTimeDB, Dentist, Patient
from Utils.SistemManager import SistemManager

paciente1 = Patient(1, "Jorge Preciado Mendoza", "rositaguipla@gmail.com", "3322527151")
paciente2 = Patient(2, "Mayan Santos Toscano", "mayansantos70153@gmail.com", "3322882570")
paciente3 = Patient(3, "Lizbeth Aguirre Plascencia", "liz.agui.pla@gmail.com", "3321707140")
paciente4 = Patient(4, "Luis Manuel Ramírez Ávalos", "lmra.99990@gmail.com", "3310111261")
paciente5 = Patient(5, "Enrique Luna García", "quiquelunag@gmail.com", "3312816565")

dentista1 = Dentist(1, "Rosita Aguirre Plascencia", "0225352@up.edu.mx", "3322527151")
dentista1.addPatient(paciente1)
dentista1.addPatient(paciente2)
dentista1.addPatient(paciente3)
dentista1.addPatient(paciente4)
dentista1.addPatient(paciente5)
dentista1.setCalendarId('c_h83t2c7516h7ml22k1bipa6buo@group.calendar.google.com')

database = DentalTimeDB()
database.addDentist(dentista1)

sisMan = SistemManager(database)

while True:
    opc = sisMan.mainMenu()
    if opc == "1":
        sisMan.scheduleAppointment()
    elif opc == "2":
        print("\nSaliendo del programa...")
        break
    else:
        print["\nOpción inválida"]