const std = @import("std");
const Lexer = @import("lexer.zig");

pub const Expr = union(enum) {
    Integer: i32,
    Operation: struct {
        left: *Expr,
        op: Op,
        right: *Expr,
    },
};

pub const Op = enum { Add, Subtract };

pub fn parse(tokens: []Lexer.Token) !*Expr {
    // Parsing logic here
}
