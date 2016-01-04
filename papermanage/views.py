# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import * 
from django.template import Context
from models import Paper,User,Pbpaper


class UserForm(forms.Form):
    File = forms.FileField()
    
def index(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    c=Context({"a":a})
    return render_to_response("index.html",c)

def reference(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    paper_list=Paper.objects.all()
    c=Context({"paper_list":paper_list})
    return render_to_response("reference.html",c,d)
    
def publish(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        paper_list=Pbpaper.objects.all()
        c=Context({"paper_list":paper_list})
        return render_to_response("publish.html",c,d)
        
def search(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    DouB=request.GET['searchname']
    DouA=request.GET['select']
    if DouA=="Title":
        paper_list=Paper.objects.filter(Title__contains=DouB)
    if DouA=="Author":
        paper_list=Paper.objects.filter(Author__contains=DouB)
    if DouA=="Keyword":
        paper_list=Paper.objects.filter(Keyword__contains=DouB)
    if DouA=="Publisher":
        paper_list=Paper.objects.filter(Publisher__contains=DouB)
    if DouA=="Publishdate":
        paper_list=Paper.objects.filter(PublishDate=DouB)
    c=Context({"paper_list":paper_list})
    return render_to_response("reference.html",c,d)

def searchclass(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    DouB=request.GET['grade']
    paper_list=Paper.objects.filter(Grade3=DouB)
    c=Context({"paper_list":paper_list})
    return render_to_response("reference.html",c,d)

def pbsearch(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        DouB=request.GET['searchname']
        DouA=request.GET['select']
        if DouA=="Title":
            paper_list=Pbpaper.objects.filter(Title__contains=DouB)
        if DouA=="Author":
            l1=Pbpaper.objects.filter(Author1__contains=DouB)
            l2=Pbpaper.objects.filter(Author2__contains=DouB)
            l3=Pbpaper.objects.filter(Author3__contains=DouB)
            l4=Pbpaper.objects.filter(Author4__contains=DouB)
            paper_list=list(set(l1).union(set(l2)).union(set(l3)).union(set(l4)))
        if DouA=="Keyword":
            paper_list=Pbpaper.objects.filter(Keyword__contains=DouB)
        if DouA=="Publisher":
            paper_list=Pbpaper.objects.filter(Publisher__contains=DouB)
        if DouA=="Publishdate":
            paper_list=Pbpaper.objects.filter(PublishDate=DouB)
        c=Context({"paper_list":paper_list})
        return render_to_response("publish.html",c,d)

def pbsearchclass(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        DouB=request.GET['grade']
        paper_list=Pbpaper.objects.filter(Grade3=DouB)
        c=Context({"paper_list":paper_list})
        return render_to_response("publish.html",c,d)

def add(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    if request.POST:
        post=request.POST
        form = UserForm(request.POST,request.FILES)
        new_paper=Paper()
        new_paper.PaperID=post["PaperID"]
        new_paper.Title=post["Title"]
        new_paper.Author=post["Author"]
        new_paper.Keyword=post["Keyword"]
        new_paper.Publisher=post["Publisher"]
        new_paper.PublishDate=post["Publishdate"]
        new_paper.Summary=post["Summary"]
        new_paper.Grade1=post["grade1"]
        new_paper.Grade2=post["grade2"]
        new_paper.Grade3=post["grade3"]
        new_paper.save()
        if form.is_valid():
            File=form.cleaned_data['File']
            File.name=new_paper.PaperID+".doc"

            from os import environ  
            online = environ.get("APP_NAME", "")   
           
            if online:  
                import sae.const  
                access_key = sae.const.ACCESS_KEY  
                secret_key = sae.const.SECRET_KEY  
                appname = sae.const.APP_NAME  
                domain_name = "cunchu"
                
                import sae.storage  
                s = sae.storage.Client()  
                ob = sae.storage.Object(File.read())  
                url = s.put(domain_name, File.name, ob)  
                
            new_paper.address="http://papermanage-cunchu.stor.sinaapp.com/"+str(File.name)
            new_paper.save()
            return HttpResponseRedirect('/reference/') 
    else:
        form = UserForm()
    return render_to_response('add.html', {'form': form}, d)
    
def pbadd(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        if request.POST:
            post=request.POST
            form = UserForm(request.POST,request.FILES)
            new_paper=Pbpaper()
            new_paper.PaperID=post["PaperID"]
            new_paper.Title=post["Title"]
            new_paper.Author1=post["Author1"]
            new_paper.Author2=post["Author2"]
            new_paper.Author3=post["Author3"]
            new_paper.Author4=post["Author4"]
            new_paper.Keyword=post["Keyword"]
            new_paper.Publisher=post["Publisher"]
            new_paper.PublishDate=post["Publishdate"]
            new_paper.Summary=post["Summary"]
            new_paper.Grade1=post["grade1"]
            new_paper.Grade2=post["grade2"]
            new_paper.Grade3=post["grade3"]
            new_paper.Score=int(post["score"])
            if form.is_valid():
                File=form.cleaned_data['File']
                File.name=new_paper.PaperID+".doc"
    
                from os import environ  
                online = environ.get("APP_NAME", "")   
               
                if online:  
                    import sae.const  
                    access_key = sae.const.ACCESS_KEY  
                    secret_key = sae.const.SECRET_KEY  
                    appname = sae.const.APP_NAME  
                    domain_name = "cunchu"
                    
                    import sae.storage  
                    s = sae.storage.Client()  
                    ob = sae.storage.Object(File.read())  
                    url = s.put(domain_name, File.name, ob)  
                    
                new_paper.address="http://papermanage-cunchu.stor.sinaapp.com/"+str(File.name)
                new_paper.save()
                return HttpResponseRedirect('/publish/')  
        else:
            form = UserForm()
        return render_to_response('pbadd.html', {'form': form}, d)

def more(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    more_id =request.GET["id"]
    paper=Paper.objects.get(PaperID=more_id)
    c = Context({"paper":paper}) 
    return render_to_response("information.html",c,d)  

def delete(request):
    paperid = request.GET["id"]
    Paper.objects.get(PaperID=paperid).delete()
    return HttpResponseRedirect("/reference/")

def modify(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    paperid = request.GET["id"]
    old = Paper.objects.get(PaperID=paperid)
    if request.POST:
        post = request.POST
        old.Title=post['Title']
        old.Author=post['Author']
        old.Keyword=post['Keyword']
        old.Publisher=post['Publisher']
        old.PublishDate=post['Publishdate']
        old.Summary=post['Summary']
        old.Grade1=post['grade1']
        old.Grade2=post['grade2']
        old.Grade3=post['grade3']
        old.save()
        return HttpResponseRedirect('/reference/')
    c=Context({"paper":old})
    return render_to_response("modify.html",c,d)

def pbmore(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        more_id =request.GET["id"]
        paper=Pbpaper.objects.get(PaperID=more_id)
        if paper.Author1==a or paper.Author2==a or paper.Author3==a or paper.Author4==a:
            fg = 1;
        else:
            fg = 0;
        c = Context({"paper":paper}) 
        d = Context({"a":[a, fg]})
        return render_to_response("pbinformation.html",c,d)  

def pbdelete(request):
    paperid = request.GET["id"]
    Pbpaper.objects.get(PaperID=paperid).delete()
    return HttpResponseRedirect("/publish/")

def pbmodify(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        paperid = request.GET["id"]
        old = Pbpaper.objects.get(PaperID=paperid)
        if request.POST:
            post = request.POST
            old.Title=post['Title']
            old.Author1=post['Author1']
            old.Author2=post['Author2']
            old.Author3=post['Author3']
            old.Author4=post['Author4']
            old.Keyword=post['Keyword']
            old.Publisher=post['Publisher']
            old.PublishDate=post['Publishdate']
            old.Summary=post['Summary']
            old.Grade1=post['grade1']
            old.Grade2=post['grade2']
            old.Grade3=post['grade3']
            old.save()
            return HttpResponseRedirect('/publish/')
        c=Context({"paper":old})
        return render_to_response("pbmodify.html",c,d)

def update(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
    d=Context({"a":a})
    paperid = request.GET["id"]
    old = Paper.objects.get(PaperID=paperid)
    if request.FILES:
        post = request.FILES
        File=post['file']
        
        File.name=old.PaperID+".doc"
    
        from os import environ  
        online = environ.get("APP_NAME", "")   
        
        if online:  
            import sae.const  
            access_key = sae.const.ACCESS_KEY  
            secret_key = sae.const.SECRET_KEY  
            appname = sae.const.APP_NAME  
            domain_name = "cunchu"
            
            import sae.storage  
            s = sae.storage.Client()  
            ob = sae.storage.Object(File.read())  
            url = s.put(domain_name, File.name, ob)  
            
        old.address="http://papermanage-cunchu.stor.sinaapp.com/"+str(File.name)
        old.save()
        return HttpResponseRedirect('/reference/') 
    return render_to_response('addfile.html',d)
def pbupdate(request):
    if request.session.get('username')==None:
        a=0
        return HttpResponseRedirect('/login/')
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        paperid = request.GET["id"]
        old = Pbpaper.objects.get(PaperID=paperid)
        if request.FILES:
            post = request.FILES
            File=post['file']
            File.name=old.PaperID+".doc"
    
            from os import environ  
            online = environ.get("APP_NAME", "")   
            
            if online:  
                import sae.const  
                access_key = sae.const.ACCESS_KEY  
                secret_key = sae.const.SECRET_KEY  
                appname = sae.const.APP_NAME  
                domain_name = "cunchu"
                
                import sae.storage  
                s = sae.storage.Client()  
                ob = sae.storage.Object(File.read())  
                url = s.put(domain_name, File.name, ob)  
                
            old.address="http://papermanage-cunchu.stor.sinaapp.com/"+str(File.name)
            old.save() 
            return HttpResponseRedirect('/publish/') 
        return render_to_response('addfile.html', d)

def register(request):
    a=0
    if request.POST:
        post = request.POST
        users=User.objects.all()
        for u in users:
            if (u.username==post['name'] or u.name==post['realname']):
                a=1
                c=Context({"a":a})
                return render_to_response("registered.html", c)
        if a==0:
            new_user=User()
            new_user.username=post['name']
            new_user.password=post['password1']
            new_user.name=post['realname']
            new_user.email=post['email']
            new_user.tel=post['tel']
            new_user.save()
            return HttpResponseRedirect("/login/")
    else:
        return render_to_response("registered.html")
        

def login(request):
    x=0
    if request.POST:
        post = request.POST
        users=User.objects.all()
        name=post['name']
        word=post['password']
        for u in users:
            if u.username==name:
                x=1
        if x==1:
            user=User.objects.get(username=name)
            if user.password==word:
                request.session['username']=name
                request.session['realname']=user.name
                return HttpResponseRedirect("/personal/")
            else:
                x=0  
                c=Context({"x":x})
                return render_to_response("login.html", c)
        else:
            x=0  
            c=Context({"x":x})
            return render_to_response("login.html", c)
    else:
        return render_to_response("login.html")  

def loginout(request):
    del request.session['username']
    return HttpResponseRedirect("/home/")
'''
def load(request):
    paperid = request.GET["id"]
    paper = Paper.objects.get(PaperID=paperid)
    b = str(paper.File)[12:]
    c=Context({"b":b})
    return render_to_response("load.html",c) 

def pbload(request):
    paperid = request.GET["id"]
    paper = Pbpaper.objects.get(PaperID=paperid)
    b = str(paper.File)[12:]
    c=Context({"b":b})
    return render_to_response("load.html",c) 
'''
def authsearch(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        if request.POST:
            name = request.POST["name"]
            author_list=[]
            l1=Pbpaper.objects.filter(Author1=name)
            l2=Pbpaper.objects.filter(Author2=name)
            l3=Pbpaper.objects.filter(Author3=name)
            l4=Pbpaper.objects.filter(Author4=name)
            paper_list=list(set(l1).union(set(l2)).union(set(l3)).union(set(l4)))
            for paper in paper_list:
                author_list.append(paper.Author1)
                author_list.append(paper.Author2)
                author_list.append(paper.Author3)
                author_list.append(paper.Author4)
            author_list = list(set(author_list))
            if author_list != []:
                author_list.remove(name)
            paper_l=[]
            for author in author_list:
                if author != "":
                    l=[author,]
                    for paper in paper_list:
                        if paper.Author1==author or paper.Author2==author or paper.Author3==author or paper.Author4==author:
                            l.append(paper.Title)
                    paper_l.append(l)
            c=Context({"paper_l":paper_l}) 
            return render_to_response("authsearch.html", c, d) 
        return render_to_response("authsearch.html", d) 

def personal(request):
    if request.session.get('username')==None:
        a=0
    else:
        a=request.session.get('realname')
        d=Context({"a":a})
        author_list=[]
        l1=Pbpaper.objects.filter(Author1=a)
        l2=Pbpaper.objects.filter(Author2=a)
        l3=Pbpaper.objects.filter(Author3=a)
        l4=Pbpaper.objects.filter(Author4=a)
        paper_list=list(set(l1).union(set(l2)).union(set(l3)).union(set(l4)))
        score=0.0
        for paper in paper_list:
            if paper.Author1==a:
                score += float(paper.Score)*1.0
            elif paper.Author2==a:
                score += float(paper.Score)*0.6
            elif paper.Author3==a:
                score += float(paper.Score)*0.3
            elif paper.Author4==a:
                score += float(paper.Score)*0.1
        for paper in paper_list:
            author_list.append(paper.Author1)
            author_list.append(paper.Author2)
            author_list.append(paper.Author3)
            author_list.append(paper.Author4)
        author_list = list(set(author_list))
        if author_list != []:
            author_list.remove(a)
        paper_l=[]
        for author in author_list:
            if author != "":
                l=[author,]
                for paper in paper_list:
                    if paper.Author1==author or paper.Author2==author or paper.Author3==author or paper.Author4==author:
                        l.append(paper.Title)
                paper_l.append(l)
        author=User.objects.get(name=a)
        inf=[author, score, paper_l, paper_list]
        c=Context({"inf":inf})
        return render_to_response("personal.html", c, d) 
        
def fix(request):
    if request.session.get('username')==None:
        b=0
    else:
        b=request.session.get('realname')
        d=Context({"b":b})
        a=0
        if request.POST:
            post = request.POST
            username=request.session.get('username')
            user=User.objects.get(username=username)
            if user.password==post['password0']:
                user.password=post['password1']
                user.save()
                return HttpResponseRedirect("/personal/")
            else:
                a=1
                c=Context({"a":a})
                return render_to_response("fix.html", c, d) 
        else:
            return render_to_response("fix.html", d)



    

    


    

    
