from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        file_name = request.form.get('file_name')
        file_context = request.form.get('file_context')
        fw = open(f'./files/{file_name}', 'w')
        fw.write(file_context)
        fw.close()

        return render_template('created.html', message=file_name)
    # return redirect('/') # Перекинуть пользователя, если он сам зашел на /create без данных из формы
    return 'WHAT?!! Go away!111'


@app.route('/show')
def show():
    files_paths = os.listdir('./files')
    files_paths.remove('deleted_files')
    return render_template('show.html', list_files = files_paths)


@app.route('/file/<name>')
def file_fn(name):
    path = f'./files/{name}'
    file_context = open(path,'r').read()
    return render_template('file.html', file_name=path, file_context=file_context)


@app.route('/delete/<name>')
def file_delete(name):
    try:
        path = f'./files/{name}'
        # os.remove(path)
        os.rename(path, f'./files/deleted_files/{name}')
        return f'Ok, file {name} deleted!'
    except:
        return f'{name} not found!'