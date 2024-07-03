const std = @import("std");

pub const Token = struct {
    typ: TokenType,
    value: []const u8,
};

pub const TokenType = enum {
    integer,
    plus,
    minus,
    end,
};

pub fn tokenize(source: []const u8) ![]Token {
    var tokens: []Token = &[_]Token{};
    var i: usize = 0;
    while (i < source.len) {
        switch (source[i]) {
            '0'...'9' => {
                // Implement logic to handle numbers
            },
            '+' => {
                // Handle plus token
            },
            '-' => {
                // Handle minus token
            },
            else => {}
        }
        i += 1;
    }
    return tokens;
}
