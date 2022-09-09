test = {
  'name': 'eval-calls',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'c233180a72fb01da144c781913a400a2',
          'choices': [
            '1',
            '2',
            '5',
            '6',
            '7',
            '8'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval to evaluate the expression: (+ 2 4 6 8) ?'
        },
        {
          'answer': '38dac9033a8f5e8edb2dbe6428e02d1d',
          'choices': [
            '1',
            '2',
            '5',
            '6',
            '7',
            '8'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (+ 2 4 6 8) ?'
        },
        {
          'answer': 'd32d43311c6eb775f7ff6c3d9c673e57',
          'choices': [
            '3',
            '7',
            '8',
            '9',
            '10',
            '13'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval: (+ 2 (* 4 (- 6 8))) ?'
        },
        {
          'answer': '400b880bd4ddd7622658a2c6ab1656de',
          'choices': [
            '3',
            '7',
            '8',
            '9',
            '10',
            '13'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (+ 2 (* 4 (- 6 8))) ?'
        },
        {
          'answer': 'c233180a72fb01da144c781913a400a2',
          'choices': [
            '1',
            '2',
            '4',
            '6',
            '8',
            '10'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval: (if #f (+ 2 3) (+ 1 2)) ?'
        },
        {
          'answer': '38dac9033a8f5e8edb2dbe6428e02d1d',
          'choices': [
            '1',
            '2',
            '4',
            '6',
            '8',
            '10'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (if #f (+ 2 3) (+ 1 2)) ?'
        },
        {
          'answer': '38dac9033a8f5e8edb2dbe6428e02d1d',
          'choices': [
            '0',
            '1',
            '3',
            '7',
            '8',
            '9'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval: (define (cube a) (* a a a)) ?'
        },
        {
          'answer': '5ca79ce4fb57688138ae494e7845eb74',
          'choices': [
            '0',
            '1',
            '3',
            '7',
            '8',
            '9'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (define (cube a) (* a a a)) ?'
        },
        {
          'answer': 'a47f39b96b0a3849b716b770fff860cc',
          'choices': [
            '2',
            '3',
            '7',
            '8',
            '9',
            '11'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_eval: (cube 3) ?'
        },
        {
          'answer': 'bec7b0c91bdcb548cda9e9f3546cf0d7',
          'choices': [
            '2',
            '3',
            '7',
            '8',
            '9',
            '11'
          ],
          'hidden': False,
          'locked': True,
          'question': 'How many calls are made to scheme_apply: (cube 3) ?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
