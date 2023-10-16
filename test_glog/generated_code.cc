void LLVMFuzzerTestOneInput(const unsigned char *data, unsigned Size) {
  // Convert the input data to a string
  std::string input(reinterpret_cast<const char *>(data), Size);

  // Create a buffer to store the demangled symbol
  char buffer[1024]; // Adjust the size as needed

  // Call the Demangle function with the input and buffer
  bool success = Demangle(input.c_str(), buffer, sizeof(buffer));

  // Print the demangled symbol if demangling was successful
  if (success) {
    std::cout << "Demangled symbol: " << buffer << std::endl;
  } else {
    std::cout << "Demangling failed." << std::endl;
  }
}