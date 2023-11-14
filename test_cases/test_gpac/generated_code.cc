extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    // Assuming you have the necessary headers included and the required libraries linked

    // Convert the input data to a string
    std::string fileName(reinterpret_cast<const char*>(data), size);

    // Call the gf_isom_open_file function
    GF_ISOFile* movie = gf_isom_open_file(fileName.c_str(), GF_ISOM_OPEN_READ, nullptr);

    // Check if the movie object is valid
    if (movie != nullptr) {
        // Do something with the movie object if needed

        // Free the memory allocated for the movie object
        gf_isom_delete_movie(movie);
    }

    return 0;
}