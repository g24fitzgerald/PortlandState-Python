#Copyright (c) 2014 Gina Fitzgerald 
#In class exercise

#create email recognizer ('[any lowercase letter] + @pdx.edu')
schnitzel = re.compile('[a-z] + @pdx.edu')

print(schnitzel.fullmatch(asdfadsf@pdx.edu))

#create name recognizer ('(Firstname) (space) (Lastname)') 
schnitzel2= re.compile('([A-Z][a-z])+()+([A-Z] +[a-z])')
print(schnitzel2.fullmatch(Jane Doe))
