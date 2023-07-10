# CollegeNotificationSystem

## Problem Statement
We want to design a notification system for colleges. Requirements are as follows

API endpoints to manage teachers with following details

iid (unique identifier)

name

email

API endpoints to manage students with following details

id

Name

email

Teacher_uuids (list of teachers they want to get notifications from. This is the uuid of the teacher from the previous endpoint)

Role based access control (Authorisation)

Only users with the role ‘admin’ can manage teachers.

Users with the role ‘manager’ can manage students but only view teachers.

Users with role ‘teacher’ can send email to students in their pod

Users with role ‘student’ can only view their details and teacher details.

API to send email.

This source code should be uploaded to a personal project in your Github account.

Clean coding practices should be followed.

## Undertaken Method

Figure 1
We create a centralised User table which handles the login credentials as per the role of the user. The user role can be of four types namely the admin, manager, teacher, student. The admin and manager user are pre registered in the db.

The user has the ability to manage teachers, whereas a manager can manage students, hence the two users can create entries in the user table by adding credentials for teacher and student table along with it respectively.

According to the requirements, the relationship between students and teachers is one:many.

To normalise this information instead of having multiple rows in teachers and students tables, a ‘connection’ table is created to store the relevant information of students and their corresponding teachers they want to receive notification from.

The description of the tables is given in Figure 1. The ‘connection’ table will help us to retrieve the ids of teachers which the student with a particular id has chosen to receive notifications from

Also it will enable us to retrieve the ids of the students through which we can fetch the emails from the students table, to enable a particular teacher to send mails to students. 

User access and Database control:

Figure 2
For the Database we will use Sqlite or PostgreSQL.

According to the requirements there are 4 types of users namely the Admin, Manager, Teachers and Students.

Here is description of the roles and accesses of each user:

Admin: An Admin can make POST requests to the ‘teachers’ table implying an admin has access to manage teachers with operations such as Create, Update and Delete. No other users can access the teachers table to make such changes.

Manager: A manager has access to manage students through operations like Create, Update and Delete, therefore this user is able to make POST requests to alter with the data in the students table. This is also an exclusive access.

Teacher: A Teacher has the ability to check all the students who have chosen to receive notifications from the active teacher user. This allows the teacher to only make GET requests to fetch information from the students table alongside this Teacher will be able to make requests to a Mail API in order to send mails to the students.

Student: A Student has the access to view the teachers and his details, moreover he can choose which teacher he wants to receive notifications from, this enables him to make POST requests to make changes in the connection tables, which will reflect to the teacher user when he views the students enrolled to receive notification from him/her.

 ## Tech Requirements
In order to achieve the following objectives we need a bunch of packages which are listed below:

 

Python

VS Code

Postgres

Pgadmin

Flask

Flask-Login

Flask-Migrate

Flask-SQLAlchemy

psycopg2

pytest

pytest-cov

requests

SQLAlchemy

Werkzeug-security

## API routes
The several Api Calls are dependent upon the role of the user

The only routes available to all the users are:

/login: POST request to login route with email and password fields required in body, upon successful execution user is logged in. A session is created by the flask login manager.

/logout: GET request to logout route can be made, if a user is logged in, it would be logged out and the session would be terminated internally through flask login manager.

Other routes are user specific and are listed below:

Admin

/register/teacher: POST request to this url creates a user with role teacher, the body must specify the email, password and name of the registered entity. A corresponding entry in the teacher table is created.

/students/students: GET request to this route returns the list of all the students currently registered.

/teachers/teachers: GET request to this route returns a list of all the teachers currently registered.

Manager

/register/students: POST request to this url creates a user with role student, the body must specify the email, password and name of the registered entity. A corresponding entry in the student table is created.

/students/students: GET request to this route returns the list of all the students currently registered.

/teachers/teachers: GET request to this route returns a list of all the teachers currently registered.

Teacher

/teachers/teachers: GET request to this route returns a list of all the teachers currently registered.

/teachers/teachers/students: GET request to this route returns a list of students enrolled under the currently logged in teacher.

teachers/sendmail: teacher user can make POST requests to this route passing the email, password, subject, message in the body of the gmail account to login to a smtp server and send a mail to the email ids of students enrolled under the teacher.

Student

/students/students: GET request to this route returns the list of all the students currently registered.

students/enroll: POST request to this route creates an entry in the connection table of the current student id with the ‘teacher_id’ that is passed through the body.
