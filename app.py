from flask import Flask, render_template, request, session
from flask_session import Session

app= Flask("__name__")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/login")
def login():
    return render_template("index.html")

@app.route("/index", methods=["POST"])
def index():
    message=""
    username= request.form.get("username")
    password= request.form.get("password")
    if (password=="2505" and username=="fredyNeira"):
        return render_template("index.html")
    else:
        message="Los datos ingresados son erróneos, inténtelo de nuevo"
        return render_template("login.html", message=message)


@app.route("/fieldsForm", methods=["POST"])
def fieldsForm():
  session["noContact"] = int(request.form.get("noContact"))
  session["noProgram"] = int(request.form.get("noProgram"))
  session["noLanguage"] = int(request.form.get("noLanguage"))
  session["noWorks"] = int(request.form.get("noWorks"))
  session["noEducation"] = int(request.form.get("noEducation"))
  return render_template("fieldsForm.html", noTrabajo=session["noWorks"], noContacto= session["noContact"], noPrograma=session["noProgram"], noIdioma=session["noLanguage"], noEducacion=session["noEducation"])

@app.route("/generated", methods=["POST"])
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



if __name__=="__main__":
    app.run(debug=True)
