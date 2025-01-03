garden = [[c for c in l] for l in open('input.txt').read().split('\n')]

cost = 0
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
seen = set()
for y in range(len(garden)):
    for x in range(len(garden[0])):
        if (x,y) in seen:
            continue
        perimeter = 0
        area = 0
        queue = [(x,y)]
        while len(queue) > 0:
            px,py = queue.pop(0)
            n_neighbours = 0
            if (px,py) in seen:
                continue
            for dx,dy in dirs:
                nx = px + dx
                ny = py + dy
                if 0 <= nx < len(garden[0]) and 0 <= ny < len(garden) and garden[ny][nx] == garden[py][px]:                    
                    queue.append((nx,ny))
                    n_neighbours += 1
            perimeter += 4-n_neighbours
            area += 1
            seen.add((px,py))
        cost += perimeter * area
print(cost)


https://www.google.com/search?q=how+to+find+the+sum+of+interior+angles+of+a+polygon&sca_esv=3cbb507ea125247b&sxsrf=ADLYWIKacydCrKftpjppqpd2SR0v0T7u8w%3A1735039316049&ei=VJlqZ9fYAvnHwPAP-cOMqQk&oq=how+to+find+the+sum+of+int&gs_lp=Egxnd3Mtd2l6LXNlcnAiGmhvdyB0byBmaW5kIHRoZSBzdW0gb2YgaW50KgIIADIKEAAYgAQYFBiHAjIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEiiMVDjEFipKnADeAGQAQCYAYkBoAHGD6oBBDIzLjO4AQPIAQD4AQGYAh2gAukPwgIKEAAYsAMY1gQYR8ICBBAjGCfCAgoQIxiABBgnGIoFwgIUEC4YgAQYkQIY0QMY1AIYxwEYigXCAgsQABiABBiRAhiKBcICChAAGIAEGEMYigXCAgsQLhiABBjRAxjHAcICChAuGIAEGEMYigXCAgUQLhiABMICCBAuGIAEGNQCwgINEAAYgAQYQxjJAxiKBcICCxAAGIAEGJIDGIoFmAMAiAYBkAYIkgcEMjUuNKAHntkB&sclient=gws-wiz-serp#vhid=8cDJ7SdSJ1o5JM&vssid=l
https://stackoverflow.com/questions/12083480/finding-internal-angles-of-polygon

# Example from above
x1 = 0
y1 = -1
x2 = 1
y2 = 0

x1*y2-x2*y1
0*0 - 1*-1 = 1

x1*x2 + y1*y2
0*1 + -1*0 = 0