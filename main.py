class PhoneContact(object):
    name ='ds'
    contactNumber = 792179219721
    note='ddw'
    def __init__(self, name, conractNumber, note):
        self.name = name
        self.note = note
        self.contactNumber = conractNumber


    def getContactByName(self):
        a = input()
        if a == 'ds':
            print("имя {}, номер {}, запись {}".format(self.name, self.contactNumber,self.note))

    def new_contact(self):
        name_n, phone, note_n = input()
        name_n = PhoneContact
        phone = PhoneContact
        note_n = PhoneContact


class PhoneBook(object):
    contactNumber = []
    def __init__(self, contactNumber):
        self.contactNumber = contactNumber

