# Need to clean up this import list. I am sure I have a few old things in here.
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.utils import timezone

from allaccess.models import AccountAccess

from snet.forms import UploadFileForm
from snet.models import User_Bio
from snet.models import Wall
from snet.models import User
from snet.models import Post
from snet.models import Pics
from snet.models import Sub_Post

from allaccess.views import OAuthRedirect
from allaccess.views import OAuthCallback


class AdditionalPermissionsRedirect(OAuthRedirect):

    def get_additional_parameters(self, provider):
        if provider.name == 'facebook':
            # Request permission to see user's email
            return {'scope': ['email']}

class AssociateCallback(OAuthCallback):

    def get_or_create_user(self, provider, access, info):
        new = User.create.objects.create(
            first_name=info.get('first_name'),
            last_name=info.get('last_name'),
            gender=info.get('gender'),
            age=0
            )
        # age is unrelaiable from facebook...
        # https://developers.facebook.com/docs/graph-api/reference/v2.2/user
        return new
        #return super(AssociateCallback, self).get_or_create_user(provider, access, info)


# Facebook Login.
def facelogin(request):
    username = ''
    if request.user.is_authenticated():
        username = request.user.username
        ub = User_Bio.objects.filter(name=username)
        if ub:
            #k = All
            #print(request.user.accountaccess_set.first().scope)
            return redirect('/snet/%s/wall' % username)

        # If Facebook is not accociated with an account.
        elif not ub:
            un = User.objects.get(username=username)
            flog = AccountAccess.objects.get(user=un)
            context = {'flog': flog, 'user': un}
            return render(request, 'snet/face_reg.html', context)
    else:
        return render(request, 'snet/base_login.html')

# Register a new facvebook account to an existing user.
def faceregister(request, f_id, old_usern):
    if request.POST.get('blogin'):
        lname = request.POST.get('tname')
        lpass = request.POST.get('ppass')
        log = authenticate(username=lname, password=lpass)

        # This is a work around way to associate the user with the 
        # facebook id. There are better ways that involve overloading functions
        # but I could not get them to work correctly. Rob gave me the idea to 
        # do things this way.
        if log is not None:
            login(request,log)
            ub = get_object_or_404(User_Bio, name=lname)
            us = get_object_or_404(User, username=lname)
            old_us = get_object_or_404(User,username=old_usern)
            ub.facebook_id = f_id
            flog = AccountAccess.objects.get(user=old_us)
            flog.user = us
            ub.save()
            flog.save()
            # old_us should be deleted at this point. It is only a dummy
            # record.
            return redirect('/snet/%s/wall' % lname)
        else:  # LOGIN FAILED
            return render(request, 'snet/base_login.html')  # placeholder
    else:
        return render(request, 'snet/base_login.html')  # placeholder


# Social Network views
@csrf_protect
def userlogin(request):
    print("in userlogin")

    # Standard Register
    if request.method == 'POST':
        if request.POST.get('bregister'): #REGISTER
            return render(request,'snet/register.html')

        #Standard Login
        elif request.POST.get('blogin'):
            lname = request.POST.get('tname')
            lpass = request.POST.get('ppass')
            log = authenticate(username=lname, password=lpass)
            if log is not None:
                login(request,log)
                u = get_object_or_404(User_Bio, name=lname)
                return redirect('/snet/%s/wall' % lname)
            else: #LOGIN FAILED
                return render(request, 'snet/base_login.html')

        # Facebook Login
        elif request.POST.get('bface'):
            return redirect('/accounts/login/facebook')

        #REGISTER        
        elif request.POST.get('bnewuser'):
            # Get user input
            username = request.POST.get('uname')
            p1 = request.POST.get('pass')
            p2 = request.POST.get('pass2')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            age = request.POST.get('age')
            gen = request.POST.get('sex')

            #check requred fields
            if(username is None or p1 is None or p1 != p2 or
                   int(age) < 0 or gen.upper() not in 'MF'):
                #add some error msg if they make a mistake
                return render(request,'snet/register.html')
            else:
                #Populate database records in database
                # Probibly need some protection against unique fields
                u = User.objects.create_user(username=username, password=p1, 
                                             first_name=fname, last_name=lname)
                u.save()
                ub = User_Bio(name=username, gender=gen, age=age, 
                              date_join = datetime.now(), register=u)
                u.save()
                ub.save()
                w = Wall(user=ub)
                w.save()
                p = Post(wall=w, poster=ub, status='Account Created',
                         pub_date=datetime.now())
                p.save()

                photo = Pics(user=ub, is_profile_pic=True)
                photo.save()

                log = authenticate(username=username, password=p1)
                login(request,log)

                print('account created ', username)
                return redirect('/snet/%s/wall' % ub)
    else:
        return render(request, 'snet/base_login.html')


# login required
@login_required()
def index(request):
    recent_users = User_Bio.objects.order_by('-name') #try except?
    context = {'recent_users': recent_users}
    return render(request, 'snet/index.html', context)

