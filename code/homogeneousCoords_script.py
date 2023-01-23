# Generated with SMOP  0.41-beta
#from libsmop import *
# homogeneousCoords_script.m

## Homogeneous coordinates 
# 
# 
# Linear geometric transformations can be written as concise equations using 
# matrix multiplication. For instance, let the following transformation maps a 
# vector ${\bf x}$ onto a vector ${\bf x}^\prime$: 
# 
# $${\bf x}^\prime = SR\,{\bf x},$$
# 
# where $S$ is a scaling matrix and $R$ is a rotation matrix. $S$ and $R$ are 
# linear transformations, and so is the composition $SR$. 
# 
# This compact form of the transformation matrix simplifies both its computation 
# and notation. For example, we can change the order in which the transformations 
# are applied by simply changing the order of multiplication, i.e.:  
# 
# $${\bf x}^{\prime\prime} = RS\,{\bf x},$$
# 
# or we can calculate the inverse transformation directly, i.e., the inverse 
# of ${\bf x}^\prime = SR\,{\bf x}$ can be written as: 
# 
# ${\bf x} = (SR)^{-1}\,{\bf x}^\prime = (R^{-1}S^{-1})\,{\bf x}^\prime$.
# 
# However, this compact notation breaks if the transformation includes a translation 
# (i.e., for affine transformations). An affine transformation includes a linear 
# component and a translation component and is written as follows:
# 
# ${\bf x}^\prime = A{\bf x} + {\bf t} $.  
# 
# In 2-D, the matrix form of the affine transformation can be written explicitly 
# as: 
# 
# $$\left[\begin{array}{c}		x^\prime \\		y^\prime\end{array}\right] = \left[\begin{array}{c}		
# a_1 & a_2 \\		a_3 & a_4\end{array}\right]\left[\begin{array}{c}    x \\        
# y\end{array}\right]+\left[\begin{array}{c}    t_x \\        t_y\end{array}\right]$$
# 
# Now, the transformation notation combines a multiplication followed by a addition. 
# It can no longer be represented by a single matrix or by multiplications only 
# (i.e., we have to mix multiplication and addition).  
## Example:

# Scaling
S=concat([[2,0],[0,1]])
# homogeneousCoords_script.m:43
# Rotation
theta=pi / 8
# homogeneousCoords_script.m:47
R=concat([[cos(theta),- sin(theta)],[sin(theta),cos(theta)]])
# homogeneousCoords_script.m:48
# Translation part of the affine transformation
t=concat([[2],[3]])
# homogeneousCoords_script.m:52
## The shape to be transformed
# The rectangle given by four vertices

px=concat([0,4,4,0])
# homogeneousCoords_script.m:57

py=concat([0,0,2,2])
# homogeneousCoords_script.m:58

disp('Input shape')
X=concat([[px],[py]])
# homogeneousCoords_script.m:60
## Apply transformation to shape
# The transformation that we will apply to the rectangle is a Rotation followed 
# by a Scaling and then a Translation, i.e.: 
# 
# ${\bf x}^\prime = (SR)\,{\bf x} + {\bf t}$.

disp('Transformed shape')
X_p=dot((dot(S,R)),X) + t
# homogeneousCoords_script.m:68
## Display shapes

figure
hold('on')
axis(concat([- 2,10,- 2,7]))
# Repeating the first vertex to close polygon lines
plot(concat([X(1,arange()),X(1,1)]),concat([X(2,arange()),X(2,1)]),'b-','linewidth',4)
plot(concat([X(1,arange()),X(1,1)]),concat([X(2,arange()),X(2,1)]),'o','MarkerSize',12,'MarkerFaceColor','b')
xlabel('x','FontSize',30)
ylabel('y','FontSize',30)
set(gca,'fontsize',18)
set(gcf,'color','w')
title('Original (blue) and Transformed (red) Shapes ')
# Show the transformed points
plt=plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'r-','linewidth',4)
# homogeneousCoords_script.m:83
plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','r')
# Plot transformed shape transparent
plt.Color[4]=0.5
# homogeneousCoords_script.m:86
grid('on')
## 
# To see how the inclusion of the translation further complicates the matrix 
# notation, let us calculate the inverse of the affine transformation in the previous 
# equation. The inverse is given by:  
# 
# ${\bf x} = (SR)^{-1}\left({\bf x}^\prime - {\bf t}\right) = R^{-1}S^{-1}\left({\bf 
# x}^\prime - {\bf t}\right) = R^{-1}S^{-1}{\bf x}^\prime - R^{-1}S^{-1}{\bf t} 
# $.
# 
# We can use this equation to go from the red shape back to the blue shape. 
## Example using the inverse affine transformation
# In this example, we do exactly that but we will plot the transformed shape 
# in green color.

