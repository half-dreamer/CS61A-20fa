test = {
  'name': 'derive-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (derive x^2 'x) ; Remember products have the form (* a b)
          5677b347b03655ed5ba4d637128b074c
          # locked
          scm> (derive x^3 'x)
          0d0ddbcb02925ae809a618030fe91cb0
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (derive (make-sum x^3 x^2) 'x)
          (+ (* 3 (^ x 2)) (* 2 x))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      scm> (define x^2 (make-exp 'x 2))
      scm> (define x^3 (make-exp 'x 3))
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
