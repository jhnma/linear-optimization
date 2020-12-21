% problem data:
  % A: constraint matrix (m*m)
  % B: RHS vector (n)
  % C: cost-coeff vector (n)

% Tab is a simplex tableau with a basic feasible solution, tab is a
% (m+1)*(n+1) matrix.

% Step 1
if any(tab(1,1:n)>0) % checks if vector in first n columns of the first row is larger than 0
    % Step 2
    % pivot_column such that tab(1,pivot_column) > 0
    d = tab(2:end, pivot_column);
    if (all(d <= 0)
        % stop and declare unboundedness of optimal value
        
    else
        % Step 3
        f = tab(2:end, end);
        J = find(d>0);
        [~,j]=min(f(J)/d(J));
        pivot_row=J(j)+1;
        
        % Step 4
        % Gauss-Jordan Exchange
        
    end
else
   % current tableau is optimal 
end