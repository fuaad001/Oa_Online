from flask import render_template, request, redirect, url_for, abort
from . import main
from .. import db, photos
from flask_login import login_required, current_user
from ..models import User, Notice, Certificate, Impediment, Agreement, Witness
from .forms import UpdateProfile,CivilMarriage

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Oa Online'

    return render_template('index.html', title = title)

@main.route('/types')
def types():
    '''
    View root page function that returns the types page and its data
    '''

    title = 'Types'

    return render_template('types.html')

@main.route('/importance')
def importance():
    '''
    View root page function that returns the importance page and its data
    '''

    title = 'importance'

    return render_template('importance.html')

@main.route('/requirements')
def requirements():
    '''
    View root page function that returns the requirements page and its data
    '''

    title = 'requirements'

    return render_template('requirements.html')

@main.route('/process')
def process():
    '''
    View root page function that returns the process page and its data
    '''

    title = 'process'

    return render_template('process.html')

@main.route('/divorce')
def divorce():
    '''
    View root page function that returns the divorce page and its data
    '''

    title = 'divorce'

    return render_template('divorce.html')

@main.route('/divorce2')
def divorce2():
    '''
    View root page function that returns the divorce2 page and its data
    '''

    title = 'divorce2'

    return render_template('divorce2.html')

@main.route('/process2')
def process2():
    '''
    View root page function that returns the process2 page and its data
    '''

    title = 'process2'

    return render_template('process2.html')

@main.route('/laws')
def laws():
    '''
    View root page function that returns the laws page and its data
    '''

    title = 'laws'

    return render_template('laws.html')

@main.route('/marry/notice', methods=["GET", "POST"])
def notice():
    '''
    View root page function that returns the notice page and its data
    '''

    notice = Notice()

    if request.method == "POST":
        district = request.form['district']
        spouse = request.form["spouse"]
        g_name = request.form["g_name"]
        g_condition = request.form["g_condition"]
        g_occupation = request.form["g_occupation"]
        g_age = request.form["g_age"]
        g_residence = request.form["g_residence"]
        g_consent = request.form["g_consent"]
        b_name = request.form["b_name"]
        b_condition = request.form["b_condition"]
        b_occupation = request.form["b_occupation"]
        b_age = request.form["b_age"]
        b_residence = request.form["b_residence"]
        b_consent = request.form["b_consent"]
        dd = request.form["dd"]
        mm = request.form["mm"]
        yy = request.form["yy"]
        signature = request.form["signature"]

        notice.district = district
        notice.spouse = spouse
        notice.g_name = g_name
        notice.g_condition = g_condition
        notice.g_occupation = g_occupation
        notice.g_age = g_age
        notice.g_residence = g_residence
        notice.g_consent = g_consent
        notice.b_name = b_name
        notice.b_condition = b_condition
        notice.b_occupation = b_occupation
        notice.b_age = b_age
        notice.b_residence = b_residence
        notice.b_consent = b_consent
        notice.dd = dd
        notice.mm = mm
        notice.yy = yy
        notice.signature = signature
        notice.user_id = current_user.id

        db.session.add(notice)
        db.session.commit()

        return redirect(url_for('.index'))


    title = 'Marriage Notice'

    return render_template('marriages/notice.html')

