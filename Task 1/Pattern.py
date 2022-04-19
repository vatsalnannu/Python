for i in range(7):
  if(i<(7/2)):
    print(" "*(int((7/2)-i)),"#"*((i*2)+1))
  else:
    print(" "*(int(i-(7/2)+1)),"#"*((7-i)*2-1))
