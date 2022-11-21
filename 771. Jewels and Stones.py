def numJewelsInStones(jewels: str, stones: str) -> int:
    # jewarr = list(jewels)
    # stonarr = list(stones)
    # numOfJewels = 0
    # for i in jewarr:
    #     for j in range(len(stonarr)):
    #         if i == stonarr[j]:
    #             numOfJewels+=1
    # print(numOfJewels)
    print(sum(map(stones.count, jewels)))
    print(sum(map(jewels.count, stones)))


jewels = "aA"
stones = "aAAbbbb"
numJewelsInStones(jewels,stones)