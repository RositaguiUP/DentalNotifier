from twilio.rest import Client
from Plugin.Google import Create_Service, convert_to_RFC_datetime

class DentalNotifierPlugin:
    def __init__(self):
        CLIENT_SECRET_FILE = 'Plugin/client_secret.json'
        API_NAME = 'calendar'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/calendar']
        
        self.service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        ACCOUNT_SID = "AC164881fcc313e206c3d3fe72056d1ffb"
        AUTH_TOKEN  = "164e3842924649cc7cdc1367072dd66e"

        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def createEvent(self, year, month, day, startHour, startMinutes, endHour, endMinutes,
        summary, description, patientName, patientEmail, calendarId):
        print(
            "\n\t***MENU PRINCIPAL***\n\nSeleccione una opción:"
            + "\n\t1) Agendar Cita\n\t2) Salir"
        )

        hour_adjustment = 5
        event_request_body = {
            'start': {
                'dateTime': convert_to_RFC_datetime(year, month, day, startHour + hour_adjustment, startMinutes),
                'timeZone': 'America/Mexico_City'
            },
            'end': {
                'dateTime': convert_to_RFC_datetime(year, month, day, endHour + hour_adjustment, endMinutes),
                'timeZone': 'America/Mexico_City'
            },
            'summary': summary,
            'description': description,
            'colorId': 7,
            'status': 'confirmed',
            'transparency': 'opaque',
            'visibility': 'private',
            "attendees": [
                {
                "email": patientEmail,
                "displayName": patientName,
                "organizer": False,
                },
            ],
        }

        response = self.service.events().insert(
            calendarId = calendarId,
            sendNotifications = True,
            sendUpdates = 'all',
            body = event_request_body
        ).execute()

        return(response)
    
    def sendWhatsappMsg(self, number, message):
        from_whatsapp_number='whatsapp:+14155238886'
        to_whatsapp_number='whatsapp:+521' + number

        self.client.messages.create(body=message, from_=from_whatsapp_number, to=to_whatsapp_number)
