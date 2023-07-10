# CollegeNotificationSystem

Problem Statement
We want to design a notification system for colleges. Requirements are as follows


API endpoints to manage teachers with following details

uuid (unique identifier)

first name

middle name (optional)

last name

mobile

email

API endpoints to manage students with following details

uuid

first name

middle name (optional)

last name

Teacher_uuids (list of teachers they want to get notifications from. This is the uuid of the teacher from the previous endpoint)

Role based access control (Authorisation)

Only users with role admin can manage teachers.

Users with role manager can manage students but only view teachers.

Users with role teacher can send email to students in their pod

Users with role student can only view their details and teacher details.

API to send email.

This source code should be uploaded to a personal project in your Github account. 

Clean coding practices should be followed.
