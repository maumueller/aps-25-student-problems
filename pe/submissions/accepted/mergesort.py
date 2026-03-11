import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    v = [0] * n
    idx = 1
    for i in range(n):
        x = int(data[idx])
        v[x - 1] = i
        idx += 1
    w = [0] * n
    for i in range(n):
        w[i] = v[int(data[idx]) - 1]
        idx += 1

    def merge_sort(arr, left, right):
        if right - left <= 1:
            return 0
        mid = (left + right) // 2
        inv = merge_sort(arr, left, mid) + merge_sort(arr, mid, right)
        temp = []
        i, j = left, mid
        while i < mid and j < right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                inv += mid - i
                j += 1
        temp.extend(arr[i:mid])
        temp.extend(arr[j:right])
        arr[left:right] = temp
        return inv

    print(merge_sort(w, 0, n))

if __name__ == "__main__":
    main()

#CPU time: 0.969 seconds
#Peak memory usage: 167.50 MiB