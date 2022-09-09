test = {
  'name': 'over-or-under',
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
          scm> (over-or-under 5 5)
          0
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (over-or-under 5 4)
          1
          """,
          'hidden': False
        },
        {
          'code': """
          scm> (over-or-under 3 5)
          -1
          """,
          'hidden': False
        }
      ]
    }
  ]
}