@main.route('/marry/sign_certificate')
def certificate():
    '''
    View root page function that returns the certificate page and its data
    '''

    certificate = Certificate()

    if request.method == "POST":
        g_date = request.form["g_date"]
        g_name = request.form["g_name"]
        g_condition = request.form["g_condition"]
        g_occupation = request.form["g_occupation"]
        g_age = request.form["g_age"]
        g_residence = request.form["g_residence"]
        g_fname = request.form["g_fname"]
        g_foccupation = request.form["g_foccupation"]
        b_date = request.form["b_date"]
        b_name = request.form["b_name"]
        b_condition = request.form["b_condition"]
        b_occupation = request.form["b_occupation"]
        b_age = request.form["b_age"]
        b_residence = request.form["b_residence"]
        g_fname = request.form["b_fname"]
        g_foccupation = request.form["b_foccupation"]
        groom = request.form["groom"]
        bride = request.form["bride"]
        witness1 = request.form["witness1"]
        witness2 = request.form["witness2"]
        date = request.form["date"]

        certificate.g_date = g_date
        certificate.g_name = g_name
        certificate.g_condition = g_condition
        certificate.g_occupation = g_occupation
        certificate.g_age = g_age
        certificate.g_residence = g_residence
        certificate.g_fname = g_fname
        certificate.g_foccupation = g_foccupation
        certificate.b_date = b_date
        certificate.b_name = b_name
        certificate.b_condition = b_condition
        certificate.b_occupation = b_occupation
        certificate.b_age = b_age
        certificate.b_residence = b_residence
        certificate.b_fname = b_fname
        certificate.b_foccupation = b_foccupation
        certificate.groom = groom
        certificate.bride = bride
        certificate.witness1 = witness1
        certificate.witness2 = witness2
        certificate.date = date
        certificate.user_id = current_user.id


        db.session.add(certificate)
        db.session.commit()

        return redirect(url_for('.index'))

    title = 'Marriage Certificate'

    return render_template('marriages/certificate.html')

@main.route('/marry/impediment_certificate')
def impediment():
    '''
    View root page function that returns the impediment page and its data
    '''

    impediment = Impediment()

    if request.method == "POST":
        spouse = request.form["spouse"]
        at = request.form["at"]
        in_input = request.form["in_input"]
        surname = request.form["surname"]
        forename = request.form["forename"]
        country = request.form["country"]
        date = request.form["date"]
        father = request.form["father"]
        sex = request.form["sex"]
        race = request.form["race"]
        religion = request.form["religion"]
        residence = request.form["residence"]
        condition = request.form["condition"]
        occupation = request.form["occupation"]
        dd = request.form["dd"]
        mm = request.form["mm"]
        yy = request.form["yy"]
        signature = request.form["signature"]

        impediment.spouse = spouse
        impediment.at = at
        impediment.in_input = in_input
        impediment.surname = surname
        impediment.forename = forename
        impediment.country = country
        impediment.date = date
        impediment.father = father
        impediment.sex = sex
        impediment.race = race
        impediment.religion = religion
        impediment.residence = residence
        impediment.occupation =  occupation
        impediment.condition = condition
        impediment.dd = dd
        impediment.mm = mm
        impediment.yy = yy
        impediment.signature = signature
        impediment.user_id = current_user.id

        db.session.add(impediment)
        db.session.commit()

        return redirect(url_for('.index'))

    return render_template('marriages/impediment.html')

@main.route('/About_us')
def about():
    '''
    View root page function that returns the about us page and its data
    '''

    title = 'About us'

    return render_template('about.html')

@main.route('/user/<user_id>')
def profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    certificate = Certificate.query.filter_by(user_id = user.id)
    notice = Notice.query.filter_by(user_id = user.id)
    impediment = Impediment.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, certificate = certificate, notice = notice, impediment = impediment)

