

def countSubsequences(s): 

    countofa = 0
  
    countofb = 0
    countofc = 0
  
    for i in range(len(s)): 
      
        if (s[i] == 'a'): 
            countofa = (1 + 2 * countofa) 
  
        elif (s[i] == 'b'): 
            countofb = (countofa + 2 * countofb) 
  
        elif (s[i] == 'c'): 
            countofc = (countofb + 2 * countofc) 
  
    return countofc 
  
if __name__ == "__main__": 
    string = input('Enter the string')
    print(countSubsequences(string))

    
