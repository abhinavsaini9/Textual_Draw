import string

f = open("input.txt", 'r')                 # Input File conataining the text
symbols = string.ascii_lowercase + string.ascii_uppercase+string.punctuation + ' '
text = f.readlines()

commands = ""
commands += "f "

for j in range(50):                    #To set the Starting point of cursor can be defined whatever one likes
    commands += "w"
    
def output(l):
    s = ""
    for i in l:
        if i in symbols:
            s += "f{0}".format(i) + ""
            s += "d"
        s += "s"
        s += "f w"
    return s
    
o = open("output.txt", 'w')

for l in text:
    commands += output(l)
    
o.write(commands)                             # all the commands printed in the output file