@main.route('/user/<user_id>/update',methods = ['GET','POST'])
@login_required
def update_profile(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    agreement = Agreement()

    if form.validate_on_submit():
        agreement.husband_vows = form.husband_vows.data
        agreement.wife_vows = form.wife_vows.data
        agreement.dowry_agreement = form.dowry_agreement.data
        agreement.other_agreements = form.other_agreements.data
        agreement.user_id = current_user.id


        db.session.add(agreement)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    return render_template('profile/update.html',form =form,user=user)

@main.route('/user/<user_id>/update/pic',methods= ['POST'])
@login_required
def update_pic(user_id):
    user = User.query.filter_by(id = user_id).first()
    if 'husband_photo' in request.files or 'wife_photo' in request.files:
        filename = photos.save(request.files['husband_photo'])
        path = f'photos/{filename}'
        user.husband_pic_path = path
        filename = photos.save(request.files['wife_photo'])
        path = f'photos/{filename}'
        user.wife_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',user_id = user.id))

@main.route('/user/<user_id>/registrar')
def registrar(user_id):
    user = User.query.filter_by(id = user_id).first()
    notice = Notice.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template("marriages/registrar.html", user = user, notice = notice)

@main.route('/user/<user_id>/attestation')
def attestation(user_id):
    user = User.query.filter_by(id = user_id).first()
    notice = Notice.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template("marriages/attestation.html", user = user, notice = notice)

@main.route('/user/<user_id>/civil_wedding',methods = ['GET','POST'])
@login_required
def civil(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = CivilMarriage()
    witness = Witness()

    if form.validate_on_submit():
        witness.witness1_name = form.witness1_name.data
        witness.witness2_name = form.witness2_name.data
        witness.witness1_id = form.witness1_id.data
        witness.witness2_id = form.witness2_id.data
        witness.witness1_dob = form.witness1_dob.data
        witness.witness2_dob = form.witness2_dob.data
        witness.user_id = current_user.id


        db.session.add(witness)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    title = 'Civil Marriage'

    return render_template('marriages/civil.html',form =form,user=user, title = title)

@main.route('/user/<user_id>/customary_wedding',methods = ['GET','POST'])
@login_required
def customary(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = CivilMarriage()
    witness = Witness()

    if form.validate_on_submit():
        witness.witness1_name = form.witness1_name.data
        witness.witness2_name = form.witness2_name.data
        witness.witness1_id = form.witness1_id.data
        witness.witness2_id = form.witness2_id.data
        witness.witness1_dob = form.witness1_dob.data
        witness.witness2_dob = form.witness2_dob.data
        witness.user_id = current_user.id


        db.session.add(witness)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    title = 'Customary Marriage'

    return render_template('marriages/customary.html',form =form,user=user, title = title)

@main.route('/user/<user_id>/islamic_wedding',methods = ['GET','POST'])
@login_required
def muslim(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = CivilMarriage()
    witness = Witness()

    if form.validate_on_submit():
        witness.witness1_name = form.witness1_name.data
        witness.witness2_name = form.witness2_name.data
        witness.witness1_id = form.witness1_id.data
        witness.witness2_id = form.witness2_id.data
        witness.witness1_dob = form.witness1_dob.data
        witness.witness2_dob = form.witness2_dob.data
        witness.user_id = current_user.id


        db.session.add(witness)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    title = 'Islamic Marriage'

    return render_template('marriages/muslim.html',form =form,user=user, title = title)

@main.route('/user/<user_id>/christian_wedding',methods = ['GET','POST'])
@login_required
def christian(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = CivilMarriage()
    witness = Witness()

    if form.validate_on_submit():
        witness.witness1_name = form.witness1_name.data
        witness.witness2_name = form.witness2_name.data
        witness.witness1_id = form.witness1_id.data
        witness.witness2_id = form.witness2_id.data
        witness.witness1_dob = form.witness1_dob.data
        witness.witness2_dob = form.witness2_dob.data
        witness.user_id = current_user.id


        db.session.add(witness)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    title = 'Christian Marriage'

    return render_template('marriages/christian.html',form =form,user=user, title = title)

@main.route('/user/<user_id>/hindu_wedding',methods = ['GET','POST'])
@login_required
def hindu(user_id):
    user = User.query.filter_by(id = user_id).first()
    if user is None:
        abort(404)

    form = CivilMarriage()
    witness = Witness()

    if form.validate_on_submit():
        witness.witness1_name = form.witness1_name.data
        witness.witness2_name = form.witness2_name.data
        witness.witness1_id = form.witness1_id.data
        witness.witness2_id = form.witness2_id.data
        witness.witness1_dob = form.witness1_dob.data
        witness.witness2_dob = form.witness2_dob.data
        witness.user_id = current_user.id


        db.session.add(witness)
        db.session.commit()

        return redirect(url_for('.profile',user_id=user.id))

    title = 'Hindu Marriage'

    return render_template('marriages/hindu.html',form =form,user=user, title = title)

@main.route('/user/<user_id>/marriage_certificate')
def certificate2(user_id):
    user = User.query.filter_by(id = user_id).first()
    certificate = Certificate.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template("marriages/certificate2.html", user = user, certificate = certificate)

@main.route('/user/<user_id>/impediment_certificate')
def impediment2(user_id):
    user = User.query.filter_by(id = user_id).first()
    impediment = Impediment.query.filter_by(user_id = user.id)

    if user is None:
        abort(404)

    return render_template("marriages/impediment2.html", user = user, impediment = impediment)
