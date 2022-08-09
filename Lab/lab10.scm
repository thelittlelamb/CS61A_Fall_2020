(define (over-or-under num1 num2)
  (cond ((< num1 num2) -1)
        ((= num1 num2) 0)
        ((> num1 num2) 1))
)


(define (make-adder num)
  (lambda (x) (+ x num))
)


(define (composed f g)
  (lambda (x) (f (g x)))
)


(define lst
  (list (list 1) list 2 (list 3 4) 5)
)


(define (remove item lst)
  (if (null? lst) ;判断nil的方法，不可以使用(= nil lst)会报错
      nil ;(nil) is wrong
      (if (= item (car lst))
          (remove item (cdr lst))
          (cons (car lst) (remove item (cdr lst)))
          )
      )
)

