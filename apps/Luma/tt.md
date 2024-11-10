- value: PROGRAM
  is_identifier: true
  is_optional: false
  is_sequential: false
  has_or_operand: false
  is_grouped: false
  pos: 0
  children:
  - value: '&XML_STATEMENT|&REQUIRE_STATEMENT'
    is_identifier: false
    is_optional: false
    is_sequential: true
    has_or_operand: true
    is_grouped: true
    pos: 0
    children:
    - value: XML_STATEMENT
      is_identifier: true
      is_optional: false
      is_sequential: false
      has_or_operand: false
      is_grouped: false
      pos: 0
      children:
      - value: OPEN_TAG
        is_identifier: true
        is_optional: false
        is_sequential: false
        has_or_operand: false
        is_grouped: false
        pos: 0
        children:
        - value: OPEN_BRACKET
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 0
          children:
          - value: <
            is_identifier: false
            is_optional: false
            is_sequential: false
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
        - value: A_IDENTIFIER
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 1
          children:
          - value: '[a-zA-Z_][a-zA-Z0-9_\.]'
            is_identifier: false
            is_optional: false
            is_sequential: true
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
        - value: ATTRIBUTES
          is_identifier: true
          is_optional: true
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 2
          children:
          - value: '&ATTRIBUTE'
            is_identifier: false
            is_optional: false
            is_sequential: true
            has_or_operand: false
            is_grouped: true
            pos: 0
            children: []
        - value: CLOSE_BRACKET
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 3
          children:
          - value: '>'
            is_identifier: false
            is_optional: false
            is_sequential: false
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
      - value: PROGRAM
        is_identifier: true
        is_optional: false
        is_sequential: false
        has_or_operand: false
        is_grouped: false
        pos: 1
        children: []
      - value: CLOSE_TAG
        is_identifier: true
        is_optional: false
        is_sequential: false
        has_or_operand: false
        is_grouped: false
        pos: 2
        children:
        - value: OPEN_BRACKET
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 0
          children:
          - value: <
            is_identifier: false
            is_optional: false
            is_sequential: false
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
        - value: SLASH
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 1
          children:
          - value: /
            is_identifier: false
            is_optional: false
            is_sequential: false
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
        - value: B_IDENTIFIER
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 2
          children:
          - value: LIST|&OBJECT|&A_IDENTIFIER
            is_identifier: true
            is_optional: false
            is_sequential: false
            has_or_operand: true
            is_grouped: false
            pos: 0
            children:
            - value: LIST
              is_identifier: false
              is_optional: false
              is_sequential: false
              has_or_operand: false
              is_grouped: false
              pos: 0
              children:
              - value: OPEN_BRACKET
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 0
                children:
                - value: <
                  is_identifier: false
                  is_optional: false
                  is_sequential: false
                  has_or_operand: false
                  is_grouped: false
                  pos: 0
                  children: []
              - value: B_IDENTIFIER
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 1
                children: []
              - value: (&COMMA
                is_identifier: false
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 2
                children: []
              - value: B_IDENTIFIER)
                is_identifier: true
                is_optional: true
                is_sequential: true
                has_or_operand: false
                is_grouped: false
                pos: 3
                children: []
              - value: CLOSE_BRACKET
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 4
                children:
                - value: '>'
                  is_identifier: false
                  is_optional: false
                  is_sequential: false
                  has_or_operand: false
                  is_grouped: false
                  pos: 0
                  children: []
            - value: OBJECT
              is_identifier: true
              is_optional: false
              is_sequential: false
              has_or_operand: false
              is_grouped: false
              pos: 0
              children:
              - value: OPEN_KEY
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 0
                children:
                - value: '{'
                  is_identifier: false
                  is_optional: false
                  is_sequential: false
                  has_or_operand: false
                  is_grouped: false
                  pos: 0
                  children: []
              - value: (&A_IDENTIFIER
                is_identifier: false
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 1
                children: []
              - value: COLON
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 2
                children:
                - value: ':'
                  is_identifier: false
                  is_optional: false
                  is_sequential: false
                  has_or_operand: false
                  is_grouped: false
                  pos: 0
                  children: []
              - value: B_IDENTIFIER)
                is_identifier: true
                is_optional: true
                is_sequential: true
                has_or_operand: false
                is_grouped: false
                pos: 3
                children: []
              - value: CLOSE_KEY
                is_identifier: true
                is_optional: false
                is_sequential: false
                has_or_operand: false
                is_grouped: false
                pos: 4
                children:
                - value: '}'
                  is_identifier: false
                  is_optional: false
                  is_sequential: false
                  has_or_operand: false
                  is_grouped: false
                  pos: 0
                  children: []
            - value: A_IDENTIFIER
              is_identifier: true
              is_optional: false
              is_sequential: false
              has_or_operand: false
              is_grouped: false
              pos: 0
              children:
              - value: '[a-zA-Z_][a-zA-Z0-9_\.]'
                is_identifier: false
                is_optional: false
                is_sequential: true
                has_or_operand: false
                is_grouped: false
                pos: 0
                children: []
        - value: CLOSE_BRACKET
          is_identifier: true
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 3
          children:
          - value: '>'
            is_identifier: false
            is_optional: false
            is_sequential: false
            has_or_operand: false
            is_grouped: false
            pos: 0
            children: []
    - value: REQUIRE_STATEMENT
      is_identifier: true
      is_optional: false
      is_sequential: false
      has_or_operand: false
      is_grouped: false
      pos: 0
      children:
      - value: REQUIRE_LITERAL
        is_identifier: true
        is_optional: false
        is_sequential: false
        has_or_operand: false
        is_grouped: false
        pos: 0
        children:
        - value: require
          is_identifier: false
          is_optional: false
          is_sequential: false
          has_or_operand: false
          is_grouped: false
          pos: 0
          children: []
      - value: A_IDENTIFIER
        is_identifier: true
        is_optional: false
        is_sequential: false
        has_or_operand: false
        is_grouped: false
        pos: 1
        children:
        - value: '[a-zA-Z_][a-zA-Z0-9_\.]'
          is_identifier: false
          is_optional: false
          is_sequential: true
          has_or_operand: false
          is_grouped: false
          pos: 0
          children: []
