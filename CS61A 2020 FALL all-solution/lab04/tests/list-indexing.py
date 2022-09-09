test = {
  'name': 'List Indexing',
  'points': 0,
  'suites': [
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> x = [1, 3, [5, 7], 9] # Write the expression that indexes into x to output the 7
          x[2][1]
          >>> x = [[3, [5, 7], 9]] # Write the expression that indexes into x to output the 7
          x[0][1][1]
          """
        }
      ]
    },
    {
      'type': 'wwpp',
      'cases': [
        {
          'code': """
          >>> lst = [3, 2, 7, [84, 83, 82]]
          >>> lst[4]
          Error
          >>> lst[3][0]
          84
          """
        }
      ]
    }
  ]
}
