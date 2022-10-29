# resources-optimizer

Given a matrix $M_{n \times m} = [m_{ij}]$, representing the map of a city with possibly certain resources $R = \{1,\ldots,k}$ (*e.g.*, 1 = *fitness gym*, 2 = *boxing gym*, 3 = *dance school* etc. and 0 = *no resource*) in a certain position $(i,j)$, *i.e.*, $m_{ij} \in \\{0\\} \cup \ R$, this script allows to compute a score matrix $S_{n \times m} = [s_{ij}]$ where $s_{ij}$ represents the score of position $(i,j)$ based on a certain metric.

Generically, it is possible to define such a metric as 

$$s_{ij} = \frac{1}{1+ f_a(\\{d(i,j,r)_{r \in R}\\})}$$

,where $f_a$ is an aggregation function (*e.g.*, sum) and $d(i,j,r)$ is a certain notion of distance between position $(i,j)$ and resource $r$ (*e.g.*, the distance between $(i,j)$ and the closest $r$), thus $\\{d(i,j,r)_{r \in R}\\}$ represents the set of those distances with respect to $r \in R$.

Here is an example of visualization of the output of the script with $k = 3$ and $n = m = 50$ (see comments in the code to see definitions of the metrics) and $M$ generated uniformly at random (*i.e.*, each possible value of $m_{ij}$ is equally likely):

