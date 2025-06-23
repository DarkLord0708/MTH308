% POWER METHOD - Find dominant eigenvalue and eigenvector
% --------------------------------------------------------

% Define matrix A
A = [3 0 0; -4 6 2; 16 -15 -5];

% Initial guess (non-zero vector)
x = [1; 0.5; 0.25];

% Parameters
tol = 1e-6;
max_iter = 100;

% Normalize initial vector
% x = x / max(abs(x));
% disp(x);
lambda_old = 0;

% Power Method Loop
for k = 1:max_iter
    y = A * x;
    x = y / max(abs(y));             % Normalize the vector
    lambda = max(abs(y));         

    % Check convergence
    if abs(lambda - lambda_old) < tol
        fprintf('Converged in %d iterations.\n', k);
        break;
    end

    lambda_old = lambda;
end

% Display results
fprintf('Dominant Eigenvalue: %.6f\n', lambda);
disp('Corresponding Eigenvector:');
disp(x);