- value: EOF
  is_identifier: true
  is_optional: false
  is_sequential: false
  has_or_operand: false
  is_grouped: false
  pos: 1
  children:
  - value: EOF
    is_identifier: false
    is_optional: false
    is_sequential: false
    has_or_operand: false
    is_grouped: false
    pos: 0
    children: []

- PROGRAM
    - &XML_STATEMENT|&REQUIRE_STATEMENT (sequential, or, grouped)
        - XML_STATEMENT
            - OPEN_TAG
                - OPEN_BRACKET
                    - <
                - A_IDENTIFIER
                    - [a-zA-Z_][a-zA-Z0-9_\.] (sequential)
                - ATTRIBUTES (optional)
                    - &ATTRIBUTE (sequential, grouped)
                - CLOSE_BRACKET
                    - >
            - PROGRAM
            - CLOSE_TAG
                - OPEN_BRACKET
                    - <
                - SLASH
                    - /
                - B_IDENTIFIER
                    - LIST|&OBJECT|&A_IDENTIFIER (or)
                        - LIST
                            - OPEN_BRACKET
                                - <
                            - B_IDENTIFIER
                            - (&COMMA
                            - B_IDENTIFIER) (optional, sequential)
                            - CLOSE_BRACKET
                                - >
                        - OBJECT
                            - OPEN_KEY
                                - {
                            - (&A_IDENTIFIER
                            - COLON
                                - :
                            - B_IDENTIFIER) (optional, sequential)
                            - CLOSE_KEY
                                - }
                        - A_IDENTIFIER
                            - [a-zA-Z_][a-zA-Z0-9_\.] (sequential)
                - CLOSE_BRACKET
                    - >
        - REQUIRE_STATEMENT
            - REQUIRE_LITERAL
                - require
            - A_IDENTIFIER
                - [a-zA-Z_][a-zA-Z0-9_\.] (sequential)
- EOF
    - EOF
