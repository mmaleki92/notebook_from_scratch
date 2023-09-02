notebook = {}

message = """
1 --> add a note
2 --> edit a note
3 --> show notes
4 --> delete a note
"""
print(message)
command = input('1/2/3/4\n')
note_id = 0
if command == '1':
    note = {}
    note['title'] = input('title:') 
    note['text'] = input('text:')
notebook[note_id]  = note
print(notebook)