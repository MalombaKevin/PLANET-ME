from threading import currentThread
from flask import render_template,redirect,url_for, abort, request
from app.models import Megapitch, User
from app.request import get_quotes
from . import main
from flask_login import login_required, current_user
from .forms import UpdateProfile, addMegaPitch
from .. import db
from .. import db,photos


@main.route('/')

def index():
  
    return render_template('index.html')

@main.route('/planetmeblogs')
def planetmeblogs():
    globalusers= Megapitch.query.all()

    
    return render_template('planetmeblogs.html', globalusers= globalusers)

@main.route('/planetmeblogs/theme/<theme>')
def planetmetheme(theme):
    
    globaltheme = Megapitch.get_megapitch(theme=theme)
    
    
    return render_template('planetmethemes.html', globaltheme = globaltheme )

@main.route('/planetmeblogs/users/')
def planetmeusers():
    
    globalusers = User.query.all()    
    
    return render_template('planetmeusers.html',globalusers=globalusers )

@main.route('/quotes')
def quotes():
    
    quotes =  get_quotes() 
    
    return render_template('quotes.html', quotes=quotes)

@main.route('/planetmeblogs/planetmediscussion/<int:id>')
def discuss(id):
    blog = Megapitch.query.filter_by(id=id).first()
    return render_template('planemediscussion.html', pitch = blog)


   


@main.route('/planetmepitch/new' ,methods = ['GET','POST'])
@login_required
def planetmepitch():
    user = User.query.filter_by(id = current_user.id).first()


    if user is None:
        abort(404)
    
    megaForm=addMegaPitch()

    if megaForm.validate_on_submit():
        theme = megaForm.theme.data
        title = megaForm.title.data
        contributors = megaForm.contributors.data
        pitch = megaForm.pitch.data
        # country = megaForm.country.data
        user_id = current_user._get_current_object().id
          
        new_megapitch_object=Megapitch(theme=theme, title=title, contributors=contributors,pitch=pitch,user_id=user_id)
     

        new_megapitch_object.save_megapitch()    
    
        
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/planetmepitch.html', megaForm = megaForm)


   

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
   

    if user is None:
        abort(404)
    

    user_id =current_user._get_current_object().id
    all_mega_pitches = Megapitch.query.filter_by(user_id = user_id).all()
    

    return render_template("profile/profile.html", user = user, pitches= all_mega_pitches)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))