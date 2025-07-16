import matplotlib
matplotlib.use('Agg') # This line is necessary to use matplotlib in a Flask application without a display server.
from flask import Flask ,redirect,render_template,request
 
import matplotlib.pyplot as plt

app=Flask(__name__)
@app.route('/', methods =["GET" ,"POST"])
def details():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        type = request.form["ID"]
        id = request.form["id_value"]
        if id =="":
            return render_template('wrong.html')
        id=int(id)
        data = []
        with open('data.csv' ,'r') as file:
            file.readline()
            if type == 'student_id':
                for row in file:
                    row = list(map(int,row.strip().split(',')))
                    if row[0] == id:
                        data.append(row)
            elif type == "course_id":
                for row in file:
                    row = list(map(int,row.strip().split(',')))
                    if row[1] == id:
                        data.append(row)  
        
        if len(data)==0:
            return render_template("wrong.html")
        
        elif type == 'student_id':
            total_mark = 0
            for x in data:
                total_mark +=x[2]
            print(total_mark)
            print(data)
            return render_template('student.html',data=data,total_marks=total_mark)
        elif type == 'course_id':
            total_marks = 0
            max_marks = 0 
            marks =[]
            i =0
            for x in data:
                total_marks +=x[2]
                i+=1
                marks.append(x[2])
                if x[2]> max_marks:
                    max_marks = x[2]
            avg_marks = total_marks/i 
            plt.hist(marks)
            plt.ylabel('Freaquency')
            plt.savefig('static/plot.png')
            plt.close()
            return render_template('course.html',total_marks=total_marks,avg_marks=avg_marks , max_marks = max_marks, img='static/plot.png')
        

          





app.debug = True
app.run()


    