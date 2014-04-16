def file_fixer():
  commands=open("input2.txt","r")
  output=open("output.txt","r")
  command=commands.readlines()
  outputs=output.readlines()
  commands.close()
  output.close()
  output=open("output.txt","w")
  i=2
  for line in outputs:
    if line=="Command: \n":
      new_line = "Command: "+ command[i]     
      i+=1
      output.write(new_line)
    else:
      output.write(line)


file_fixer()
