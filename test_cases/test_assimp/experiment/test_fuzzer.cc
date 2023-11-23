#include "Common/Importer.h"
#include "Common/BaseProcess.h"
#include "Common/DefaultProgressHandler.h"
#include "PostProcessing/ProcessHelper.h"
#include "Common/ScenePreprocessor.h"
#include "Common/ScenePrivate.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
    // Create an instance of the Importer class
    Assimp::Importer importer;

    // Optionally, set up any required properties or flags for the importer here
    // ...

    // Call the ReadFileFromMemory function with the provided data and size
    const aiScene* scene = importer.ReadFileFromMemory(static_cast<const void*>(data), size, 0 /* flags */, nullptr /* hint */);

    // For fuzzing, we typically don't need to do anything with the scene
    // However, if you want to check certain properties, you can do so here
    // ...

    // The return value is non-zero if the input is interesting (e.g., triggers a crash or bug)
    // and zero otherwise. For now, we return zero to indicate successful processing of the input.
    return 0;
}

