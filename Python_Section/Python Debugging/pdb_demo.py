import pdb
#set_trace()  this sets a break point

#once the breakpoint is set:
##c = continue
##n = next (stop after executing the next line within the current funtion)
##s = step (stop as soon as possible even in a called function)
##l = show location
##pp = pretty print

def pdbTest():
    pdb.set_trace()
    print("First Line")
    pdb.set_trace()
    print("Second line")
    pdb.set_trace()
    print("Third Line")
    pdb.set_trace()
    print("Fourth Line")
    pdb.set_trace()
    print("Fifth line")

pdbTest()