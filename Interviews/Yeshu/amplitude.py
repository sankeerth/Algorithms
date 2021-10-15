def spiral(points):
    seen = set()
    P = [(point, i) for i, point in enumerate(points)]
    
    bottomSort = sorted(P, key=lambda x: x[0][1])
    rightSort = sorted(P, key=lambda x: -x[0][0])

    print(bottomSort)
    print()
    print(rightSort)

    b, r, t, l = 0, 0, len(points)-1, len(points)-1
    result = []

    seen.add(bottomSort[b][1])
    result.append(bottomSort[b][1])
    b += 1

    while len(seen) < len(points):
        while r < len(points):
            if rightSort[r][1] not in seen:
                seen.add(rightSort[r][1])
                result.append(rightSort[r][1])
                r += 1
                break
            r += 1

        while t > 0:
            if bottomSort[t][1] not in seen:
                seen.add(bottomSort[t][1])
                result.append(bottomSort[t][1])
                t -= 1
                break
            t -= 1

        while l > 0:
            if rightSort[l][1] not in seen:
                seen.add(rightSort[l][1])
                result.append(rightSort[l][1])
                l -= 1
                break
            l -= 1

        while b < len(points):
            if bottomSort[b][1] not in seen:
                seen.add(bottomSort[b][1])
                result.append(bottomSort[b][1])
                b += 1
                break
            b += 1

    return result

print(spiral([[11,-3], [-2,2], [-1,9], [-10,3], [-3,-9], [-2,-5], [9, 5], [-6,7], [-5,-1], [2,3]]))
