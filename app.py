from flask import Flask,render_template,request,url_for,redirect
app=Flask(__name__)

Student_list = [{"Name": "Mahalakshmi", "Age": 24, "Roll_NO": 101, "Marks": [90, 75, 80, 98, 75]},

                {"Name": "Nijanthan", "Age": 23, "Roll_NO": 102, "Marks": [90, 75, 80, 98, 65]},

                {"Name": "Selva", "Age": 22, "Roll_NO": 103, "Marks": [90, 75, 80, 78, 99]},

                {"Name": "Preethi", "Age": 22, "Roll_NO": 104, "Marks": [94, 75, 80, 88, 35]},

                {"Name": "Ajay", "Age": 23, "Roll_NO": 105, "Marks": [70, 85, 80, 98, 35]},

                {"Name": "Anand", "Age": 26, "Roll_NO": 106, "Marks": [90, 75, 85, 98, 35]},

                {"Name": "Pavitran", "Age": 21, "Roll_NO": 107, "Marks": [80, 98, 35, 90, 75]},

                {"Name": "Kumar", "Age": 25, "Roll_NO": 108, "Marks": [90, 80, 98, 35, 75]},

                {"Name": "Saranya", "Age": 26, "Roll_NO": 109, "Marks": [75, 80, 90, 98, 35]},

                {"Name": "Jeffin", "Age": 22, "Roll_NO": 110, "Marks": [98, 35, 90, 75, 80]}]

@app.route("/",methods=["POST","GET"])
def func():
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        Roll_NO=request.form.get("Roll_NO")
        Mark1=request.form.get("Mark1")
        Mark2=request.form.get("Mark2")
        Mark3=request.form.get("Mark3")
        Mark4=request.form.get("Mark4")
        Mark5=request.form.get("Mark5")
        Marks=[]
        Marks.append(Mark1)
        Marks.append(Mark2)
        Marks.append(Mark3)
        Marks.append(Mark4)
        Marks.append(Mark5)

        dict1={}
        dict1.update({"Name":Name})
        dict1.update({"Age":Age})
        dict1.update({"Roll_NO":Roll_NO})
        dict1.update({"Marks":Marks})
        
        Student_list.append(dict1)
        
    return render_template("home.html",list1=Student_list)


@app.route("/<string:a>")
def delete(a):
    Student_list.pop(int(a)-1)
    return render_template("home.html",list1=Student_list)

@app.route("/edit/<string:index>",methods=["POST","GET"])
def edit(index):
    if request.method=="POST":
        Name=request.form.get("Name")
        Age=request.form.get("Age")
        Roll_NO=request.form.get("Roll_NO")
        Mark1=request.form.get("Mark1")
        Mark2=request.form.get("Mark2")
        Mark3=request.form.get("Mark3")
        Mark4=request.form.get("Mark4")
        Mark5=request.form.get("Mark5")
        Marks=[]
        Marks.append(Mark1)
        Marks.append(Mark2)
        Marks.append(Mark3)
        Marks.append(Mark4)
        Marks.append(Mark5)

        student_l=Student_list[int(index)-1]
        student_l.update({"Name":Name})
        student_l.update({"Age":Age})
        student_l.update({"Roll_NO":Roll_NO})
        student_l.update({"Marks":Marks})
        return redirect(url_for('func'))
    edit_student_list=Student_list[int(index)-1]
    return render_template("edit.html",student=edit_student_list)

if __name__=="__main__":
    app.run(debug=True)