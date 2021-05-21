dfa = {'A':{'a':'B'},
       'B':{'a':'C'},
       'C':{'a':'D'},
       'D':{'a':'E'},
       'E':{'a':'A'}
       }

text = input().lower()
boolean = False
state = 'A'
end = {'D', 'A'} 
try:
    for c in text:
        state = dfa[state][c]
    boolean = state in end
except:
    boolean = False
if boolean:
    print("Aceito")
else: 
    print("Rejeitado")
