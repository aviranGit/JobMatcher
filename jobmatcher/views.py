from django.shortcuts import render
from jobmatcher.models import Job, Candidate
from django.db.models import Q


def homePage(request):
    return render(request, 'home_page.html')

'''
"getCandidates" function called when client execute "candidate search" - The flow is to filter candidate with full and partial title.
Then, count matching skills and sort the candidates with more matching skills. The results returns to the client as html page.
'''
def getCandidates(request):
    job_id = request.GET.get('job_id') #get the job ID from the form input ("home_page.html")
    
    #Initialize list for counting skills matchs for each candidate
    candidate_skills_count = []

    #Wrapping the job search in try/except to detect if the job id is not exist in DB
    try:
        job = Job.objects.get(id = job_id) # get the job from db by job_id
    except Job.DoesNotExist:
        job = None

    if(job == None): #the job_id doen not exist in DB
        return render(request, 'results_format.html', {'job_not_exist': True})
    #keep the job skills query set
    job_skills_queryset = job.skills.all()

    #Store job skills names in list
    job_skills_names = [skill.name for skill in job_skills_queryset] 

    #This filtering combines "full title match" and "partial title match"(BONUS) -using Q with OR operator to optimize the performance.
    title_match_candidates = Candidate.objects.filter(Q(title = job.title)|Q(title__istartswith = job.title.split(' ')[0]))

    #The second cosideration is "as many skills as possible"
    for candidate in title_match_candidates:
        candidate_skills_set = candidate.skills.all()
        #Store the skills name as well to present in result report
        candidate_skills_set_names = [skill.name for skill in candidate_skills_set]

        #list of matching skills with given job. Using .contains to reduce the runtime over skills QuerySet. 
        candidate_match_skills = [skill for skill in candidate_skills_set if job_skills_queryset.contains(skill)]

        #Append the candidate count of skills matching with the candidate object and skills set.
        candidate_skills_count.append((len(candidate_match_skills), candidate, candidate_skills_set_names))
        
    best_candidates = sorted(candidate_skills_count, key= lambda c: c[0], reverse= True)[:20]
    #cut the list and keep only tuple of (candidate, skills set)
    best_candidates = [(candidate[1], candidate[2]) for candidate in best_candidates]

    #Rendering the "results_format.html" page which organize the best_candidate elements 
    return render(request, 'results_format.html',{'given_job': job, 'job_skills':job_skills_names,
                    'candidate_list': best_candidates})
