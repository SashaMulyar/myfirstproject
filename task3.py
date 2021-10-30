# with open('text.txt', 'r', encoding='utf-8') as t:
#     t=t.read()
# t=t.split()
# print(t)

# p=''
# for i in range(len(t)):
#     p+=t[i]+' '
#     if len(p)==40:
#         print(p)
#         p=''
#     if i == (len(t)-1):
#         print(p)
#         break
#     if len(p)+len(t[i+1])>40:
#         print(p)
#         p=''


x = int(input("Введите максимальное количество символов в строке, которое должно быть больше 35"))
if x <= 35:
    while x <= 35:
        x = int(input(
            "Неверный ввод. Введите максимальное количество символов в строке, которое должно быть больше 35"))

with open("text.txt", "a", encoding="utf-8") as f:
    curs_max = f.tell()


with open("text.txt", "r", encoding="utf-8") as donor:
    with open("readytext.txt", "w", encoding="utf-8") as receiver:
        curs = 0
        while True:
            donor.seek(curs)
            s = donor.readline(x+1)
            curs += len(s.encode("utf-8"))
            if curs >= curs_max:
                break
            elif s[-1] == " " or s[-1] == "\n":
                s = s[:-1]
            else:
                l = s.split()
                curs = curs-len(l[-1].encode("utf-8"))
                space = len(l.pop())
                if space % (len(l)-1) != 0:
                    add_space = space % (len(l)-1)
                    for i in range(len(l)-1):
                        l[i] += " "
                        add_space -= 1
                        if add_space == 0:
                            break
                mult_space = space//(len(l)-1)
                for i in range(len(l)-1):
                    for j in range(mult_space):
                        l[i] += " "
                s = " ".join(l)
            receiver.write(s+"\n")
        receiver.write(s)
    

    
    