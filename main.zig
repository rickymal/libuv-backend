const std = @import("std");
const Lexer = @import("lib/lexer.zig");
const Parser = @import("lib/parser.zig");
const Interpreter = @import("lib/interpreter.zig");

pub fn main() !void {
    const allocator = std.heap.page_allocator;
    const source = "3 + 4 - 5";
    const tokens = try Lexer.tokenize(source);
    const expr = try Parser.parse(tokens);
    const result = try Interpreter.interpret(expr);
    std.debug.print("Result: {}\n", .{result});
}
