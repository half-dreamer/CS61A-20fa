(define (factorial x) 
	(if (= x 0)	1 
	(* x (factorial (- x 1)))))
(display (factorial 4))


(define (fib n) 
	(if (or (= n 1) (= n 0)) n
		(+ (fib (- n 1)) (fib (- n 2)))
))
(print (fib 0))
(display (fib 1))
(display (fib 10))

(define (my_append a b) 
	(cond ((= b nil) a)
	(else (my_append (list a (car b)) (cdr b)))
	)