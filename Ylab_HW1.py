# task 1
def domain_name(url):
    if (url.startswith('http')):
        url = url.split('//')[1]

    if (url.startswith('www')):
        return url.split('.')[1]
    else:
        return url.split('.')[0]

# task 2
def int32_to_ip(int32):
    blocks = ['0'] * 4
    for i in range(3,-1,-1):
        blocks[i] = str(int32 % (2**8))
        int32 //= 2**8
    return '.'.join(blocks)

# task 3
def zeros(n):
    answer = 0
    temp = 5
    while (n > temp):
        answer += n // temp
        temp *= 5
    return answer

# task 4
def iterators_to_str(iterators, s):
    result = ['-'] * len(s)

    for i in range(len(iterators)):
        result[iterators[i]] = ('banana')[i]

    return ''.join(result)


def recursion_for_task_4(s, iterators, position, result, banana):
    if (position == len(banana)):
        result.add(iterators_to_str(iterators, s))

    else:
        it = 0

        if (iterators):
            it = iterators[-1]

        while (it < len(s)):

            if (s[it] == banana[position]):
                iterators.append(it)
                recursion_for_task_4(s, iterators, position + 1, result, banana)
                iterators.pop()

            it += 1


def bananas(s) -> set:
    result = set()
    recursion_for_task_4(s, [], 0, result, 'banana')
    return result

# task 5
def recursion_for_task_5(primesL, limit, result, val):
    if (val <= limit):
        result.add(val)

        for i in primesL:
            recursion_for_task_5(primesL, limit, result, val * i)


def count_find_num(primesL, limit):
    result = set()
    temp = 1

    for i in primesL:
        temp *= i

    if (temp > limit):
        return []

    recursion_for_task_5(primesL, limit, result, temp)

    return [len(result), max(result)]


if __name__ == '__main__':
    # tests:

    # task 1
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"

    # task 2
    assert int32_to_ip(2154959208) == "128.114.17.104"
    assert int32_to_ip(0) == "0.0.0.0"
    assert int32_to_ip(2149583361) == "128.32.10.1"

    # task 3
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7

    # task 4
    assert bananas("banann") == set()
    assert bananas("banana") == {"banana"}
    assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                    "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                    "-ban--ana", "b-anana--"}
    assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
    assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}

    # task 5
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []

    print("Correct!")