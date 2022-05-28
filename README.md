Hi:) 

This simple app porpuse is to help you to find the best candidates for a given job.
Each job and candidate has title and skills set.

Getting Started:
Requirments-
- Pyton 
- MySQL 

App Structure- 
- The app name in the project is "jobmatcher"
- There are three models:
  - Skill (attribute: name) 
  - Candidate (attributes: title, skills(ManyToMany))
  - Job (attributes: title, skills(ManyToMany))
- The endpoint that search for best candidates is 'matcher/bestCandidates/' - which can be reach after clicking the "Search" button at home page.

Installing The App-

1. Clone the repository.
2. Install mysqlclient using - "pip install mysqlclient"
3. In matcher/setting.py - set your DB detail (NAME, USER, PASSWORD) and save the file.
4. run the following scripts:
  3.1 "python manage.py makemigrations"
  3.2 "python manage.py migrate"
  3.3 "python manage.py runserver"
5.The server will be running on http://127.0.0.1:8000/ (localhost port 8000)

*I asked about the DB data and I didn't get answer yet, so I assume that you will be able to insert your data to check the app.

Play With The App:

1. Open the link in your browser http://127.0.0.1:8000/.
2. In the "Welcome" page, insert Job ID - number in the range of 1 to #NUMBER_OF_JOBS_IN_DB 
3. Click "Search" 
4. You will navigate to the result page. 
5. Click "New Search" to re-search candidates for another job.

Enjoy:)

A little bit screenshots ☺️

<img width="569" alt="image" src="https://user-images.githubusercontent.com/62885985/170815785-afdafaae-c8b6-40a7-b521-1e7097e1ed8f.png">


<img width="443" alt="image" src="https://user-images.githubusercontent.com/62885985/170815795-4ee39583-e300-4a78-8173-2b296e77bb7a.png">

