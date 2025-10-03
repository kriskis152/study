chan = []
comanda = (str(0))
razmer = int(len(chan))
number = int(0)
comanda_exit = bool(False)

while not comanda_exit : 
  comanda = input()

if comanda == "add" or comanda == "Add" :
     chan.append(comanda)
     razmer = razmer + 1

elif comanda == "remove" or comanda == "Remove" :
     number = int(input())
     del chan[number]

elif comanda == "list" or comanda == "List":
     print (chan, razmer)

elif comanda == "exit" or comanda == "Exit" :
     comanda_exit = True
