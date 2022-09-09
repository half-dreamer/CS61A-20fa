test = {
  'name': 'derive-product',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-product 2 3)
          c233180a72fb01da144c781913a400a2
          # locked
          scm> (make-product 'x 0)
          5ca79ce4fb57688138ae494e7845eb74
          # locked
          scm> (make-product 1 'x)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (make-product 'a 'x)
          b3bc97b672456bf013678796c90cd224
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (derive '(* x y) 'x)
          y
          scm> (derive '(+ x (* x y)) 'x)
          (+ 1 y)
          scm> (derive '(* (* x y) (+ x 3)) 'x)
          (+ (* y (+ x 3)) (* x y))
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
