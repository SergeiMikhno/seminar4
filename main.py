from mytree import MyTree

def heapsort (tree):
	l = []
	while tree.length() != 0:
		l.append(tree.delete())
	return l[::-1] 

t = MyTree()
with open("words_33.txt","r") as f:
    lines = f.readlines()
    for word in lines:
        t.insert(word[:-1])
        
    array = heapsort(t)
    
for word in array:
	print(word)    





