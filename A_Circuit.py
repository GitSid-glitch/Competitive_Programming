t=int(input().strip())
output=[]

for i in range(t):
    n=int(input().strip())
    s=list(map(int, input().strip().split()))
    
    c=sum(s)
    
    if n==1 and c==2:
        min_on=0
        max_on=0
    else:
        min_on=c % 2  
        max_on=min(c, n)  
    
    output.append((min_on,max_on))

for i in output:
    print(i[0],i[1])


'''import sys
input = sys.stdin.read

def circuit_lights():
    # Read all input at once
    data = input().strip().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        # Read the number of lights
        n = int(data[index])
        index += 1
        # Read the states of the 2*n switches
        switches = list(map(int, data[index:index + 2 * n]))
        index += 2 * n
        
        # Count the total number of "on" switches
        count_on = sum(switches)
        
        # Calculate minimum and maximum lights that can be on
        min_lights_on = count_on % 2  # If even, all lights can be off; if odd, at least one will be on
        max_lights_on = min(count_on, n)  # Maximum lights on cannot exceed the number of lights
        
        results.append(f"{min_lights_on} {max_lights_on}")
    
    # Output all results at once
    sys.stdout.write("\n".join(results) + "\n")

# Call the function
circuit_lights()
'''

