(defun main () 
    (defun fac (n) 
        (if (>= 1 n) 
            1 
            (* n (fac (- n 1)))
        )
    ) 
    (fac 5)
)
