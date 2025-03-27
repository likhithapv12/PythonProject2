from flask import Flask , jsonify

todo = Flask(__name__)

students=[
    {
        "id":1,
        "name":"yesh",
        "age":20
    },
    {
        "id": 2,
        "name": "yeshan",
        "age": 25
    },
    {
        "id": 3,
        "name": "yeshwanth",
        "age": 10
    }
    ]
@todo.route('/student-list')
def get_students_list():
    return jsonify(students)

@todo.route('/students/get/<int:id>')
def get_student_list(id):
    print(id)
    for std in students:
     if std['id'] == id:
       return jsonify(std)
    print(std)




if __name__ == '__main__':
    todo.run(


        debug=True
    )