# MTH308
# 📊 Numerical Methods in Python

This repository contains Python implementations of various **Numerical Methods** used to solve mathematical problems computationally. Each method is organized into logical sections for ease of understanding, testing, and extension.

## 📁 Contents

### 🔹 Root Finding Methods (root_finding)
- **Bisection Method**
- **Regula Falsi (False Position)** – Normal and Modified
- **Secant Method**
- **Newton-Raphson Method** (single-variable and system of equations)

### 🔹 Linear System Solvers (linear_systems)
- **Gaussian Elimination** (with and without Partial Pivoting)
- **LU Decomposition** (Doolittle Method)
- **Iterative Solvers:**
  - Gauss-Jacobi
  - Gauss-Seidel
  - SOR (Successive Over-Relaxation)
  - SSOR (Symmetric SOR)

### 🔹 Eigenvalue Problems (Eigen Value problem)
- **Power Method** – To compute the dominant eigenvalue and its eigenvector

### 🔹 Interpolation
- **Lagrange Interpolation**
- **Newton’s Divided Differences**
- **Neville’s Method**

### 🔹 Numerical Differentiation
- **Richardson Extrapolation**
- **Euler’s Method**
- **Runge-Kutta 2nd Order Method** (Midpoint Method)

### 🔹 Numerical Integration
- **Trapezoidal Rule**
- **Simpson’s 1/3 Rule**
- **Newton-Cotes (Composite, General Degree)**
- **Romberg Integration** 

---

## 🧪 Example Usage

Each file is self-contained and can be run independently. For example:

```bash
python bisection_method.py
python runge_kutta_method.py
python simpsons_rule.py
