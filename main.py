import json
import os

message = """
1 --> add a note
2 --> edit a note
3 --> show notes
4 --> delete a note
5 --> save to json
"""
def create_notebook(nb_file_name):
    if not os.path.exists(nb_file_name):
        notebook = {}
        with open(nb_file_name, 'w') as f:
            json.dump(notebook, f)
    else:
        with open(nb_file_name, 'r') as f:
            notebook = json.load(f)
    return notebook

def command_center(note_id, command, nb_file_name):
    if command == '1':
        note = {}
        note['title'] = input('title:') 
        note['text'] = input('text:')
        notebook[note_id]  = note
    elif command == '2':
        note_id_edit = int(input('give me an id'))
        if note_id_edit in notebook:
            notebook[note_id_edit]['title'] = input('title:')
            notebook[note_id_edit]['text'] = input('text:')
    elif command == '3':
        show_notes(notebook)
    elif command == '4':
        delete_id = input('give me the id to delete')
        sure = input('are you sure? (y/n)')
        if sure == 'y':
            del notebook[delete_id]
    elif command=='5':
        with open(nb_file_name, 'w') as f:
            json.dump(notebook, f)
def show_notes(notebook):
    for id in notebook.keys():
        print('-'*10)
        print('Title:', notebook[id]['title'])
        print('Text:', notebook[id]['text'][0:10])
        print('-'*10)

note_id = 0
nb_file_name = 'notebook.json'
while True:
    notebook = create_notebook(nb_file_name)
    show_notes(notebook)
    print(message)
    command = input('1/2/3/4/5\n')
    command_center(note_id, command, nb_file_name)
   
    note_id += 1