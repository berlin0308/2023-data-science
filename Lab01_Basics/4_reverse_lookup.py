
""" C-4
Given a dictionary d and a key k, it is easy to find the corresponding value v = d[k]. This 
operation is called a lookup. But what if you have v and you want to find k? There is no simple 
syntax  for reverse lookup.  Implement  a  function  for  reverse  lookup  using  the  following 
template and note that there might be more than one key that maps to the value v. 

def reverse_lookup(d, v): 
  k = [] 
  #TODO 
  return k 

""" 

def reverse_lookup(d, v): 
    k = [] 
    for i in d.keys():
        if d[i] == v:
            k.append(i)

    return k 

d = {1:333, 2:444, 5:444}
print(reverse_lookup(d, 444))