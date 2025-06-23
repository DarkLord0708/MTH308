% problem 1
f = @(x, y) (x - y)/2;
x = 0;
y = 1;
h = 0.1;

for i = 1:2
    k1 = f(x, y);
    k2 = f(x + h/2, y + h*k1/2);
    k3 = f(x + h/2, y + h*k2/2);
    k4 = f(x + h, y + h*k3);
    y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4);
    x = x + h;
end

fprintf("Problem 1: y(0.2) = %.6f\n", y);



% problem 2
f = @(x, y) -2*x - y;
x = 0;
y = -1;
h = 0.1;

for i = 1:5
    k1 = f(x, y);
    k2 = f(x + h/2, y + h*k1/2);
    k3 = f(x + h/2, y + h*k2/2);
    k4 = f(x + h, y + h*k3);
    y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4);
    x = x + h;
end

fprintf("Problem 2: y(0.5) = %.6f\n", y);



% problem 3
f = @(x, y) -y;
x = 0;
y = 1;
h = 0.1;

for i = 1:2
    k1 = f(x, y);
    k2 = f(x + h/2, y + h*k1/2);
    k3 = f(x + h/2, y + h*k2/2);
    k4 = f(x + h, y + h*k3);
    y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4);
    x = x + h;
end

fprintf("Problem 3: y(0.2) = %.6f\n", y);



% problem 4
f = @(x) x.^3;
a = 1;
b = 2;
n = 4;
h = (b - a)/n;

x = a:h:b;
y = f(x);

integral = h/2 * (y(1) + 2*sum(y(2:end-1)) + y(end));
fprintf("Problem 4: Integral ≈ %.6f\n", integral);



% problem 5
f = @(x) exp(-x).*sin(x);
a = 0;
b = 3;
n = 6; % Must be even
h = (b - a)/n;

x = a:h:b;
y = f(x);

odd_sum = sum(y(2:2:end-1));
even_sum = sum(y(3:2:end-2));

integral = (h/3) * (y(1) + 4*odd_sum + 2*even_sum + y(end));
fprintf("Problem 5: Integral ≈ %.6f\n", integral);


% problem 7
f = @(x, y) (x + y).*sin(x.*y);
x0 = 0;
y0 = 5;
h = 0.2;
xf = 2;

x = x0:h:xf;
y = zeros(size(x));
y(1) = y0;

for i = 1:(length(x)-1)
    k1 = f(x(i), y(i));
    k2 = f(x(i) + h/2, y(i) + h*k1/2);
    k3 = f(x(i) + h/2, y(i) + h*k2/2);
    k4 = f(x(i) + h, y(i) + h*k3);
    
    y(i+1) = y(i) + (h/6)*(k1 + 2*k2 + 2*k3 + k4);
end

% Display results
fprintf('x\t\ty\n');
for i = 1:length(x)
    fprintf('%.1f\t%.6f\n', x(i), y(i));
end

function I = trapezoidal_rule(f, a, b, n)
    h = (b - a) / n;
    x = a:h:b;
    y = f(x);
    I = h/2 * (y(1) + 2*sum(y(2:end-1)) + y(end));
end
function I = simpsons_rule(f, a, b, n)
    if mod(n, 2) ~= 0
        error('Simpson''s rule requires even number of intervals.');
    end
    h = (b - a) / n;
    x = a:h:b;
    y = f(x);
    I = h/3 * (y(1) + 4*sum(y(2:2:end-1)) + 2*sum(y(3:2:end-2)) + y(end));
end
% Example: a. ∫_1^2 x*log(x) dx with n = 4
f = @(x) x .* log(x);
a = 1; b = 2; n = 4;

I_trap = trapezoidal_rule(f, a, b, n);
I_simp = simpsons_rule(f, a, b, n);

fprintf("Trapezoidal Rule Result: %.6f\n", I_trap);
fprintf("Simpson's Rule Result: %.6f\n", I_simp);
