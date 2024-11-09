#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream> // Inclui a biblioteca para operações de entrada e saída.
#include <uv.h>

void on_write_end(uv_write_t* req, int status) {
    if (status) {
        fprintf(stderr, "Write error %s\n", uv_strerror(status));
    }
    uv_close((uv_handle_t*)req->handle, NULL);
    free(req);
}

void on_new_connection(uv_stream_t *server, int status) {
    if (status < 0) {
        fprintf(stderr, "New connection error %s\n", uv_strerror(status));
        return;
    }

    uv_tcp_t *client = (uv_tcp_t*) malloc(sizeof(uv_tcp_t));
    if (uv_tcp_init(uv_default_loop(), client) < 0) {
        fprintf(stderr, "Cannot initialize client TCP handle\n");
        return;
    }

    if (uv_accept(server, (uv_stream_t*) client) == 0) {
        uv_write_t *req = (uv_write_t*) malloc(sizeof(uv_write_t));

        char response[] = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello, world!";
        uv_buf_t buffer = uv_buf_init(response, strlen(response));

        uv_write(req, (uv_stream_t*) client, &buffer, 1, on_write_end);
        
    } else {
        uv_close((uv_handle_t*) client, NULL);
        free(client);
    }
}


int main() {
    std::cout << "Olá, mundo!" << std::endl; // Imprime a mensagem "Olá, mundo!" na tela.
    return 0; // Retorna 0 para indicar que o programa terminou com sucesso.
}

int uv_main() {
    return 0;
    // uv_tcp_t server;
    // uv_loop_t *loop = uv_default_loop();

    // if (uv_tcp_init(loop, &server) < 0) {
    //     fprintf(stderr, "Cannot initialize server TCP handle\n");
    //     return 1;
    // }

    // struct sockaddr_in addr;
    // if (uv_ip4_addr("0.0.0.0", 8080, &addr) < 0) {
    //     fprintf(stderr, "Cannot initialize IP address\n");
    //     return 1;
    // }

    // if (uv_tcp_bind(&server, (const struct sockaddr*)&addr, 0) < 0) {
    //     fprintf(stderr, "Cannot bind server to address\n");
    //     return 1;
    // }

    // if (uv_listen((uv_stream_t*) &server, 128, on_new_connection) < 0) {
    //     fprintf(stderr, "Cannot listen for connections\n");
    //     return 1;
    // }

    // return uv_run(loop, UV_RUN_DEFAULT);
}
