# 从用户获得长和宽 (get number from user)
length = float(input("Enter the length of the plot in meters: "))
width = float(input("Enter the width of the plot in meters: "))
# 计算面积和周长 (calculate area and perimeter)
area = length * width
perimeter = 2 * (length + width)
# 输出面积和周长 (output area and perimeter)
print(f"Area: {area} square meters")
print(f"Perimeter: {perimeter} meters")
