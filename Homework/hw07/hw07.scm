(define (filter-lst fn lst)
  (if (null? lst)
       nil
       (if (fn (car lst)) ;返回值是#t or #f
           (cons (car lst) (filter-lst fn (cdr lst)))
           (filter-lst fn (cdr lst))
       )
   )
)

(define (interleave first second)
  (cond ((null? first) second)
        ((null? second) first)
        (else (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))))
  )
)


(define (accumulate combiner start n term)
 (if (= n 0)
     start
     (combiner (term n) (accumulate combiner start (- n 1) term))
 )
)


(define (no-repeats lst)
 (if (null? lst)
     nil
     (cons (car lst)
           (no-repeats (filter-lst (lambda (x) (not (= x (car lst)))) (cdr lst))))
 )
)


