b = 256
string1,string2=str(raw_input()).split()
def areIsomorphic():
	
    m = len(string1)
    n = len(string2)
 
    
    
    if m != n:
        return ("no")
        
    
    
    marked = ["no"] *b
    map = [-1] *b
    
    for i in range(n):
    	
         
        
        if map[ord(string1[i])] == -1:
            if marked[ord(string2[i])] == True:
                return ("no")
            marked[ord(string2[i])] = True
            map[ord(string1[i])] = string2[i]
        elif map[ord(string1[i])] != string2[i]:
            return ("no")
 
    return ("yes")
    
print areIsomorphic()
