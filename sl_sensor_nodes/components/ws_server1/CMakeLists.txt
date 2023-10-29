idf_component_register(
    SRCS "ws_server1.c"
    INCLUDE_DIRS "inc"
    REQUIRES "esp_event" "nvs_flash" "log" "esp_system" "protocol_examples_common" "esp_netif" "esp_wifi" "esp_eth" "esp_http_server"
)