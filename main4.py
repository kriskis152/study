chan = []
comanda = (str(0))
razmer = int(len(chan))
number = int(0)
comanda_exit = bool(False)
zadacha = str("0")
while not comanda_exit : 
 comanda = input()

 if comanda == "add" or comanda == "Add" :
     zadacha = input()
     chan.append(zadacha)
     razmer = razmer + 1
 elif comanda == "remove" or comanda == "Remove" :
     number = int(input())
     if number > razmer or number < 0 :
        print("Wrong number")
        number = int(input())
     del chan[number]
     razmer = razmer - 1
 elif comanda == "list" or comanda == "List":
     print (chan, razmer)

 elif comanda == "exit" or comanda == "Exit" :
     comanda_exit = True
