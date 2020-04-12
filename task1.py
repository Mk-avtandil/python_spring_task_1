class Counter:
    def count(self, values):
        sum,one,two,three,four,five,six = 0,0,0,0,0,0,0
        for i in values:
            if i == 1:
                one += 1
                if one < 3:
                    sum += 100
                elif one == 3:
                    sum += 800
                elif one > 3:
                    sum += 1000
            if i == 2:
                two += 1
                if two >= 3:
                    sum += 200 
            if i == 3:
                three += 1
                if three >= 3:
                    sum += 300
            if i == 4:
                four += 1
                if four >= 3:
                    sum += 400
            if i == 5:
                five += 1
                if five < 3:
                    sum += 50
                elif five == 3:
                    sum += 400
                elif five > 3:
                    sum += 500
            if i == 6:
                six += 1
                if six >= 3:
                    sum += 600

            if one == 1 and two == 1 and three == 1 and four == 1 and five == 1 and six == 1:
                sum = 1500

            if two == 2 and four == 2 and six == 2:
                sum = 750

        return sum