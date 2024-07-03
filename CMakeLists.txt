cmake_minimum_required(VERSION 3.10)
project(my_libuv_backend_cpp)

# Especifique onde estão os headers e bibliotecas para o libuv
include_directories("/usr/include")  # Normalmente os headers estão em /usr/include
link_directories("/usr/lib/x86_64-linux-gnu")  # Normalmente as bibliotecas estão aqui, mas isso pode variar

# Adiciona os arquivos fonte do executável, ajustando o caminho para a pasta lib
add_executable(my_libuv_backend_cpp main.cpp lib/lexer.cpp lib/parser.cpp lib/interpreter.cpp)

# Link com a biblioteca libuv
target_link_libraries(my_libuv_backend_cpp uv)
