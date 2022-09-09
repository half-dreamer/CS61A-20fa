test = {
  'name': 'make-exp',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-exp 2 4)
          43fb0199e9e2345f8b8a767d78463c89
          # locked
          scm> (make-exp 'x 1)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (make-exp 'x 0)
          38dac9033a8f5e8edb2dbe6428e02d1d
          # locked
          scm> x^2
          37c446142756e6233e39a8a175b02f82
          # locked
          scm> (first-operand x^2)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (second-operand x^2)
          bec7b0c91bdcb548cda9e9f3546cf0d7
          # locked
          scm> (exp? x^2) ; #t or #f
          545654f52801dba9cbbe0347d265df09
          # locked
          scm> (exp? 1)
          8cd49ce066289d3b150d7b6108dda61e
          # locked
          scm> (exp? 'x)
          8cd49ce066289d3b150d7b6108dda61e
          # locked
          """,
          'hidden': False,
          'locked': True
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
