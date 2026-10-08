class Cal:
    def sum(self, *num):
        total = 0
        for i in num:
            total += i 
        print(total)
add = Cal()
res = add.sum(10,20,50)
res1 = add.sum(10,58)
