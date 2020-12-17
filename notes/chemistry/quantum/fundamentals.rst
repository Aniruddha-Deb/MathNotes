Fundamentals
================================

Why Quantum Chemistry
#######################

This is a good question, which doesn't get enough attention. For most of us, 
we have to learn quantum mechanics because it's in the course curriculum, or 
because "classical mechanics fails at the microscopic level" or some BS like that.
`Chapter 1 of the Feynman Lectures, Vol.3 <https://www.feynmanlectures.caltech.edu/III_01.html>`_
explains this amazingly, and if you're still not satisfied and want a more 
hardcore explanation, check out the afterword of `Griffiths' Introduction to 
Quantum Mechanics <https://www.fisica.net/mecanica-quantica/Griffiths%20-%20Introduction%20to%20quantum%20mechanics.pdf>`_. 

In short, Quantum mechanics primarily arises to explain the behaviour of things 
that cannot be measured without disturbing their state. Like the electron or 
photon in a double slit experiment, trying to measure their position would 
cause a transfer of energy, however infinitesimal. This would disturb them from
the state that they were in, which would defeat the purpose of the measurement.

How to go Quantum
#####################

Explaining the behaviour of things that cannot be measured sounds easier than
it looks. If we have a box and a ball, and we need to describe the position of
the ball with reference to the box, for simplicity's sake we have two options:

1. The ball is in the box
2. The ball is outside the box i.e. it is not in the box

Since this is quantum chemistry, we cannot measure the location of the ball. 
We then use probabilities to describe the location of the ball: if :math:`p_1^2` is the 
probability of the ball being in the box and :math:`p_2^2` is the probability of the 
ball being outside the box, then the position of the ball is defined by something
we call a `wavefunction`. The wavefunction in this case would be

.. math:: \psi = p_1\ket{1} + p_2\ket{2}

Here we have described the simplest quantum system: A `2 state quantum system <https://en.wikipedia.org/wiki/Two-state_quantum_system>`_.
Don't be surprised by the :math:`\ket{1}` and :math:`\ket{2}` notations: they
merely represent the different states the system can take, and we'll go into 
more detail on them in a second. If they make you 
uncomfortable (they made me :P), you can think of them as the unit vectors 
:math:`\hat i` and :math:`\hat j`. The wavefunction would then define a vector
which was inclined at :math:`\arctan \frac{p_2}{p_1}` to the x-axis.

Deriving Probability from the wavefunction
###############################################################

You must have noticed that rather than putting the probability directly
in the wavefunction, we took the square root of probability. This is called
the `Probability Amplitude <https://en.wikipedia.org/wiki/Probability_amplitude>`_,
and is by definition. According to the born interpretation of the wavefunction
:math:`|\psi|^2` gives the probability of an event occuring. In this case, 
the probability of state 1 is :math:`p_1^2` and that of state 2 is :math:`p_2^2`. A few
things to note:

1. The probability amplitude can also be complex. In this case, the probability
   is the absolute value of the wavefunction, given by :math:`\psi^*\psi`, :math:`\psi^*`
   is the complex conjugate of :math:`\psi`.
2. The total probability of the wavefunction should be 1. In this case, that implies
   :math:`p_1^2 + p_2^2 = 1`. In general, for a given wavefunction psi, it's 
   square integral :math:`\int \psi^* \psi d\tau` should be 1 over it's entire
   domain.

Observables, Operators and their Notations
###################################################

In quantum mechanics, an Observable is a dynamic variable of a system that can 
be experimentally measured, for example position, momentum and kinetic energy.
An observable quantity is generally enclosed in a 'ket', which is the bracket-like
thing we used to denote states of the ball earlier. However, I won't be using 
kets and further formalism in these notes, except maybe in the Mathematics part.

Every observable quantity has an operator associated with it. Thus, the position
of a particle :math:`\ket{x}` has an operator :math:`\hat{x}` associated with
it. The operator defines an operation to be performed on an observable. 
For example, the operator :math:`\hat x` is defined as

.. math:: \hat x = x

which is a simple multiplication operation. The momentum operator, however,
is defined as follows:

.. math:: \hat p = -i \hbar \frac{\partial}{\partial x}

Note that in multiple dimensions, :math:`\frac{\partial}{\partial x}` becomes 
:math:`\nabla`. 

One point of confusion is the notation :math:`\hat p^2`: this does not mean 
that we are squaring the operator, but that we are applying the operator twice
in succession. If we take an example, 

.. math:: 
	
	\begin{align}
	\hat p^2 U &= \left(-i\hbar \frac{\partial }{\partial x}\right) \left( -i\hbar \frac{\partial U}{\partial x}\right) \\
	\hat p^2 U &= -\hbar^2 \frac{\partial^2 U}{\partial x^2}
	\end{align}

An interesting thing to note is that using these two fundamental operators 
(momentum and position), we can define all of the operators related to classical
mechanics as a function of :math:`\hat p` and :math:`\hat x`. As an example, kinetic
energy is 

.. math:: \hat K = \frac{\hat p^2}{2m} = \frac{-\hbar^2}{2m}\nabla^2

Operators have a few important properties, which are discussed in the 
next section

Properties of Operators
##################################################

Eigenvalues and Eigenfunctions
**************************************************
If for an operator :math:`\hat X`, the following equation holds:

.. math:: \hat X f = K f

then :math:`f` is called an **eigenfunction** of :math:`\hat X` and :math:`K` is
called an **eigenvalue** of :math:`\hat X`. The terminology derives from linear
algebra (eigenvectors and eigenvalues), and we'll explore the mathematics in the
next section.

Hermiticity
**************************************************
All the quantum mechanical operators corresponding to observables are called
`hermitian`: a hermitian operator :math:`\hat X` is one for which the following 
is true:

.. math:: \int \psi_j^*\ \hat X\ \psi_i\ d\tau = \left\{ \int \psi_i^*\ \hat X\ \psi_j\ d\tau \right\}^*

This will be covered in some more detail in the math section, but for now, there
are two important properties of hermitian operators:

1. The eigenvalues of hermitian operators are real
2. The eigenfunctions of hermitian operators are orthogonal

The second point will be explained in greater detail in the Mathematics section.
