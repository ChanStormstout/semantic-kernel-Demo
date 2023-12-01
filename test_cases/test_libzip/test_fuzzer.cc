#include <stdint.h>
#include <stdlib.h>
#include <unistd.h> // Include the header for write and close functions
#include <zip.h>

// Make sure to link against the zip library when compiling
// Add -lzip to your compiler flags

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // Create a temporary file with the input data
    char tmpfile[] = "/tmp/fuzz-XXXXXX";
    int fd = mkstemp(tmpfile);
    if (fd < 0) {
        return 0; // Couldn't create file, so we just return
    }
    write(fd, data, size);
    close(fd);

    // Try to open the temporary file as a zip archive
    int err;
    zip_error_t ziperror;
    zip_t *za = zip_open(tmpfile, ZIP_RDONLY, &err);
    if (!za) {
        zip_error_init_with_code(&ziperror, err);
        // You can handle errors here, for now we will just clean up
        zip_error_fini(&ziperror);
    }

    // Clean up resources
    if (za) {
        zip_close(za);
    }
    unlink(tmpfile); // Remove the temporary file

    return 0; // Non-zero return values are reserved for future use.
}

