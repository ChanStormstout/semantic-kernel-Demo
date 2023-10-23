#include <assimp/Importer.hpp>

extern "C" int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size) {
    // Create an instance of the Importer class
    ASSIMP_API::Importer importer;

    // Call the ReadFileFromMemory method with the provided data and size
    const aiScene* scene = importer.ReadFileFromMemory(data, size, aiProcessPreset_TargetRealtime_Quality, nullptr);

    // Check if the scene was successfully loaded
    if (scene != nullptr) {
        // Process the scene data
        // ...
    }

    return 0;
}