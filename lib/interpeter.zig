const std = @import("std");
const Parser = @import("parser.zig");

pub fn interpret(expr: *Parser.Expr) !i32 {
    return switch (expr.*) {
        .Integer => |i| i,
        .Operation => |op| {
            // Interpret operations recursively
        },
    };
}
