test = {
    'name': 'Prologue - Expr',
    'points': 0,
    'suites': [
    {
        'type': 'concept',
        'cases':
        [
            {
              'question': r"""
              What are all the types of expressions in PyCombinator?
              """,
              'choices': [
                'literal, name, call expression, lambda expression',
                'number, lambda function, primitive function, string',
                'value, expression, function, number',
                'name, function, number, literal',
              ],
              'answer': 'literal, name, call expression, lambda expression',
            },
            {
              'question': r"""
              What are all the types of values in PyCombinator?
              """,
              'choices': [
                'number, lambda function, primitive function',
                'number, string, function',
                'name, number, lambda function',
                'number, lambda expression, primitive function',
              ],
              'answer': 'number, lambda function, primitive function',
            },
            {
              'question': r"""
              What does a Literal evaluate to?
              """,
              'choices': [
                'a Number',
                'a String',
                'a Function',
                'an Expression',
              ],
              'answer': 'a Number',
            },
            {
              'question': r"""
              What is the difference between a lambda expression and a lambda function?
              """,
              'choices': [
                'They are the same thing',
                'A lambda expression is the result of evaluating a lambda function',
                'A lambda function is the result of evaluating a lambda expression',
                'A lambda expression is a call to a lambda function',
              ],
              'answer': 'A lambda function is the result of evaluating a lambda expression',
            },
            {
              'question': r"""
              Which of the following describes the eval method?
              """,
              'choices': [
                'A method of Expr objects that evaluates the Expr and returns a Value',
                'A method of Expr objects that evaluates a call expression and returns a Number',
                'A method of LambdaExpression objects that evaluates a function call',
                'A method of Literal objects that returns a Name',
              ],
              'answer': 'A method of Expr objects that evaluates the Expr and returns a Value',
            },
            {
              'question': r"""
              How are environments represented in our interpreter?
              """,
              'choices': [
                'As dictionaries that map variable names to Value objects',
                'As sequences of Frame objects',
                'As dictionaries that map Name objects to Value objects',
                'As linked lists containing dictionaries',
              ],
              'answer': 'As dictionaries that map variable names to Value objects',
            }
        ]
    }
    ]


}
