# Homogeneous coordinates

#### **Overview**

Geometric transformations play a key role in computer graphics and related fields. Transformations that are linear can be represented by a single matrix. On the hand, non-linear transformations such as the affine transformation, can still be partially represented by matrices. Their mathematical notation, however, can become cumbersome when expressing inverses and combinations of multiple transformations. Luckily, there is a geometric space where transformations are always linear, which means that we can always represent them as a (single) matrix. This geometry is called projective geometry and we can convert vectors and transformations from Cartesian coordinates to Projective coordinates (i.e., homogeneous coordinates) and back. 

#### **Two-dimensional transformations in homogeneous coordinates** 

The vector ${\bf x} = (x,y)^\mathsf{T}$ can be represented in homogeneous coordinates by the vector $\tilde{\bf x} = (x,y,\lambda)^\mathsf{T}$, with $\lambda \neq 0$, i.e.: 
$$
\begin{align}
		\begin{bmatrix}
		x \\
		y
	\end{bmatrix}	
 	\rightarrow
		\begin{bmatrix}
		x \\
		y \\
		\lambda
	\end{bmatrix}.	
\end{align}
$$
This is still a 2-D point but it is now represented by 3 instead of 2 coordinates. Here, all we are doing to convert from Cartesian coordinates to homogeneous coordinates is to augment the original vector by adding $\lambda\neq0$ as an extra coordinate. 

To convert homogenous coordinates back to Cartesian, we need only to divide the homogeneous coordinates as follows: 
$$
\begin{align}
		\begin{bmatrix}
		x \\
		y \\
		\lambda
	\end{bmatrix}	
 	\rightarrow
		\begin{bmatrix}
		x/\lambda \\
		y/\lambda
	\end{bmatrix}.	
\end{align}
$$
The simplest and most common choice is to set $\lambda=1$, i.e.: 
$$
\begin{align}
		\begin{bmatrix}
		x \\
		y
	\end{bmatrix}	
 	\rightarrow
		\begin{bmatrix}
		x \\
		y \\
		1
	\end{bmatrix}.	
\end{align}
$$
If $\lambda=1$, then most conversions are straightforward, 

Because, we augmented the vectors, we must also augment the transformations. The following are 2-D transformations in homogeneous coordinates: 

Scaling:
$$
\begin{align}
	S = 
	\begin{bmatrix}
		s_x & 0 & 0 \\
		0 & s_y & 0 \\
		0 & 0 & 1 \\
	\end{bmatrix}.
\end{align}
$$





Rotation:
$$
\begin{align}
	R = 
	\begin{bmatrix}
		\cos\theta & -\sin\theta & 0 \\
		\sin\theta & \cos\theta & 0 \\
		0 & 0 & 1 
	\end{bmatrix}.
\end{align}
$$

And most importantly, we can now also represent translation as a matrix, which is something that we could not do in Cartesian coordinates. The 2-D translation matrix is given by: 
$$
\begin{align}
	T = 
	\begin{bmatrix}
		1 & 0 & t_x \\
		0 & 1 & t_y \\
		0 & 0 & 1 
	\end{bmatrix}.
\end{align}
$$

The affine transformation also has its equivalent in homogeneous coordinates, i.e.: 
$$
\begin{align}
	A = 
	\begin{bmatrix}
		a_1 & a_2 & t_x \\
		a_3 & a_4 & t_y \\
		0 & 0 & 1 \\
	\end{bmatrix}.
\end{align}
$$

Because all transformations in projective geometry are linear, we can represent compositions and inverses with a concise notation. For example, the transformation: 
$$
\begin{align}
	{\bf x}^\prime = SR\,{\bf x} + {\bf t}.
\end{align}
$$

can be written in homogeneous coordinates as: 
$$
\begin{align}
	\tilde{\bf x}^\prime = T_hS_hR_h\,\tilde{\bf x}, 
	\label{homogeneousComposition}
\end{align}
$$

and its inverse would be simply: 
$$
\begin{align}
	\tilde{\bf x} &= \left(T_h\,S_h\,R_h\right)^{-1}\,\tilde{\bf x}^\prime\notag \\ 
 &= R_h^{-1}\,S_h^{-1}\,T_h^{-1}\,\tilde{\bf x}^\prime. 
	\label{homogeneousCompositionInverse}
\end{align}
$$

In Equation $\ref{homogeneousComposition}$, the subscript $h$ is being used to indicate the homogeneous version of the transformation. However, we do not usually explicitly differentiate the transformations.  

In higher dimensions, homogeneous coordinates are analogous to the 2-D case, i.e., just add an extra coordinate to the original vector. In the 3-D case, the homogeneous representation of a vector is: 
$$
\tilde{\bf x} = 
\begin{bmatrix}
	x\\
	y\\
	z\\
	1
\end{bmatrix}
$$

The translation matrix is:
$$
\begin{align}
	T = 
	\begin{bmatrix}
		1 & 0 & 0 & t_x \\
		0 & 1 & 0 & t_y \\
		0 & 0 & 1 & t_z \\
		0 & 0 & 0 & 1 \\
	\end{bmatrix}.
\end{align}
$$





The scaling matrix is:
$$
\begin{align}
	S = 
	\begin{bmatrix}
		s_x & 0 & 0 & 0\\
		0 & s_y & 0 & 0 \\
		0 &  0 & s_z & 0\\
		0 & 0 & 0 & 1 \\
	\end{bmatrix}.
\end{align}
$$

And a transformation $\tilde{\bf x}^\prime = S\,T\,\tilde{\bf x}$ is:

$$
\begin{align}
\begin{bmatrix}
	x^\prime\\
	y^\prime\\
	z^\prime\\
	1
\end{bmatrix} =
	\begin{bmatrix}
		s_x & 0 & 0 & 0\\
		0 & s_y & 0 & 0 \\
		0 &  0 & s_z & 0\\
		0 & 0 & 0 & 1 \\
	\end{bmatrix}
		\begin{bmatrix}
		1 & 0 & 0 & t_x \\
		0 & 1 & 0 & t_y \\
		0 & 0 & 1 & t_z \\
		0 & 0 & 0 & 1 \\
	\end{bmatrix}
	\begin{bmatrix}
	x\\
	y\\
	z\\
	1
\end{bmatrix}
\end{align}
$$



$$
\begin{align}
\begin{bmatrix}
	x^\prime\\
	y^\prime\\
	z^\prime\\
	%1
\end{bmatrix} =
	\begin{bmatrix}
		a_{1,1} & a_{1,2} & a_{1,3} & t_x\\
		a_{2,1} & a_{2,2} & a_{2,3} & t_y \\
		a_{3,1} &  a_{3,2}& a_{2,3} & t_z\\
		%0 & 0 & 0 & 1 \\
	\end{bmatrix}_{3\times4}

	\begin{bmatrix}
	x\\
	y\\
	z\\
	1
\end{bmatrix}_{4\times1}
\end{align}
$$

###### 





$$
\tilde{\bf x}^\prime = \left[
		A \,\,\,\,\,{\bf t}\right]
	\,\tilde{\bf x}
= A\tilde{\bf x} + {\bf t}
$$

###### 
