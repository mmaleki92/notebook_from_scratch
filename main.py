import json

notebook = {}

message = """
1 --> add a note
2 --> edit a note
3 --> show notes
4 --> delete a note
5 --> save to json
"""
print(message)
command = input('1/2/3/4\n')
note_id = 0
    elif command=='5':
        with open('notebook.json', 'w') as f:
            json.dump(notebook, f)
