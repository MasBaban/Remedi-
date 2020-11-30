#Soal 1

def find_short(s):
    min_length = float("inf")

    for x in s.split():
        if len(x) < min_length:
            min_length = len(x)

    return min_length

print('find_short(many people get up early in the morning)')
print('the shortest word has', find_short('many people get up early in the morning'), 'char(s)')

print('find_short(every office would getting newest monitor)')
print('the shortest word has', find_short('every office would getting newest monito'), 'char(s)')

print('find_short(create new file after this morning)')
print('the shortest word has', find_short('create new file after this morning'), 'char(s)')

# Soal 2

def persistence(a):
    if a in [0,1,2,3,4,5,6,7,8,9]:
        print(0)
    elif a <0 :
        print( "please input positive number only")
    else:
        jumlahloop = 0
        while a>9:
            jumlahloop+=1
            akhir=1
            num_str = str(a)
            for i in num_str:
                akhir=akhir* int(i)
            a=akhir
        print(jumlahloop)
print('persistence(999)')
persistence(999)
print('because 9 x 9 x 9 = 279, than 7 x 2 x 9 = 126, than 1 x 2 x 6 = 12, than 1 x 2 = 2')
print('so it take four times multiplication until we get a single digit')

