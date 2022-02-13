(defun main () 
    (defun sum (n) 
        (if (>= 1 n) 
            1 
            (+ n (sum (- n 1)))
        )
    ) 
    (sum 10)
)
