
# CENTER OF MASS VISUALISATION
![App Screenshot](https://media.istockphoto.com/id/618420050/vector/justice-scale-vector-illustration.jpg?s=612x612&w=0&k=20&c=uKT5agD87TJa_92DOoNFVS_FhuXu-73vmar-H8eXL8E=)

source: https://www.istockphoto.com/pl/ilustracje/drawing-of-libra-scales-star-sign



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
![App Screenshot]([data:image/png;base64,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](https://i0.wp.com/www.learncram.com/wp-content/uploads/2020/09/center-of-mass-1.png?resize=325%2C215&ssl=1))

source: http://hyperphysics.phy-astr.gsu.edu/hbase/cm.html

### b) Dynamic equation of motion
In the book I gave as a source, you can find an analytical solution to this problem, but I wanted to do it numerically. So I used Newton's second law of motion.

![App Screenshot](https://drive.google.com/uc?id=1k0us7t1PfIT6dYWKgwTy1QHFN40fF6DI)

The acceleration is the second derivative of the position, so I changed a to the second derivative. 

Force is the force that acts on the selected particle in the plane.

The solution is the function x(t).

This is the answer to how my program works. It solves this second derivative, calculates the positions of the particles based on the calculated function, and from this it calculates the position of the center of mass.



## III. Installation
The program is a simulation, not a library, so you can download it right away and use it. 
## IV. Instructions
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