# search for users
@login_required()
def search_index(request, user_name, search_str):
    # if the user searches for * or other non alpha characters then 
    # a 404 is returned. Look this up.
    search_result = User_Bio.objects.all().filter(name__icontains=search_str)
    if search_result:
        userb = get_object_or_404(User_Bio, name=user_name)
        context = {'recent_users': search_result, 'userb': userb}
        return render(request, 'snet/sindex.html', context)
    else:
        return redirect('/snet/%s/wall' % user_name)

#profile page
# This may be redundent with alt_profile. 
# I should merge profile into alt_profile
@login_required()
def profile(request, user_name):
    # Looking at this now, I think I couldhave added all the User_Bio info 
    # into User and eliminated User_Bio
    if request.user.username == user_name:
        userp = request.user
        userb = userp.user_bio_set.all()[0]
    else:
        userp = get_object_or_404(User, username=user_name)
        userb = userp.user_bio_set.filter(name=user_name)[0]
    wal = userb.wall_set.all()[0]
    posts = wal.post_set.all()
    subpost = wal.sub_post_set.all()
    pro_pic = userb.pics_set.filter(is_profile_pic=True)[0]
    context = {'userb': userb, 'postsa':posts,'userp': userp, 
               'pro_pic': pro_pic, 'subpost':subpost}
    if request.method == 'POST':
        print(request.POST)
        
        # Wall post
        if request.POST.get('bwall') or request.POST.get('postWall'):
            new_status = request.POST.get('postWall')
            if new_status: #Check for empty string
                update = Post(poster=request.user.user_bio_set.all()[0], 
                              wall=wal, status=new_status,
                              pub_date=timezone.now())
                update.save()
                posts = wal.post_set.all()
                context['postsa'] = posts
            return render(request, 'snet/profile.html', context)

        # Logout button.    
        elif request.POST.get('blogout'): #LOGOUT
            logout(request)
            return redirect('%s' % settings.LOGIN_URL)

        # Edit Profile info
        elif request.POST.get('bedit'):
            return render(request, 'snet/update_profile.html', context)

        #Get all the updated profile info
        elif request.POST.get('buserupdate'):
            userb.age = request.POST.get('age')
            userb.gender = request.POST.get('sex')
            userp.first_name = request.POST.get('fname')
            userp.last_name = request.POST.get('lname')
            userp.save()
            userb.save()
            context['userb'] = userb
            context['userp'] = userp

        # Look at photos
        elif request.POST.get('bpic'):
            return redirect('/snet/%s/list/' % userb)

        # Search for new Users
        elif request.POST.get('bsearch') or request.POST.get('searchbar'):
            search_str = request.POST.get('searchbar')
            if search_str:
                return redirect('/snet/%s/search/%s' % (userb, search_str))
    # Get
    return render(request, 'snet/profile.html', context)

# I just borrowed what this guy did. uploads photos
# REF: https://docs.djangoproject.com/en/1.7/topics/http/file-uploads/
@login_required()
def upload_file(request, user_name):
    userb = get_object_or_404(User_Bio, name=user_name)
    if request.method == 'POST':

        # Upload photo
        if request.POST.get('bupload'):
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Pics(photo=request.FILES['docfile'],user=userb)
                newdoc.save()
                return redirect('/snet/%s/list' % userb)

        # Go back to profiel
        elif request.POST.get('bback'):
            return redirect('/snet/%s/wall' % userb)
    else:
        form = Pics()
    documents = Pics.objects.filter(user=userb)
    context = {'documents': documents,'form': form, 'userb': userb}
    return render(request, 'snet/list.html', context)

# Allows users to slect a photo from their list of uploaded photos.
# The for loop is in here to deal with a bug that I had when I first
# created this. Now it should work with get_object instead of get_list.
# I have not tested this yet, but it could make this a lot faster.
@login_required()
def photo_update(request, user_name, photo_id):
    userb = get_object_or_404(User_Bio, name=user_name)
    photo = get_object_or_404(Pics, user=userb, pk=photo_id)
    old = get_list_or_404(Pics, user=userb) #optimise this...
    for i in old:
        i.is_profile_pic = False
        i.save()
    photo.is_profile_pic = True
    photo.save()
    return redirect('/snet/%s/wall' % userb)

# I made this special to handle updatine a subpost. I was woried that
# associating the subpost and the main post would take a lot of code, but 
# it worked out well. 
# This was made to work with both your own profiel and an alternate profile.
# Look here for tips on merging alt_profile and profile views.
@login_required()
def subpost(request, user_name, post_pk, box_id):
    #print(request.user.user_bio_set.all()[0])
    user_log = request.user.user_bio_set.all()[0]
    if request.user.username == user_name:
        userb = user_log
    else:
        userb = get_object_or_404(User_Bio, name=user_name)
    #usera = get_object_or_404(User_Bio, name=altername_name)
    wal = userb.wall_set.all()[0]
    #wal = get_object_or_404(Wall, user=usera)
    #post = get_object_or_404(Post, pk=post_pk)
    post = wal.post_set.filter(pk=post_pk)[0]
    update = request.POST.get('tsubpost' + str(post_pk))
    if update:
        subp = Sub_Post(wall=wal, parent_post=post, poster=user_log, 
                        status=update, pub_date=timezone.now())
        subp.save()
    return redirect('/snet/%s/wall' % user_name)