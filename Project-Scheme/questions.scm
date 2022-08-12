(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

(define (zip pairs)
  'replace-this-line)


;  Problem 15: Returns a list of two-element lists
; (1 2 3 4 5) -> (cons 1 (cons 2 (cons 3 (cons 4 nil))))
; ((1 2)) -> (cons (cons 1 (cons 2 nil)) nil)
; ((1 2) (3 4)) -> (cons (cons 1 (cons 2 nil)) (cons (cons 3 (cons 4 nil)) nil))
(define (enumerate s)
(begin(define (helper index s)
              (cond ((null? s) s)
                    (else (cons (cons index (cons (car s) nil)) (helper (+ index 1) (cdr s))))
              )
    )
    (helper 0 s)
) 
)
; END PROBLEM 15

;; Problem 16: Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (begin(define (helper comp list1 list2)
                (cond ((null? list1) list2)
                      ((null? list2) list1)
                      (else (cond ((comp (car list1) (car list2)) (cons (car list1) (helper comp (cdr list1) list2)))
                                  (else (cons (car list2) (helper comp list1 (cdr list2))))
                            )
                      )
                )
        )
        (helper comp list1 list2)
  )
  )
  ; END PROBLEM 16

;; Problem 17
(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (cond (
          ((null? (cdr s)) (cons s nil))
          ((> (car s) (car (cdr s))) (cons (cons (car s) nil) (nondecreaselist (cdr s))))
          (else (cons (cons (car s) (car (nondecreaselist (cdr s)))) (cdr (nondecreaselist (cdr s))))))
    )
)
    ; END PROBLEM 17


(define (zip s)
        (cond ((null? s) '(() ()))
              (else (cons (cons (car (car s)) (car (zip (cdr s)))) (cons (cons (car (cdr (car s))) (car (cdr (zip (cdr s))))) nil))))
)


;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (cons (cons 'lambda (cons (car (zip values)) (cons (let-to-lambda (car body)) nil))) (car (cdr (zip values))))
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))

