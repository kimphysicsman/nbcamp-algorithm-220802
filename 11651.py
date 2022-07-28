# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
#
# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

def compare_point(point_1, point_2):
    if point_1[1] < point_2[1]:
        return True
    elif point_1[1] == point_2[1]:
        if point_1[0] < point_2[0]:
            return True
    return False


def merge_sort(array):
    n = len(array)

    if n == 1:
        return array

    mid = n // 2

    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


def merge(array_1, array_2):
    n_1 = len(array_1)
    n_2 = len(array_2)
    idx_1 = 0
    idx_2 = 0

    merge_list = []

    while True:
        if compare_point(array_1[idx_1], array_2[idx_2]):
            merge_list.append(array_1[idx_1])
            idx_1 += 1
            if idx_1 == n_1:
                merge_list.extend(array_2[idx_2:])
                break
        else:
            merge_list.append(array_2[idx_2])
            idx_2 += 1
            if idx_2 == n_2:
                merge_list.extend(array_1[idx_1:])
                break

    return merge_list


def main():
    # point_list = [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
    point_list = []
    n = int(input("input N : "))

    for _ in range(n):
        point = [int(item) for item in input("input x, y : ").split()]
        point_list.append(point)

    sort_list = merge_sort(point_list)

    for x, y in sort_list:
        print(x, y)

main()