from os import path
from flask import Blueprint, current_app, render_template, request, redirect, url_for, Markup, abort
from flask.helpers import flash
from flask_login import login_required, current_user
from json import loads
from werkzeug.utils import secure_filename
from ..models import Blog
from ..helper import allowed_file, delete_file, get_user_id, add_to_database, get_blog, remove_blog, save_file, serialize, add_id
from .. import  db

# create a Blueprint object called blog.
blog = Blueprint('blog', __name__, 
                template_folder='templates', 
                static_folder='static',
                static_url_path='/blog')
                
# display blog page
@blog.route('/<int:post_id>/post')
def post(post_id):
    post = get_blog(post_id)
    if post is None:
        abort(404)
    author = get_user_id(post.writer_id)
    # deserialized from string into map
    sections = loads(post.content)

    return render_template('blog/post.html', post=post, author=author, sections=sections)

# create blog page
@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    # send POST request
    if request.method == 'POST':

        title = request.form.get('blog_title')
        contents = request.form.getlist('blog_contents')
        subtitles = request.form.getlist('blog_subtitles')
        image =  request.files['blog_img_file']

        # check if user upload the allow file extension
        if image and not allowed_file(image.filename):
            flash('Only allow file extension: \'png\', \'jpg\', \'jpeg\', \'gif\'', 'danger')
        else:
            # filter any file name contain invalidate format (ex. ../../../user.jpg)
            filename = secure_filename(image.filename)
            # serialized array into string by dumps from json library, it could be easily store into database
            serialized_section = serialize(contents, subtitles)

            new_blog = Blog(current_user.id, title, serialized_section, filename)
            add_to_database(new_blog)
            # check if user upload a image, if upload, then save the image to the uploaded file location 
            # and rename it as file name + blog id + file extension
            if filename != '':
                save_file(image, path.join(current_app.config['UPLOAD_FOLDER'], add_id(filename, new_blog.id)))
            return redirect(url_for('main.profile'))

    return render_template('blog/create.html', page_title='Create a New Post')

# edit blog page
@blog.route('/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = get_blog(post_id)
    sections = loads(post.content)
    # check if user enter blog that user has not credential to modify or not exist
    if current_user.id != post.writer_id:
        abort(404)

    if request.method == 'POST':
        title = request.form.get('blog_title')
        contents = request.form.getlist('blog_contents')
        subtitles = request.form.getlist('blog_subtitles')
        image =  request.files['blog_img_file']

        if image and not allowed_file(image.filename):
            flash('Only allow file extension: \'png\', \'jpg\', \'jpeg\', \'gif\'', 'danger')
            # update sections because user may want to keep their change in edit page
            sections = {}
            for i in range(len(contents)):
                sections[subtitles[i]] = contents[i]

        else:
            # filter any file name contain invalidate format (ex. ../../../user.jpg)
            filename = secure_filename(image.filename)
            # serialized array into string by dumps from json library, it could be easily store into database
            serialized_section = serialize(contents, subtitles)

            modify_blog = db.session.query(Blog).filter(Blog.id == post_id)
            blog = modify_blog.first()
            if filename == '' or filename == blog.image_file:
                # update the blog content and title but not image
                modify_blog.update({Blog.title: title, Blog.content: serialized_section, Blog.updated_date: db.func.now()}, synchronize_session=False)
            else:
                # removed existing image file
                if blog.image_file is not None:
                    delete_file(path.join(current_app.config['UPLOAD_FOLDER'], add_id(blog.image_file, blog.id)))
                modify_blog.update({Blog.title: title, Blog.content: serialized_section, Blog.image_file: filename, Blog.updated_date: db.func.now()}, synchronize_session=False)
                # save new image file
                save_file(image, path.join(current_app.config['UPLOAD_FOLDER'], add_id(filename, blog.id)))
            
            db.session.commit()
            return redirect(url_for('main.profile'))
    
    return render_template('blog/edit.html', page_title='Edit Post: ' + post.title , post=post, sections=sections)
    
# delete blog page
@blog.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id):
    remove_blog(post_id)
    return redirect(url_for('main.profile'))
