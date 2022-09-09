import re

DICT_PROMPT_TO_CHARACTER = {
    '>>>': '#',
    'scm>': ';',
}

def canonicalize(assess_id):
    """
    Takes an assessment/question's ID and canonicalizeicalizes it across iterations of
    a course.
    """
    
    hash_regex = re.compile(r'\w{32}')
    
    lines = assess_id.split('\n')
    canon_lines = []
  
    parsing_code = False
    for line in lines:
        line = line.strip()

        if not parsing_code and len(line) > 0:
            for prompt in DICT_PROMPT_TO_CHARACTER:
                if line.startswith(prompt):
                    parsing_code = True
                    comment_character = DICT_PROMPT_TO_CHARACTER[prompt]
                    break

        # If False still in preamble and do not include in canonicalized lines
        if parsing_code:
            # Remove any comments
            comment_index = line.find(comment_character)
            if comment_index >= 0:
                line = line[0:comment_index].strip()

            # If a hashed answer, replace with constant since these vary by semester
            if hash_regex.match(line):
                line = 'LOCKED_ANSWER'

            # Remove any '# locked' text since these are here regardless of language
            if line == '# locked':
                line = ''

            if len(line) > 0:
                canon_lines.append(line)

    return '\n'.join(canon_lines) + '\n'
