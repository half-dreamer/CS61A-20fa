test = {
  'name': 'size',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          sqlite> SELECT * FROM sentences;
          The two siblings, barack plus clinton have the same size: standard
          The two siblings, abraham plus grover have the same size: toy
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'ordered': False,
      'scored': True,
      'setup': r"""
      sqlite> .read hw09.sql
      """,
      'teardown': '',
      'type': 'sqlite'
    }
  ]
}
