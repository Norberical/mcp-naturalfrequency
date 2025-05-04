$$
\lambda^4 = \frac{\rho A}{EI}\omega^2 = \frac{\varepsilon^4}{l^4}
$$

$$
\begin{align*}
\phi(x) &= A \cosh(\lambda x) + B \sinh(\lambda x) + C \cos(\lambda x) + D \sin(\lambda x) 
\\
\phi^{\prime}(x) &= A \lambda \sinh(\lambda x) + B \lambda \cosh(\lambda x) - C \lambda \sin(\lambda x) + D \lambda \cos(\lambda x) 
\\
\phi^{\prime\prime}(x) &= A \lambda^2 \cosh(\lambda x) + B \lambda^2 \sinh(\lambda x) - C \lambda^2 \cos(\lambda x) - D \lambda^2 \sin(\lambda x) 
\\
\phi^{\prime\prime\prime}(x) &= A \lambda^3 \sinh(\lambda x) + B \lambda^3 \cosh(\lambda x) + C \lambda^3 \sin(\lambda x) - D \lambda^3 \cos(\lambda x)
%\\
%\phi^{\prime\prime\prime\prime}(x) &= A \lambda^4 \cosh(\lambda x) + B \lambda^4 \sinh(\lambda x) + C \lambda^4 \cos(\lambda x) + D \lambda^4 \sin(\lambda x)
\end{align*}
$$

$$
\begin{align*}
w(x,t) &= \phi(x) T(t) 
\\
\varphi(x,t) &= w^{\prime}(x,t) = \phi^{\prime}(x) T(t) 
\\
\kappa(x,t) = -\frac{M(x,t)}{EI} &= w^{\prime\prime}(x,t) = \phi^{\prime\prime}(x) T(t) 
\\
-\frac{V(x,t)}{EI} &= w^{\prime\prime\prime}(x,t) = \phi^{\prime\prime\prime}(x) T(t) 
\end{align*}
$$

$$
\begin{align*}
w(0,t) &= w_0 T(t) & w(l,t) &= w_1 T(t) \\
\varphi(0,t) &= \varphi_0 T(t) & \varphi(l,t) &= \varphi_1 T(t) \\
M(0,t) &= M_0 T(t) = -c_0 \varphi_0 T(t) & M(l,t) &= M_1 T(t) = -c_1 \varphi_1 T(t) \\
V(0,t) &= V_0 T(t) = -k_0 w_0 T(t) & V(l,t) &= V_1 T(t) = - k_1 w_1T(t)
\end{align*}
$$

$$
\begin{align*}
V_0 + k_0w_0 &= -EI\lambda^3[B - D] + k_0[A + C] \\
             &= + k_0A -EI\lambda^3B + k_0C + EI\lambda^3D = 0\\
\end{align*}
$$

$$
\begin{align*}
M_0 + c_0 \varphi_0 &= -EI\lambda[A - C] + c_0 [B + D] \\
                    &= -EI\lambda A + c_0 B + EI\lambda C + c_0 D = 0 \\
\end{align*}
$$

$$
\begin{align*}
V_1 + k_1w_1 =& -EI\lambda^3[A  \sh(\lambda l) + B \ch(\lambda l) + C \sin(\lambda l) - D \cos(\lambda l)] \\
             &+ k_1 [A \ch(\lambda l) + B \sh(\lambda l) + C \cos(\lambda l) + D \sin(\lambda l) ]\\
             =& [-EI\lambda^3\sh(\lambda l) + k_1 \ch(\lambda l)] A + \\
              & [-EI\lambda^3\ch(\lambda l) + k_1 \sh(\lambda l)] B + \\
              & [-EI\lambda^3\sin(\lambda l) + k_1 \cos(\lambda l)] C + \\
              & [+EI\lambda^3\cos(\lambda l) + k_1 \sin(\lambda l)] D = 0\\
\end{align*}
$$

$$
\begin{align*}
M_1 + c_1\varphi_1 =& -EI\lambda^2[A  \ch(\lambda l) + B \sh(\lambda l) - C \cos(\lambda l) - D \sin(\lambda l)] \\
             &+ k_1 \lambda [A \sh(\lambda l) + B \ch(\lambda l) - C \sin(\lambda l) + D \cos(\lambda l) ]\\
             =& [-EI\lambda^2\ch(\lambda l) + k_1 \lambda \sh(\lambda l)] A + \\
              & [-EI\lambda^2\sh(\lambda l) + k_1 \lambda \ch(\lambda l)] B + \\
              & [+EI\lambda^2\cos(\lambda l) - k_1 \lambda \sin(\lambda l)] C + \\
              & [+EI\lambda^2\sin(\lambda l) + k_1 \lambda \cos(\lambda l)] D = 0\\
\end{align*}
$$

$$
\begin{align*}
\begin{bmatrix}
    k_0 & -EI\lambda^3 & k_0 & EI\lambda^3 \\
    -EI\lambda & c_0 & EI\lambda & c_0 \\
    -EI\lambda^3\sh(\lambda l) + k_1 \ch(\lambda l) & -EI\lambda^3\ch(\lambda l) + k_1 \sh(\lambda l) & -EI\lambda^3\sin(\lambda l) + k_1 \cos(\lambda l) & EI\lambda^3\cos(\lambda l) + k_1 \sin(\lambda l) \\
    -EI\lambda\ch(\lambda l) + k_1 \sh(\lambda l) & -EI\lambda\sh(\lambda l) + k_1 \ch(\lambda l) & EI\lambda\cos(\lambda l) - k_1 \sin(\lambda l) & EI\lambda\sin(\lambda l) + k_1 \cos(\lambda l)
\end{bmatrix} \cdot 
\begin{bmatrix}
    A \\ B \\ C \\ D
\end{bmatrix} = 
\begin{bmatrix}
    0 \\ 0 \\ 0 \\ 0
\end{bmatrix}
\end{align*}
$$

$$
\begin{align*}
\begin{bmatrix}
    \frac{k_0}{EI} & -\lambda^3 & \frac{k_0}{EI} & \lambda^3 \\
    -\lambda & \frac{c_0}{EI} & \lambda & \frac{c_0}{EI} \\
    -\lambda^3\sh(\lambda l) + \frac{k_1}{EI} \ch(\lambda l) & -\lambda^3\ch(\lambda l) + \frac{k_1}{EI} \sh(\lambda l) & -\lambda^3\sin(\lambda l) + \frac{k_1}{EI} \cos(\lambda l) & \lambda^3\cos(\lambda l) + \frac{k_1}{EI} \sin(\lambda l) \\
    -\lambda\ch(\lambda l) + \frac{c_1}{EI} \sh(\lambda l) & - \lambda\sh(\lambda l) + \frac{c_1}{EI} \ch(\lambda l) & \lambda\cos(\lambda l) - \frac{c_1}{EI} \sin(\lambda l) & \lambda\sin(\lambda l) + \frac{c_1}{EI} \cos(\lambda l)
\end{bmatrix} \cdot 
\begin{bmatrix}
    A \\ B \\ C \\ D
\end{bmatrix} = 
\begin{bmatrix}
    0 \\ 0 \\ 0 \\ 0
\end{bmatrix}
\end{align*}
$$