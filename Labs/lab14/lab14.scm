

(define (compose-all funcs)
  (if (zero? (length funcs) )  
      (lambda (x) x)
      (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x) )  )
  
  )
)

(define identity (compose-all (list)))

(identity 42)