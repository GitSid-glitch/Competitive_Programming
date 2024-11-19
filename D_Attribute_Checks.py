def main():
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    m += 1
    dp = [[0] * m for _ in range(2)]
    adder = [[(0, 0)] * m for _ in range(2)]
    cur_cnt = 0

    for i in ls:
        if i == 0:
            add = 0
            for a in range(cur_cnt + 1):
                add += adder[0][a][0]
                dp[0][a] += add

            add = 0
            for b in range(cur_cnt, -1, -1):
                add += adder[0][b][1]
                dp[0][b] += add

            for j in range(m):
                if j < m - 1:
                    dp[1][j + 1] = max(dp[1][j + 1], dp[0][j])
                dp[1][j] = max(dp[1][j], dp[0][j])

            cur_cnt += 1
            dp[0] = dp[1][:]
            dp[1] = [0] * m
            adder[0] = adder[1][:]
            adder[1] = [(0, 0)] * m

        elif i > 0:
            if abs(i) > cur_cnt:
                continue
            adder[0][abs(i)] = (adder[0][abs(i)][0] + 1, adder[0][abs(i)][1])

        else:
            if abs(i) > cur_cnt:
                continue
            adder[0][cur_cnt - abs(i)] = (adder[0][cur_cnt - abs(i)][0], adder[0][cur_cnt - abs(i)][1] + 1)

    add = 0
    for a in range(m):
        add += adder[0][a][0]
        dp[0][a] += add

    add = 0
    for b in range(m - 1, -1, -1):
        add += adder[0][b][1]
        dp[0][b] += add

    ans = 0
    for i in dp[0]:
        ans = max(ans, i)

    print(ans)


if __name__ == "__main__":
    main()
