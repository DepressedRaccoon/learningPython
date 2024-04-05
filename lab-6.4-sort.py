def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1


def main():
    n = int(input("Enter the number of line segments: "))
    segments = []
    for i in range(n):
        segment = float(input("Enter segment {}: ".format(i + 1)))
        segments.append(segment)

    bubble_sort(segments)

    valid_triangles = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if is_valid_triangle(segments[i], segments[j], segments[k]):
                    valid_triangles.append((segments[i], segments[j], segments[k]))

    if valid_triangles:
        print("Valid triangle combinations:")
        for triangle in valid_triangles:
            print(triangle)
    else:
        print("No valid triangle combinations found.")


main()
