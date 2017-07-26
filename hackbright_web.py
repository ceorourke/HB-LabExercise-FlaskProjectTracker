"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    records = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           records=records)
    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template('student_search.html')


@app.route("/student-creation")
def student_creation_display():
    """Shows the form that lets you add a new student."""

    return render_template('make_student.html')


@app.route('/student-add', methods=['POST'])
def student_add():
    """Returns a student added to database"""

    github = request.form.get('github')
    first = request.form.get('first_name')
    last = request.form.get('last_name')

    hackbright.make_new_student(first, last, github)

    return render_template('new_student_added.html',
                           github=github,
                           first=first,
                           last=last)


@app.route('/project')
def project_listing():
    """Displays details of a project"""

    project_title, description, max_grade = request.args.get('title')
    print request.args.get('title')
    return render_template('project_description.html',
                           project_title=project_title,
                           description=description,
                           max_grade=max_grade)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
