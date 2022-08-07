## alternating prime sequence
def cross(car, street):
    dp = [[0 for _ in range(car[-1]+1)] for _ in range(2)]
    res = ["NAN" for _ in range(len(car))]

    ## Base Case
    for i in range(len(car)):
        if car[i] == 0 and street[i]==1:
            dp[1][0] = 1
            res[i] = 0

    dp[0][0] = 0
    # dp[0][1] = 1
    # temp = car.copy()


    for i in range(1,car[-1]+1):
        for j in range(len(car)):
            car_arrive = car[j]
            st = street[j]
            if car_arrive==i and st == 1:
                if dp[1][i-1] == 1 or dp[0][i-1] == 0:
                    dp[1][i] = 1
                    res[j] = car_arrive

            if car_arrive==i and st == 0:
                if dp[0][i-1] == 1 or dp[1][i-1]==0:
                    dp[0][i] = 1
                    res[j] = car_arrive


        car = [i+1 if car[t]<=i and res[t]!=car[t] else car[t] for t in range(len(car))]

        print(dp)
        print(car)
        print(res)


if __name__ == '__main__':
    car = [0,0,1,4]
    street = [0,1,1,0]
    result = cross(car, street)
    print(result)