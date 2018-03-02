from django.shortcuts import render,redirect
from hashlib import sha1
from  ds_user.models import User,Address
from django.http import  HttpResponseRedirect,JsonResponse
from ds_goods.models import GoodInfo
from  ds_user.user_decorator import login
from ds_user import user_decorator

def login(request):
    uname=request.COOKIES.get('uname','')
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,'pwd':pwd,'error':0}
    try:
        url=request.META['HTTP_REFERER']
        if '/user/Regist' in url:raise Exception()
    except:url='/'
    response=render(request,'ds_user/登录.html',context)
    response.set_cookie('url',url)
    return response
def Regist(request):
    return render(request,'ds_user/注册.html')
def login_handle(request):
    post=request.POST
    uname=post.get('username')
    pwd=post.get('pwd','')
    remember=post.get('remember','0')
    s=sha1()
    s.update(pwd.encode('utf8'))
    upwd=s.hexdigest()
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first()
    print(user)
    if user:
        url=request.COOKIES.get('url','/')
        print(url)
        red=HttpResponseRedirect(url)
        if remember=='1':
            red.set_cookie('uname',uname.encode('utf-8'))
            red.set_cookie('upwd',pwd)
        else:
            red.set_cookie('uname','',max_age=-1)
            red.set_cookie('upwd', '', max_age=-1)
        request.session['username']=uname
        request.session['uid']=user.id
        return red
    else:
        context={'error':1,'uname':uname}
        return render(request, 'ds_user/登录.html', context)
def register_handle(request):
    post = request.POST
    uname = post.get('username')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    uemail = post.get('email','')

    if pwd != cpwd:
        return redirect('/user/regist')
    s1 = sha1()
    s1.update(pwd.encode('utf8'))
    pwd = s1.hexdigest()
    user = User()
    user.uname = uname
    user.upwd = pwd
    user.uemil = uemail
    user.save()
    print(user.uname)
    return redirect('/user/login')
def logout(request):
    request.session.flush()
    return redirect('/')


@user_decorator.login
def shdz(request):
  adds=Address.objects.filter(uid=request.session.get('uid',''),scbz=0)
  return render(request,'ds_user/管理收货地址.html',locals())

def register_exist(request):
    uname=request.GET.get('un')
    count=User.objects.filter(uname=uname).count()

    return JsonResponse({'count':count})
@user_decorator.login
def user_center_info(request):
    username=request.session.get('username','')
    user=User.objects.filter(uname=username).first()
    goodids=request.COOKIES.get('goodids','')
    goods_list = []
    if goodids!='':
        goodid1=goodids.split(',')

        for i in goodid1:
            goods_list.append(GoodInfo.object.filter(pk=i).first())
            pass
    # context={'title':'用户中心','username':username}
    return render(request,'ds_user/个人资料.html',locals())
def userupdate(request):
    post = request.POST
    uid = request.session.get('uid', '')
    user = User.objects.filter(id=uid).first()
    user.uname=post.get('un','')
    user.uphone = post.get('uphone', '')
    user.uemil = post.get('uemil', '')
    user.usex = post.get('usex','')
    user.save()
    request.session['username']=user.uname
    return redirect('/')


@user_decorator.login
def add_save(request):
  post = request.POST
  aid=post.get('aid')
  print(aid)
  if aid:
        Address.objects.filter(id=aid).update(reciver=post.get('reciver'),sheng = post.get('sheng'),
        shi = post.get('shi'),qu = post.get('qu'),yzbm = post.get('yzbm'),
        detialaddr=post.get('detialaddr'),rphone = post.get('rphone'))
  else:Address.objects.create(reciver=post.get('reciver'),sheng = post.get('sheng'),
        shi = post.get('shi'),qu = post.get('qu'),yzbm = post.get('yzbm'),
        detialaddr=post.get('detialaddr'),rphone = post.get('rphone'),uid=request.session['uid'])
  return redirect('/user/shdz')



@user_decorator.login
def mrdz(request):
  dzid = request.GET.get('dzid')
  Address.objects.all().update(mrdz=0)
  Address.objects.filter(id=dzid).update(mrdz=1)
  return redirect('/user/shdz')

@user_decorator.login
def scdz(request):
  dzid = request.GET.get('dzid')
  Address.objects.filter(id=dzid).update(scbz=1)
  return redirect('/user/shdz')

@user_decorator.login
def bjdz(request):
  dzid = request.GET.get('dzid')
  add=Address.objects.get(id=dzid)
  adds = Address.objects.filter(uid=request.session.get('uid', ''), scbz=0)
  return render(request, 'ds_user/管理收货地址.html', locals())










