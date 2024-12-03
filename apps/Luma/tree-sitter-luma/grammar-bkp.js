 * @file This is a luma tester
 * @author Henrique Mauler <henriquemauler@gmail.com>
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check
module.exports = grammar({
  name: 'cxml',

  extras: $ => [
    /\s/,
    $.comment
  ],

  // Removida a declaração de conflito
  // conflicts: $ => [
  //   [$._content, $.imperative_block]
  // ],

 rules: {
    document: $ => repeat($._statement),

    _statement: $ => choice(
      $.package_statement,
      $.element
    ),

    package_statement: $ => seq(
      'package',
      field('package_name', $.identifier)
    ),

    element: $ => seq(
      '<',
      field('tag_name', $.identifier),
      repeat($.attribute),
      '>',
      repeat($._content),
      '</',
      field('closing_tag_name', $.identifier),
      '>'
    ),

    attribute: $ => seq(
      field('attribute_name', $.identifier),
      '=',
      field('attribute_value', $._attribute_value)
    ),

    _attribute_value: $ => choice(
      $.string,
      $.array,
      $.object,
      $.element
    ),

    array: $ => seq(
      '[',
      commaSep1($.value),
      ']'
    ),

    object: $ => seq(
      '{',
      commaSep1($.pair),
      '}'
    ),

    pair: $ => seq(
      field('key', $.identifier),
      ':',
      field('value', $.value)
    ),

    value: $ => choice(
      $.string,
      $.number,
      $.identifier
    ),

    _content: $ => prec(2, choice(
      $.math_block,
      // $.imperative_block,
      $.element
    )),

    math_block: $ => seq(
        '<math>',
      $._math_content,
         '</math>'
    ),

    _math_content: $ => prec.right(repeat1(
      choice(
        $.math_expression_statement,
        $.math_statement,
        $.math_function_definition
      )
    )),

    math_expression_statement: $ => seq(
      $.math_expression,
      optional(';')
    ),

    math_expression: $ => seq(
      $.identifier,
         optional(
            '(',
           $.identifier,
             repeat(
                ',',
               $.identifier,
             ),
           ')',
         ),
      '=',
      $.math_term
    ),

    cond_expression: $ => seq(
      $.identifier,
      choice(
           '<=',
           '>=',
           '==',
           '!=',
         ),
         $.identifier,
    )

    math_statement: $ => seq(
      $.identifier,
      '(',
      optional($.identifier_list),
      ')',
      '=',
      $.math_term,
      $.math_condition,
      optional(';')
    ),

    math_function_definition: $ => seq(
      $.identifier,
      '(',
      optional($.identifier_list),
      ')',
      '=',
      $.math_term,
      optional(';')
    ),

    math_condition: $ => choice(
      seq('where', $.cond_expression),
      'otherwise'
    ),

    math_term: $ => choice(
      $.number,
      $.identifier,
      seq('(', $.math_term, ')'),
      prec.right(4, seq($.math_term, '**', $.math_term)), // Exponenciação
      prec.left(3, seq($.math_term, '*', $.math_term)),   // Multiplicação
      prec.left(3, seq($.math_term, '/', $.math_term)),   // Divisão
      prec.left(2, seq($.math_term, '+', $.math_term)),   // Adição
      prec.left(2, seq($.math_term, '-', $.math_term))    // Subtração
    ),

    identifier_list: $ => commaSep1($.identifier),

    imperative_block: $ => prec(1, repeat1(
      choice(
        $.imperative_statement,
        $.element
      )
    )),

    imperative_statement: $ => seq(
      $.identifier,
      '=',
      $.function_call,
      optional(';')
    ),

    function_call: $ => seq(
      $.identifier,
      '(',
      optional($.argument_list),
      ')'
    ),

    argument_list: $ => commaSep1($.value),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_]*/,
    number: $ => /\d+(\.\d+)?/,
    string: $ => choice(
      seq('"', repeat(/[^"]/), '"'),
      seq("'", repeat(/[^']/), "'")
    ),

    comment: $ => token(seq('//', /.*/))
  }
});

function commaSep1(rule) {
  return seq(rule, repeat(seq(',', rule)));
}
