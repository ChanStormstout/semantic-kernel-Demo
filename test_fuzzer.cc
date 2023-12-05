#include <stdint.h>
#include <stddef.h>
#include "coap3/coap.h"
#include "/home/victor/workspace/fuzzing_target_repo/libcoap/include/coap3/coap_pdu.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    coap_proto_t proto = COAP_PROTO_UDP;

    // Initialize pdu with correct enum types and values
    // Assuming COAP_MESSAGE_CON and COAP_REQUEST_GET are correct, check your library for exact values
    coap_pdu_t *pdu = coap_pdu_init(0, 0, 0, size);
    if (!pdu) {
        return 0;
    }

    coap_add_data(pdu, size, data);

    // Invoke the target function
    coap_pdu_parse(proto, data, size, pdu);

    coap_delete_pdu(pdu);

    return 0;
}
