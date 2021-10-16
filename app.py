from flask import Flask, request, render_template, session
from flask_session import Session

app= Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

class User:
    def __init__(self, username, password, email):
        self.username= username
        self.password= password
        self.email= email
    def __str__(self):
        return f"{self.username} {self.password} {self.email}"
    def save(self):
        dataUsers= open("data/users.txt", "a")
        dataUsers.write('\n'+self.username+'\n'+self.password+'\n'+self.email)
        dataUsers.close()

Users=[]

@app.route("/")
def beggin():
    return render_template("login.html", message="Debe iniciar sesión o registrarse.")

@app.route("/login")
def login():
    return render_template("login.html", message="Debe iniciar sesión o registrarse.")

@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        session.pop("userInSession", None)
        username= request.form.get("username")
        password= request.form.get("password")
        email= request.form.get("email")
        print(email)
        if email!=None: #Si se envía el formulario de registro de cuenta
            Users.append(User(username, password, email))
            saveUsers()
            return render_template("login.html", message="Registro concluido con éxito, puede iniciar sesión.")
            
        else: #Si se envía el formulario de inicio de sesión
            for i in Users:
                if username == i.username and password == i.password:
                    session["userInSession"]= username
                    return render_template("index.html")
            return render_template("login.html", message="Los datos ingresados son incorrectos, por favor ingrese un nombre de usuario y contraseña válidos.")
    else:
        return render_template("login.html", message="Debe iniciar sesión o registrarse.")
    
    
@app.route("/fieldForm", methods=['POST'])
def fieldForm():
    session["noContact"] = int(request.form.get("noContact"))
    session["noProgram"] = int(request.form.get("noProgram"))
    session["noLanguage"] = int(request.form.get("noLanguage"))
    session["noWorks"] = int(request.form.get("noWorks"))
    session["noEducation"] = int(request.form.get("noEducation"))
    return render_template("fieldForm.html", noTrabajo=session["noWorks"], noContacto= session["noContact"], noPrograma=session["noProgram"], noIdioma=session["noLanguage"], noEducacion=session["noEducation"])

@app.route("/generated", methods=['POST'])
def generated():
    name= request.form.get("completName")
    workOcuped= request.form.get("workOcuped")
    presentacion=request.form.get("presentation")
    noContact=session.get("noContact", None)
    noProgram=session.get("noProgram", None)
    noLanguage=session.get("noLanguage", None)
    noWorks=session.get("noWorks", None)
    noEducation=session.get("noEducation", None)
    listContact=[] 
    listProgram=[]
    listLanguage=[]
    listWorks=[]
    listEducation=[]
    listTmp=[]
    for i in range(noContact):
        listTmp.append(request.form.get(f"contact{i}"))
        listTmp.append(request.form.get(f"url{i}"))
        listContact.append(listTmp)
        listTmp=[]
    for i in range(noLanguage):
        listTmp.append(request.form.get(f"language{i}"))
        listTmp.append(request.form.get(f"levelLang{i}"))
        listLanguage.append(listTmp)
        listTmp=[]
    for i in range(noProgram):
        listTmp.append(request.form.get(f"program{i}"))
        listTmp.append(request.form.get(f"levelProg{i}"))
        listProgram.append(listTmp)
        listTmp=[]
    for i in range(noWorks):
        listTmp.append(request.form.get(f"dirWork{i}"))
        listTmp.append(request.form.get(f"startWork{i}"))
        listTmp.append(request.form.get(f"endWork{i}"))
        listTmp.append(request.form.get(f"nameCompany{i}"))
        listTmp.append(request.form.get(f"nameWork{i}"))
        listTmp.append(request.form.get(f"review{i}"))
        listWorks.append(listTmp)
        listTmp=[]
    for i in range(noEducation):
        listTmp.append(request.form.get(f"dirStudy{i}"))
        listTmp.append(request.form.get(f"startStudy{i}"))
        listTmp.append(request.form.get(f"endStudy{i}"))
        listTmp.append(request.form.get(f"academicDegree{i}"))
        listTmp.append(request.form.get(f"instName{i}"))
        listEducation.append(listTmp)
        listTmp=[]
    return render_template("generated.html", presentacion=presentacion, nombres=name, puesto=workOcuped, listContact= listContact, listEducation=listEducation, listLanguage= listLanguage, listWorks= listWorks, listProgram= listProgram)

def loadUsers():
    value=0
    username=""
    password=""
    email="" 
    dataUsers= open("data/users.txt", "r")
    value= dataUsers.readline()
    for i in range(int(value)):
        username= dataUsers.readline()
        password= dataUsers.readline()
        email= dataUsers.readline()
        username= username.replace('\n','')
        password= password.replace('\n','')
        email= email.replace('\n','')
        Users.append(User(username, password, email))
    dataUsers.close()

def saveUsers():
    dataUsers= open("data/users.txt", "w")
    dataUsers.write(str(len(Users)))
    dataUsers.close()
    dataUsers= open("data/users.txt", "a")
    for i in Users:
        i.save()
    dataUsers.close()
    #Users.clear()

if __name__=="__main__":
    loadUsers()
    app.run(debug=True)