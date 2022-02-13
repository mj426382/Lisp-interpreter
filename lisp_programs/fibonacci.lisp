(defun main () 
    (defun fibo (n) 
        (if (>= 1 n) 
            n 
            (+ (fibo (- n 1)) (fibo (- n 2)))
        )
    ) 
    (fibo 20)
)
