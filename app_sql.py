from flask import Flask, render_template, request
from flask import url_for, flash, redirect
from app_function import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'GU XIN is 资产评估师, 这是密码'


@app.route('/')
def index():
    conn = get_db_conn()
    posts = conn.execute('select * from posts order by created desc').fetchall()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    new_post = get_post(post_id)
    return render_template('Post.html', post=new_post)


@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('标题不能为空')
        elif not content:
            flash('内容不能为空')
        else:
            conn = get_db_conn()
            conn.execute('insert into posts (title, content) values (?, ?)',
                         (title, content)
                         )
            conn.commit()
            conn.close()

            flash('文章保存成功')
            return redirect(url_for('index'))
    return render_template('new.html')


@app.route('/del_post/<post_id>', methods=['POST', ])
def del_post(post_id):
    delete_post(post_id)
    flash('删除成功')
    return redirect(url_for('index'))


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    _post = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('标题不能为空')
        elif not content:
            flash('内容不能为空')
        else:
            edit_post(title, content, post_id)
            flash('文章修改成功')
            return redirect(url_for('index'))
    return render_template('edit.html', post=_post)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    pass
    # app.run(debug=True)
