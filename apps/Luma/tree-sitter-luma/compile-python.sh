gcc -shared -o bindings/python/tree_sitter_luma/_binding.so -fPIC bindings/python/tree_sitter_luma/binding.c src/parser.c $(python3-config --cflags --ldflags)