# Input shape is the transformed shape from the previous example
disp('Input shape')
X_p
figure
axis(concat([- 2,10,- 2,7]))
hold('on')
# Show the transformed points
plt=plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'r-','linewidth',4)
# homogeneousCoords_script.m:110
plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','r')
# Plot transformed shape transparent
#plt.Color(4) = 0.5;
grid('on')
##
disp('This is the shape resulting from the inverse affine transformation')
# Calculate the shape produced by the inverse affine
Xi=dot(dot(inv(R),inv(S)),X_p) - dot(dot(inv(R),inv(S)),t)
# homogeneousCoords_script.m:118
hold('on')
# Show the transformed points
plot(concat([Xi(1,arange()),Xi(1,1)]),concat([Xi(2,arange()),Xi(2,1)]),'g-','linewidth',4)
plot(concat([Xi(1,arange()),Xi(1,1)]),concat([Xi(2,arange()),Xi(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','g')
# Plot transformed shape transparent
grid('on')
## Homogeneous coordinates
# We can make the matrix notation of affine transformations more concise by 
# using *Homogeneous coordinates* instead of Cartesian coordinates. This is done 
# by augmenting the Cartesian coordinates with an extra non-zero coordinate value, 
# which is usually chosen to be 1.
# 
# To convert the original points from Cartesian to Homogeneous coordinates, 
# we simply add the original vector by adding 1 as an extra coordinate (i.e., 
# dimension), i.e.: 
# 
# $$\left[\begin{array}{c}		x \\		y \end{array}\right] \rightarrow\lambda\left[\begin{array}{c}		
# x \\		y \\                1\end{array}\right]$$
# 
# This is still a 2-D point but it is now represented by 3 instead of 2 coordinates. 
# Here, all we are doing to convert from Cartesian coordinates to homogeneous 
# coordinates is to augment the original vector by adding $\lambda\neq0$ as an 
# extra coordinate. 
# 
# To convert homogenous coordinates back to Cartesian, we need only to divide 
# the homogeneous coordinates as follows: 
# 
# $$\lambda\left[\begin{array}{c}		x \\		y \\                1\end{array}\right]\rightarrow\left[\begin{array}{c}		
# x / \lambda\\		y / \lambda\end{array}\right] $$
# 
# The simplest and most common choice is to set $\lambda=1$, i.e.: 
# 
# $\left[\begin{array}{c}		x \\		y \end{array}\right] \rightarrow\left[\begin{array}{c}		
# x \\		y \\                1\end{array}\right]$.
# 
# Because, we augmented the vectors, we must also augment the transformation 
# matrices. 
## The affine transformation in homogeneous coordinates
# Let us now repeat our previous examples of affine transformations  but this 
# time using homogeneous coordinates instead of Cartesian. The 2-D affine transformation 
# in homogeneous coordinates is given by: 
# 
# $\left[\begin{array}{c}		x^\prime \\		y^\prime \\                 1\end{array}\right] 
# = \left[\begin{array}{c}		a_1 & a_2  & t_x\\		a_3 & a_4  & t_y\\                  
# 0  &   0    &   1\end{array}\right]\left[\begin{array}{c}    x \\        y \\    
# 1\end{array}\right]$.
# 
# This single matrix in homogeneous coordinates incorporate both the linear 
# part of the affine and its translation. In homogeneous coordinates the scaling 
# matrix is: 
# 
# $S_h = \left[\begin{array}{c}		s_x & 0  &     0\\		0 & s_y  &  0\\                  
# 0  &   0    &   1\end{array}\right]$,
# 
# and the rotation is given by: 
# 
# $R_h= \left[\begin{array}{c}		\cos\theta & -\sin\theta & 0 \\		\sin\theta 
# & \cos\theta & 0 \\		0 & 0 & 1 \end{array}\right]$.
# 
# Most importantly, we can now also represent the translation as a matrix, which 
# is something that we could not do in Cartesian coordinates. The 2-D *translation 
# matrix* is given by: 
# 
# $T_h = \left[\begin{array}{c}		1 & 0 & t_x \\		0 & 1 & t_y \\		0 & 0 & 1 \end{array}\right]$.
# 
# In homogeneous coordinates, we can represent compositions and inverses of 
# transformations concisely. For example, the transformation: 
# 
# $	{\bf x}^\prime = SR\,{\bf x} + {\bf t}$,
# 
# can be written in homogeneous coordinates as:
# 
# $	\tilde{\bf x}^\prime = T_hS_hR_h\,\tilde{\bf x}$.
# 
# Its inverse would be simply: 
# 
# $	\tilde{\bf x} = \left(T_h\,S_h\,R_h\right)^{-1}\,\tilde{\bf x}^\prime = 
# R_h^{-1}\,S_h^{-1}\,T_h^{-1}\,\tilde{\bf x}^\prime $.
# 
# In these equations, the subscript $h$ is being used to indicate the homogeneous 
# version of the transformation. However, we do not usually explicitly differentiate 
# the transformations.  
## Example:

# Scaling
Sh=concat([[2,0,0],[0,1,0],[0,0,1]])
# homogeneousCoords_script.m:205
# Rotation
theta=pi / 8
# homogeneousCoords_script.m:210
Rh=concat([[cos(theta),- sin(theta),0],[sin(theta),cos(theta),0],[0,0,1]])
# homogeneousCoords_script.m:211
# Translation part of the affine transformation
Th=concat([[1,0,2],[0,1,3],[0,0,1]])
# homogeneousCoords_script.m:216
## The shape to be transformed
# Rectangle given by four vertices

px=concat([0,4,4,0])
# homogeneousCoords_script.m:222

py=concat([0,0,2,2])
# homogeneousCoords_script.m:223

disp('Input shape')
X=concat([[px],[py]])
# homogeneousCoords_script.m:225
Xh=concat([[px],[py],[ones(1,size(px,2))]])
# homogeneousCoords_script.m:226
##
# Transform the shape
disp('Transformed shape')
X_p=dot((dot(dot(Th,Sh),Rh)),Xh)
# homogeneousCoords_script.m:230
##
# Convert from homogeneous to cartesian coordinates
Xc=concat([[X_p(1,arange()) / X_p(3,arange())],[X_p(2,arange()) / X_p(3,arange())]])
# homogeneousCoords_script.m:233
## Display shapes

figure
hold('on')
axis(concat([- 2,10,- 2,7]))
# Repeating the first vertex to close polygon lines
plot(concat([X(1,arange()),X(1,1)]),concat([X(2,arange()),X(2,1)]),'b-','linewidth',4)
plot(concat([X(1,arange()),X(1,1)]),concat([X(2,arange()),X(2,1)]),'o','MarkerSize',12,'MarkerFaceColor','b')
xlabel('x','FontSize',30)
ylabel('y','FontSize',30)
set(gca,'fontsize',18)
set(gcf,'color','w')
title('Original (blue) and Transformed (red) Shapes ')
# Show the transformed points
plt=plot(concat([Xc(1,arange()),Xc(1,1)]),concat([Xc(2,arange()),Xc(2,1)]),'r-','linewidth',4)
# homogeneousCoords_script.m:248
plot(concat([Xc(1,arange()),Xc(1,1)]),concat([Xc(2,arange()),Xc(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','r')
# Plot transformed shape transparent
plt.Color[4]=0.5
# homogeneousCoords_script.m:251
grid('on')
## Example using the inverse affine transformation
# The transformed shape is plotted in green color.

# Input shape is the transformed shape from the previous example
disp('Input shape')
X_p
figure
axis(concat([- 2,10,- 2,7]))
hold('on')
# Show the transformed points
plt=plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'r-','linewidth',4)
# homogeneousCoords_script.m:264
plot(concat([X_p(1,arange()),X_p(1,1)]),concat([X_p(2,arange()),X_p(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','r')
# Plot transformed shape transparent
#plt.Color(4) = 0.5;
grid('on')
## 
# Recall that the inverse of the transformation is:
# 
# $	\tilde{\bf x} = \left(T_h\,S_h\,R_h\right)^{-1}\,\tilde{\bf x}^\prime = 
# R_h^{-1}\,S_h^{-1}\,T_h^{-1}\,\tilde{\bf x}^\prime $.

disp('This is the shape resulting from the inverse affine transformation')
# Calculate the shape produced by the inverse affine
Xi=dot(dot(dot(inv(Rh),inv(Sh)),inv(Th)),X_p)
# homogeneousCoords_script.m:277
# Convert from homogeneous to cartesian coordinates
Xc=concat([[Xi(1,arange()) / Xi(3,arange())],[Xi(2,arange()) / Xi(3,arange())]])
# homogeneousCoords_script.m:280
##

hold('on')
# Show the transformed points
plot(concat([Xc(1,arange()),Xc(1,1)]),concat([Xc(2,arange()),Xc(2,1)]),'g-','linewidth',4)
plot(concat([Xc(1,arange()),Xc(1,1)]),concat([Xc(2,arange()),Xc(2,1)]),'o','MarkerSize',8,'MarkerFaceColor','g')
# Plot transformed shape transparent
grid('on')