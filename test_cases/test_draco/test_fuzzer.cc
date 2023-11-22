#include "draco/compression/decode.h"
#include "draco/core/decoder_buffer.h"
#include "draco/mesh/mesh.h"
#include "draco/point_cloud/point_cloud.h"

extern "C" int LLVMFuzzerTestOneInput(const uint8_t *data, size_t size) {
  draco::DecoderBuffer buffer;
  buffer.Init(reinterpret_cast<const char *>(data), size);

  draco::Decoder decoder;
  auto type_statusor = decoder.GetEncodedGeometryType(&buffer);
  if (!type_statusor.ok()) {
    return 0;  // Unable to determine the geometry type, so we return immediately.
  }

  const draco::EncodedGeometryType geom_type = type_statusor.value();
  if (geom_type == draco::TRIANGULAR_MESH) {
    auto mesh_statusor = decoder.DecodeMeshFromBuffer(&buffer);
    if (!mesh_statusor.ok()) {
      return 0;  // Failed to decode mesh.
    }
    // Mesh decoded successfully, no further action taken for fuzzing.
  } else if (geom_type == draco::POINT_CLOUD) {
    auto point_cloud_statusor = decoder.DecodePointCloudFromBuffer(&buffer);
    if (!point_cloud_statusor.ok()) {
      return 0;  // Failed to decode point cloud.
    }
    // Point cloud decoded successfully, no further action taken for fuzzing.
  }
  return 0;  // Fuzzing was successful.
}

