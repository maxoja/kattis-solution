##x = ['12:00 a.m.','12:10 a.m.',
##           '1:00 a.m.','1:10 a.m.',
##           '2:00 a.m.','2:10 a.m.',
##           '3:00 a.m.','3:10 a.m.',
##           '4:00 a.m.','4:10 a.m.',
##           '5:00 a.m.','5:10 a.m.',
##           '6:00 a.m.','6:10 a.m.',
##           '12:00 p.m.','12:10 p.m.',
##           '1:00 p.m.','1:10 p.m.',
##           '2:00 p.m.','2:10 p.m.',
##           '3:00 p.m.','3:10 p.m.',
##           '4:00 p.m.','4:10 p.m.',
##           '5:00 p.m.','5:10 p.m.'] ###

n = int(input())
##n = len(x) ###

while n != 0:
    app = []
    for _ in range(n):
        time = input()
##        time = x.pop(0) ###
        ending = time[-4:]
        parts = time.split(':')
        h = int(parts[0])
        m = int(parts[1][:2])

        if ending == 'a.m.' and h == 12:
            h = 0
        elif ending == 'p.m.' and h < 12:
            h += 12
        
        tick = h*100 + m
        app.append(tick)

    app = sorted(app)
    
    for a in app:
        h = a//100
        m = a%100
        
        if h == 0:
            ending = 'a.m.'
            h = 12
        elif h <= 11:
            ending = 'a.m.'
        elif h == 12:
            ending = 'p.m.'
        else:
            h = h-12
            ending = 'p.m.'

        print(str(h)+':'+format(m,'02d'), ending)
        
    print()
    
    n = int(input())
