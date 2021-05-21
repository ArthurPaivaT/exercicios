dfa = {'A':{'b':'B'},
       'B':{'a':'B', 'b': 'D','c':'C'},
       'C':{'a':'B'},
       'D':{'b':'A'}}

text = input().lower()
boolean = False
state = 'A'
end = {'D'} 
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
