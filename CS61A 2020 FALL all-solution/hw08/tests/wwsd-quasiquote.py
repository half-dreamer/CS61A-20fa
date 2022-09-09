test = {
  'name': 'quasiquote',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> '(1 x 3)
          c30b24263221c7c77c68d3897f9391d0
          # locked
          scm> (define x 2)
          36e066bfc6378b709f8c41ed98771eb2
          # locked
          scm> `(1 x 3)
          c30b24263221c7c77c68d3897f9391d0
          # locked
          scm> `(1 ,x 3)
          2252870f2a5c1955c880d5162a566d4f
          # locked
          scm> '(1 ,x 3)
          5990e767a417fea62dde636fe032fa84
          # locked
          scm> `(,1 x 3)
          c30b24263221c7c77c68d3897f9391d0
          # locked
          scm> `,(+ 1 x 3)
          c233180a72fb01da144c781913a400a2
          # locked
          scm> `(1 (,x) 3)
          43de7e9a9a70fd3afaa48eb472360044
          # locked
          scm> `(1 ,(+ x 2) 3)
          5d3982688a3e5fcc906abf800d1df260
          # locked
          scm> (define y 3)
          c74db679332f447849995c0c187d9b4e
          # locked
          scm> `(x ,(* y x) y)
          31dc9c8d9844e2454ad7b2aaaea4f390
          # locked
          scm> `(1 ,(cons x (list y 4)) 5)
          2292c661938cc9a199ca88ace6c2f73d
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
