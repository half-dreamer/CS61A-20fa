test = {
  'name': 'derive-sum',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (make-sum 1 3)
          d853f7fcbaf33cb86d66fdc79149c4e7
          # locked
          scm> (make-sum 'x 0)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (make-sum 0 'x)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> (make-sum 'a 'x)
          9979e31ef97b2c17651dca39def0cab3
          # locked
          scm> (make-sum 'a (make-sum 'x 1))
          b972343ae4f8454603861ffa50b39514
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
          scm> (derive '(+ x 3) 'x)
          38dac9033a8f5e8edb2dbe6428e02d1d
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
    }
  ]
}
