from flask import Flask,request,jsonify

app = Flask(__name__)

students=[]
next_user_id=1

@app.route('/register_students',methods=['Post'])
def register_students():
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']
    global next_user_id
    student={
            'user_id':next_user_id,
            'username':username,
            'password':password,
            'email':email
        }
    students.append(student)
    next_user_id+=1
    return jsonify({"message":"student register successfull"}),200
@app.route("/get_all_students", methods=['GET'])
def get_all_students():
        return jsonify(students)

@app.route("/update_students/<int:userid>",methods=['put'])
def update_student(userid):
    username=request.json['username']
    password=request.json['password']
    email=request.json['email']
    global students
    for student in students:
        if student['user_id']==userid:
            student['username']=username
            student['password']=password
            student['email']=email
        return jsonify({"message":"students update successfull"}),200
    return jsonify({"error":"student not found"})
@app.route("/delete_students/<int:userid>",methods=['delete'])
def delete_student(userid):
    global students
    intil_student=len(students)
    students=[s for s in students if s['user_id']!=userid]
    if len(students)< intil_student:
         return({"message":"students deleted successfull"}),200
    else:
         return({"error":"student not found"})
if __name__=="__main__":
     app.run(debug=True)

        



    
    