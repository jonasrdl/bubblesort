numbers = [84, 23, 48284029187409184, 10, 214, 4829104, 244924, 99,
           49249823, 494912456, 95839020, 49086302, 2496785, 49012385,
           76876554, 678789654, 33432, 212, 34, 5, 7, 5, 34, 3123, 38]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            t = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = t
