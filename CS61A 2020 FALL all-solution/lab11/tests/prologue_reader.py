test = {
  'name': 'Prologue - Reader',
  'points': 0,
  'suites': [
  {
      'type': 'concept',
      'cases':
      [
        {
          'question': r"""
          What does REPL stand for?
          """,
          'choices': [
            'Read-Eval-Print-Loop',
            'Really-Enormous-Purple-Llamas',
            "Read-Eval-Parse-Lex",
          ],
          'answer': 'Read-Eval-Print-Loop',
        },
        {
          'question': r"""
          What does the read component of the REPL loop do?
          """,
          'choices': [
            'Evaluates call expressions',
            'Turns input into tokens',
            'Ensures a function has been defined before it is called',
            'Turns input into a useful data structure',
          ],
          'answer': 'Turns input into a useful data structure',
        },
        {
          'question': r"""
          What does the tokenize function in reader.py return?
          """,
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression',
          ],
          'answer': 'Input expression represented as a list of tokens',
        },
        {
          'question': r"""
          What will tokenize('add(3, 4)') output?
          """,
          'choices': [
            "['add', '(', 3, ',', 4, ')']",
            "['a', 'd', 'd', '(', '3', ',', '4', ')']",
            "['add', '(', '3', ',', '4', ')']",
            "['a', 'd', 'd', '(', 3, ',', 4, ')']",
          ],
          'answer': "['add', '(', 3, ',', 4, ')']",
        },
        {
          'question': r"""
          What will tokenize('(lambda: 4)()') output?
          """,
          'choices': [
            "['(', LambdaExpr, 4, ')', '(', ')']",
            "['lambda', 4, '(', ')']",
            "['(', 'lambda', ':', 4, ')', '(', ')']",
            "['(', LambdaExpr, ':', 4, ')', '(', ')']",
          ],
          'answer': "['(', 'lambda', ':', 4, ')', '(', ')']",
        },
        {
          'question': r"""
          What does the read_expr function in reader.py accept as input and
          return?  (looking at the read function may help answer this question)
          """,
          'choices': [
            'List of tokens and number of parentheses',
            'Input expression and list of tokens',
            'List of tokens and an instance of a subclass of Expr',
            'Input expression and an instance of a subclass of Expr',
          ],
          'answer': 'List of tokens and an instance of a subclass of Expr',
        },
        {
          'question': r"""
          What does the read function in reader.py return?
          """,
          'choices': [
            'Input expression with corrected number of parentheses',
            'Input expression represented as a list of tokens',
            'Input expression represented as an instance of a subclass of Expr',
            'Result of evaluating the input expression',
          ],
          'answer': 'Input expression represented as an instance of a subclass of Expr',
        },
        {
          'question': r"""
          What will read('1') output?
          """,
          'choices': [
            'Literal(1)',
            'Number(1)',
            "Name('1')",
            'Name(1)',
          ],
          'answer': 'Literal(1)',
        },
        {
          'question': r"""
          What will read('x') output?
          """,
          'choices': [
            'Literal(x)',
            'x',
            'Name(x)',
            "Name('x')",
          ],
          'answer': "Name('x')",
        },
        {
          'question': r"""
          What will read('add(3, 4)') output?
          """,
          'choices': [
            "CallExpr(Literal('add'), Literal(3), Literal(4))",
            "CallExpr('add', [Literal(3), Literal(4)])",
            "CallExpr(Name('add'), Literal(3), Literal(4))",
            "CallExpr(Name('add'), [Literal(3), Literal(4)])",
          ],
          'answer': "CallExpr(Name('add'), [Literal(3), Literal(4)])",
        },
      ]
  }
  ]
}
