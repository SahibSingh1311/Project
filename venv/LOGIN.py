import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from tkinter import *

class Patient:

    def __init__(self, PatientName, Email, Password, Phone, Height, Weight):
        self.PatientName = PatientName
        self.Email = Email
        self.Password = Password
        self.Phone = Phone
        self.Height = Height
        self.Weight = Weight

def SavePatient():
    print("button Clicked")
    cRef = Patient(None, None, None, None, None, None)
    cRef.PatientName = entryPatientName.get()
    cRef.Email = entryEmail.get()
    cRef.Password = entryPassword.get()
    cRef.Phone = entryPhone.get()
    cRef.Height = entryHeight.get()
    cRef.Weight = entryWeight.get()
    cred = credentials.Certificate("Key.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    data = cRef.__dict__
    db.collection("patient").document().set(data)
    print(">> ",cRef.PatientName, "Saved")

def SignUp():
    window2 = Tk()

    lblTitle = Label(window2, text="Add Patient Details")
    lblTitle.pack()

    lblPatientName = Label(window2, text="Enter Patient Name")
    lblPatientName.pack()

    entryPatientName = Entry(window2)
    entryPatientName.pack()

    lblPhone = Label(window2, text="Enter Phone")
    lblPhone.pack()

    entryPhone = Entry(window2)
    entryPhone.pack()

    lblEmail = Label(window2, text="Enter Email")
    lblEmail.pack()

    entryEmail = Entry(window2)
    entryEmail.pack()

    lblPassword = Label(window2, text="Enter Password")
    lblPassword.pack()

    entryPassword = Entry(window2)
    entryPassword.pack()

    lblHeight = Label(window2, text="Enter Height")
    lblHeight.pack()

    entryHeight = Entry(window2)
    entryHeight.pack()

    lblWeight = Label(window2, text="Enter Weight")
    lblWeight.pack()

    entryWeight = Entry(window2)
    entryWeight.pack()

    btnSavePatient = Button(window2, text="Add Patient", command=SavePatient)
    btnSavePatient.pack()

    window2.mainloop()


# def Login():
#     window3 = Tk()
#
#     lblEmail = Label(window3, text="Enter Email")
#     lblEmail.pack()
#
#     entryEmail = Entry(window3)
#     entryEmail.pack()
#
#     lblPassword = Label(window3, text="Enter Password")
#     lblPassword.pack()
#
#     entryPassword = Entry(window3)
#     entryPassword.pack()
#
#     btnLogin = Button(window3, text="Login")
#     btnLogin.pack()
#     window3.mainloop()
window1=Tk()
var=IntVar()
lblTitle = Label(window1, text="Do You Have An Account?")
lblTitle.pack()
R1= Radiobutton(window1, text="Yes", variable=var, value=1,command=Login)
R1.pack()
R2= Radiobutton(window1, text="No", variable=var, value=0,command=SignUp)
R2.pack()
window1.mainloop()



