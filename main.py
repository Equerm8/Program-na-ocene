from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
import keyboard

def dSdt(x, t):
    x, v = x
    return [v, acceleration]

def cfd(B:int, H: int, f2):
    t = np.linspace(0, B, H)

def center_of_mass(masses, positions):
    
    totalMass = sum(masses)
    x=0
    x = sum(masses[i]*positions[i][0] for i in range(len(masses))) / totalMass
    y = sum(masses[i]*positions[i][1] for i in range(len(masses))) / totalMass

    return x, y

# Init. conditions
acceleration = 0
read = False
masses = []
forces = []
initPos1 = []
iterator = 0
times = []

# Opening init_data
with open("init_data.txt") as file:
   
    for line in file:
        
        if line[0] == "=":
            read = False

        elif line == "Masses:\n" or line == "Forces:\n" or \
            line == "Initial positions:\n" or line == "Initial velocity:\n" or \
            line == "Number of iterations:\n" or line == "Axis limit:\n" or \
            line == "Pause time:\n" or line == "t0 t1:\n":

            read = True
            iterator += 1
            continue
        
        elif read == True and iterator == 1:
            masses.append(float(line))
            continue
        
        elif read == True and iterator == 2:
            forces.append(line)
            continue
        
        elif read == True and iterator == 3:
            temp = line
            index = temp.find(',')
            x = float(temp[1:index])
            y = float(temp[index+1:len(temp)-2])
            initPos1.append([x, y])
            continue

        elif read == True and iterator == 4:
            v_0 = float(line)
            continue

        elif read == True and iterator == 5:
            numberOfIterations = int(line)
            continue

        elif read == True and iterator == 6:
            limit = int(line)
            continue

        elif read == True and iterator == 7:
            pauseTime = float(line)
            continue

        elif read == True and iterator == 8:
            times.append(int(line))
            continue

file.close()

# Preparation for finding position equations
axis =[]
initPosAxis = []

for i, f in enumerate(forces):
    # movement in the axis of...
    axis.append('x' if f[len(f)-2] == 'x' else 'y') 
    
    # pos. in the context of the axis
    initPosAxis.append(initPos1[i][0] if axis[i] == 'x' else initPos1[i][1]) 
    
    # intiger forces
    forces[i] = int(forces[i][0:len(forces[i])-2]) 

data = list(zip(masses, forces, axis, initPosAxis))


# Solution
t = np.linspace(times[0], times[1], numberOfIterations)
positions = []
for i, d in enumerate(data):
    m, f, a, ip = d
    
    acceleration = f/m
    solve = odeint(dSdt, [ip, 0], t)

    tempPos = [s[0] for s in solve]
    temp = tempPos[0]

    positions.append(tempPos)

rows = len(positions)

# Visualisation
exit = False
with open("output.txt", 'w') as file:
    for col in range(numberOfIterations):
        if keyboard.is_pressed('q'): break 
        plt.draw()

        newMasses = []
        newPositions = []

        plt.xlim(-limit, limit)
        plt.ylim(-limit, limit)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        
        for row in range(rows):
            if keyboard.is_pressed('q'): exit = True
            if axis[row] == 'x':
                plt.scatter(positions[row][col], initPos1[row][1], 
                            label=f"Particle {row+1}")
                
                newPositions.append([positions[row][col], initPos1[row][1]])

                if col == numberOfIterations-1:
                    file.write(f"{row+1}. particle coordinates: ({positions[row][col]},{initPos1[row][1]})\n")

            else:
                plt.scatter(initPos1[row][0], positions[row][col], 
                            label=f"Particle {row+1}")
                
                newPositions.append([initPos1[row][0], 
                                     positions[row][col]])
                
                if col == numberOfIterations-1:
                    file.write(f"{row+1}. particle coordinates: ({initPos1[row][0]}, {positions[row][col]}\n")
            
        comX, comY = center_of_mass(masses, newPositions)
        plt.scatter(comX, comY, label="Center of mass")
        plt.legend()
        
        plt.pause(pauseTime)

        if col != numberOfIterations-1: plt.clf()     

        if keyboard.is_pressed('q') or exit == True: break 

    plt.show(block=True)

    file.write(f"\nCenter of mass coordinates: ({comX},{comY})\n")
    file.close()
