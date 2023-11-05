void LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    AvahiDnsPacket *p;
    uint8_t *packet_data;

    // Create a new AvahiDnsPacket
    p = avahi_dns_packet_new(size);
    if (!p) {
        // Handle error
        return;
    }

    // Copy the input data to the packet
    packet_data = AVAHI_DNS_PACKET_DATA(p);
    memcpy(packet_data, data, size);

    // Invoke the avahi_dns_packet_consume_key function
    int ret_unicast_response;
    AvahiKey *key = avahi_dns_packet_consume_key(p, &ret_unicast_response);

    // Handle the result of the function call
    if (key) {
        // Key was successfully created
        // Do something with the key
    } else {
        // Handle error
    }

    // Free the AvahiDnsPacket
    avahi_dns_packet_free(p);
}