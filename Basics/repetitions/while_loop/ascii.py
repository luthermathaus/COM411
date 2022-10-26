print("How many bars should be charged?")
target_bars = int(input())
bars_charged = 0

while bars_charged != target_bars:
    print("Charging: ", end="")
    bars_charged += 1
    print(bars_charged * "█ ")

print("The battery is fully charged")