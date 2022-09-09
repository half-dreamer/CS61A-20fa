test = {
  'name': 'make-list',
  'points': 1,
  'suites': [
    {
      'type': 'scheme',
      'scored': True,
      'setup': """
      scm> (load-all ".")
      """,
      'cases': [
        {
          'code': """
          scm> (define a '(1))
          a
          scm> a
          (1)
          scm> (define b (cons 2 a))
          b
          scm> b
          (2 1)
          scm> (define c (list 3 b))
          c
          scm> c
          (3 (2 1))
          scm> (car c)
          3
          scm> (cdr c)
          ((2 1))
          scm> (car (car (cdr c)))
          2
          scm> (cdr (car (cdr c)))
          (1)
          """,
          'hidden': False
        },
        {
          'code': """
          scm> lst  ; type out exactly how Scheme would print the list
          ((1) 2 (3 4) 5)
          """,
          'hidden': False
        }
      ]
    }
  ]
}
