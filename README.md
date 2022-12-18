# TSP-in-the-plane-with-few-interior-points

Let P be a set of points in the plane. The TSP for P is the tour of minimum length that goes through all the points of P. It is known that when the set of points is in convex position (each
point is in the boundary of the convex hull of P), then the boundary of the convex hull of P gives the optimal tour. Deineko et al. have shown that when there are few interior points, the problem can be solved via dynamic programming. The running time is exponential in the number of interior points. See https://doi.org/10.1016/j.orl.2005.01.002; a local copy is at https://www.fmf.uni-lj.si/~cabello/files/AunJTz3SWNPLqvswTz3SWNPLqvsw/. Program this and check the length for a few scenarios. For example, if the points in the outside are vertices of a regular polygon, what is the worst position for the interior points? And if the exterior points are on the boundary of a circle but not equidistributed?