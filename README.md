
# CENTER OF MASS VISUALISATION
<div align="center">
  
  <img src="https://drive.google.com/uc?id=1LM0BSiAZYsSIHtTdyukWAKB6zuCyq-bm" alt="Logo"/>

  
  <img src="https://media.istockphoto.com/id/618420050/vector/justice-scale-vector-illustration.jpg?s=612x612&w=0&k=20&c=uKT5agD87TJa_92DOoNFVS_FhuXu-73vmar-H8eXL8E=" alt="Libra"/>
  
  source: https://www.istockphoto.com/pl/ilustracje/drawing-of-libra-scales-star-sign
</div>

## I. Info

This project visualizes the motion of particles in one Cartesian axis and the center of mass in both Cartesian axes. 

#### The program includes:

🔹 masses of the particles,

🔹 constant forces that interact with particles,

🔹 initial positions of the particles,

🔹 initial velocity,

🔹 number of iterations,

🔹 time of the process.

Initial data is stored in init_data.txt. Output can be found in output.txt file.

#### If you want to skip physics stuff and math explanation of the topic than skip to installation.
## II. Theoretical explanation and problem
The problem is to find final coordinates of the center of the mass after some seconds.

### a) Center of mass equation
If we want to find coordinates of the center of the mass we would use this equation:

![Center of mass equation](https://i0.wp.com/www.learncram.com/wp-content/uploads/2020/09/center-of-mass-1.png?resize=325%2C215&ssl=1)


source: http://hyperphysics.phy-astr.gsu.edu/hbase/cm.html

### b) Dynamic equation of motion
In the book I gave as a source, you can find an analytical solution to this problem, but I wanted to do it numerically. So I used Newton's second law of motion.

![II Newtons law](https://drive.google.com/uc?id=1-OR6R0zPiZmErW_H5PS3TiAzb2lEtbaH)

The acceleration is the second derivative of the position, so I changed a to the second derivative. 

Force is the force that acts on the selected particle in the plane.

The solution is the function x(t).

This is the answer to how my program works. It solves this second derivative, calculates the positions of the particles based on the calculated function, and from this it calculates the position of the center of mass.



## III. Installation
The program is a simulation, not a library, so you can download it right away and use it. 
## IV. Instructions

#### PRESS 'Q' TO EXIT

#### If you just want to see the solution to the problem and its visualization:

🔹 enable the executable file

🔹 view the visualization,

🔹 run output.txt. There you can see the final position of the particles and the center of mass.

#### If you want to play with the simulation:

🔹 boot up init_data.txt,

🔹 read the rules,

🔹 stick to the rules!

🔹 add/remove particles,

🔹 save init_data.txt,

🔹 run executable file and after visualization output.txt.

![Screenshot of program](https://drive.google.com/uc?id=1Ej1GQitaxZkxG98wvgvfU-1oyumXhCWW)
