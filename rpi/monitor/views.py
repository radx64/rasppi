from django.shortcuts import render
from monitor.models import Temperature
from datetime import datetime, timedelta

CHART_TYPES = {
	'0': "3 godziny",
	'1': '24 godziny',
	'2': '3 dni'
}

def index(request, chart_interval='0'):
	title = "Wykres temperatury z ostatnich %s" % CHART_TYPES[chart_interval]
	
	if chart_interval not in CHART_TYPES.keys():
		chart_interval = '0'

	if chart_interval == '0':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(hours=3)))
	elif chart_interval == '1':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(days=1)))
	elif chart_interval == '2':
		temperature_list = Temperature.objects.filter(date__gte=(datetime.today()-timedelta(days=3)))
	else:
		temperature_list = []

	return render(request, 'index.html', {
		'title': title,
		'chart_types': sorted(CHART_TYPES.iteritems()),
		'chart_interval': chart_interval,
		'temperature_list': temperature_list,
	})






#    info = request.session.get('info', None)
#    if info:
#        del request.session['info']
    
#    pending_users = []
#    pending_id = Task.objects.filter(status__lt=100).values("user_id").distinct()[:10]
#    for p in pending_id:
#        pending_users.append(User.objects.get(id=p['user_id']).username)

#    biggest = []
#    big_id = Task.objects.values('user').annotate(Count('user')).order_by('-user__count')[:10]
#    for b in big_id:
#        big_tmp = {}
#        big_tmp['number'] = b['user__count']
#        big_tmp['username'] = User.objects.get(id=b['user']).username
#        biggest.append(big_tmp)

#    longest = []
#    long_id = Task.objects.filter(status=100).order_by('-time').values('user', 'time')[:10]
#    for l in long_id:
#        long_tmp = {}
#        long_tmp['time'] = l['time']
#        long_tmp['username'] = User.objects.get(id=l['user']).username
#        longest.append(long_tmp)
    
#
#    last_registered = User.objects.all().order_by('-date_joined').values('username')[:10]

#    return render(request, 'index.html', {
#                                         'info': info,
#                                         'pending_users': pending_users,
#                                         'biggest': biggest,
#                                         'longest': longest,
#                                         'last_registered': last_registered,
#                                         })

##
#def register(request):
#    info = request.session.get('info', None)
#    if info:
#        del request.session['info']
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            new_user = form.save()
#            username = form.cleaned_data['username']
#            password = form.cleaned_data['password2']
#            user = auth.authenticate(username=username, password=password)
#            auth.login(request, user)
#            request.session['info'] = 'register_success' 
#            redirect = '/profile/%s/' % username
#            return HttpResponseRedirect(redirect)
#        else:
#            return render(
#                request, 
#                "register.html", {
#                    'form': form, 
#                    'info': 'register_error',
#            })
#    else:
#        form = UserCreationForm()
#    return render(
#        request, 
#        "register.html", {
#            'form': form, 
#            'info': info,
#    })
#
#
#def login_form(request):
#    redir = ""
#    if 'next' in request.GET and request.GET['next']:
#        redir = request.GET['next']
#    return render(request, "login.html", {'next': redir,})
#
#
#def login(request):
#    username = request.POST.get('username', '')
#    password = request.POST.get('password', '')
#    user = auth.authenticate(username=username, password=password)
#    if user is not None:
#        auth.login(request, user)
#        request.session['info'] = 'login_success'
#        return HttpResponseRedirect("/tasks/")
#    else:
#        return render(request, "login.html", 
#                     {'info': 'login_error'})
#
#
#@login_required
#def profile(request, username):
#    info = request.session.get('info', None)
#    if info:
#        del request.session['info']
#
#    try:
#        user = User.objects.get(username=username)
#    except User.DoesNotExist:
#        request.session['info'] = 'profile_error'
#        return HttpResponseRedirect('/index/')
#    else:
#        return render(request, "profile.html", 
#                               {'profile': user,
#                                'info': info,
#                               })
#
#
#@login_required
#def profile_edit(request):
#    info = request.session.get('info', None)
#    if info:
#        del request.session['info']
#
#    p = User.objects.get(username=request.user)
#
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = auth.authenticate(username=username, password=password)
#        if user is not None:
#            p.first_name = request.POST['first_name']
#            p.last_name = request.POST['last_name']
#            p.email = request.POST['email']
#            p.save()
#            request.session['info'] = 'profile_edit_success'
#            redirect = "/profile/%s/" % username
#            return HttpResponseRedirect(redirect)
#        else:
#            return render(request, 
#                          "profile_edit.html", 
#                          {
#                           'profile': p,
#                           'info': 'profile_edit_error',
#                          })
#
#    return render(request, 
#                  "profile_edit.html", 
#                  {
#                   'profile': p, 
#                  })
#
#
#def logout(request):
#    auth.logout(request)
#    request.session['info'] = 'logout_success'
#    return HttpResponseRedirect('/index/')
#
#
#@login_required
#def tasks(request):
#    info = request.session.get('info', None)
#    if info:
#        del request.session['info']
#
#    user_id = User.objects.get(username=request.user).id
#    tasks = Task.objects.filter(user_id=user_id).order_by("-id").values()
#    return render(request, "tasks.html", {
#                                          'tasks': tasks,
#                                          'info': info,
#                                         })
#
#
#def task_table(request):
#    user_id = User.objects.get(username=request.user).id
#    tasks = Task.objects.filter(user_id=user_id).order_by("-id").values()
#    return render(request, "task_table.html", {'tasks': tasks})
#
#
#@login_required
#def new_task(request):
#    if request.method == 'POST':
#        user_id = User.objects.get(username=request.user).id
#        partition = request.POST['partition']
#        ffile = request.FILES['ffile']
#        new_task = Task(user_id=user_id, partition=partition, ffile=ffile, status=0)
#        new_task.save()
#
#        mpitask_output = os.popen("mpitask")
#        if 'running' not in mpitask_output.read():
#            os.popen("lamboot -v /media/sshfs/OMPI/hostfile")
#            subprocess.Popen("/media/sshfs/OMPI/raytracer/Manager")
#
#        request.session['info'] = 'new_task_success'
#        return HttpResponseRedirect("/tasks/")
#    else:
#        return render(request, "new_task.html", {})
#
#
