Hi:) 

This simple app porpuse is to help you to find the best candidates for a given job.
Each job and candidate has title and skills set.

App Structure- 
- There are three models:
  - Skill (attribute: name) 
  - Candidate (attributes: title, skills(ManyToMany))
  - Job (attributes: title, skills(ManyToMany))
- The endpoint that search for best candidates is 'matcher/bestCandidates/' - which can be reach after clicking the "Search" button at home page. 

Installing The App-

1. Clone the repository. run "git clone https://github.com/aviranGit/JobMatcher.git"
2. Create your own virtual environment 
  2.1 Run "python3 -n venv venv"
  2.2 Run "source venv/bin/activate
3. Install app requirements - run "pip install -r requirements.txt"
4. Create MySQL database. 
5. Create .env file in "matcher" folder and copy the following structure and fill the variables:

DATABASE_NAME= ##YOUR DATABASE NAME##
DATABASE_USER=##YOUR USERNAME##
DATABASE_PASSWORD=##YOUR PASSWORD##

(I didn't put the secret key in .env file to let you run the app quickly - hope it's fine๐)
7.  run the following scripts:
  3.1 "python manage.py makemigrations"
  3.2 "python manage.py migrate"
  3.3 "python manage.py runserver"
9.The server will be running on http://127.0.0.1:8000/ (localhost port 8000)


Play With The App:

1. Open the link in your browser http://127.0.0.1:8000/.
2. In the "Welcome" page, insert Job ID - number in the range of 1 to #NUMBER_OF_JOBS_IN_DB 
3. Click "Search" 
4. You will navigate to the result page. 
5. Click "New Search" to re-search candidates for another job.

If you have any question or issues running the app, I would like to guide ๐

(BTW, It's my first Django project)


A little bit screenshots โบ๏ธ๐

<img width="569" alt="image" src="https://user-images.githubusercontent.com/62885985/170815785-afdafaae-c8b6-40a7-b521-1e7097e1ed8f.png">


<img width="443" alt="image" src="https://user-images.githubusercontent.com/62885985/170815795-4ee39583-e300-4a78-8173-2b296e77bb7a.png">

