import json
import os

message = """
1 --> add a note
2 --> edit a note
3 --> show notes
4 --> delete a note
5 --> save to json
"""
note_id = 0
while True:
    if not os.path.exists('notebook.json'):
        notebook = {}
        with open('notebook.json', 'w') as f:
            json.dump(notebook, f)
    else:
        with open('notebook.json', 'r') as f:
            notebook = json.load(f)
    print(notebook)
    print(message)
    command = input('1/2/3/4/5\n')
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
        print(notebook)
    elif command=='5':
        with open('notebook.json', 'w') as f:
            json.dump(notebook, f)
    note_id += 1
