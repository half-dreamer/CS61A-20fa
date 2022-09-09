test = {
  'name': 'make-adder',
  'points': 1,
  'suites': [
    {
      'scored': True,
      'setup': """
      scm> (load-all ".")
      scm> (define add-two (make-adder 2))
      scm> (define add-three (make-adder 3))
      """,
      'type': 'scheme',
      'cases': [
        {
          'code': """
          scm> (add-two 2)
          4
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (add-two 3)
          5
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (add-three 3)
          6
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (add-three 9)
          12
          """,
          'hidden': False
        }
      ]
    }
  ]
}
