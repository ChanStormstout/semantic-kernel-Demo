import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion

kernel = sk.Kernel()
# Configure AI service used by the kernel
api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", api_key, org_id))

sk_prompt = """
ChatBot can have a conversation with you about any topic.
It can give explicit instructions or say 'I don't know' if it does not have an answer.

{{$history}}
User: {{$user_input}}
ChatBot: """

chat_function = kernel.create_semantic_function(sk_prompt, "ChatBot", max_tokens=2000, temperature=0.7, top_p=0.5)
# initialize the context
context = kernel.create_new_context()
context["history"] = ""

# define the texts
text_1 = """
Given the following code:
#ifndef LESSONS_04_VULNERABLE_FUNCTIONS_H_
#define LESSONS_04_VULNERABLE_FUNCTIONS_H_

#include <stdint.h>
#include <stddef.h>
#include <cstring>

#include <array>
#include <string>
#include <vector>


bool VulnerableFunction1(const uint8_t* data, size_t size) {
  bool result = false;
  if (size >= 3) {
    result = data[0] == 'F' &&
             data[1] == 'U' &&
             data[2] == 'Z' &&
             data[3] == 'Z';
  }

  return result;
}


template<class T>
typename T::value_type DummyHash(const T& buffer) {
  typename T::value_type hash = 0;
  for (auto value : buffer)
    hash ^= value;

  return hash;
}

constexpr auto kMagicHeader = "ZN_2016";
constexpr std::size_t kMaxPacketLen = 1024;
constexpr std::size_t kMaxBodyLength = 1024 - sizeof(kMagicHeader);



constexpr std::size_t kZn2016VerifyHashFlag = 0x0001000;

bool VulnerableFunction3(const uint8_t* data, size_t size, std::size_t flags) {
  bool verify_hash = flags & kZn2016VerifyHashFlag;
  return VulnerableFunction3(data, size, verify_hash);
}


#endif // LESSONS_04_VULNERABLE_FUNCTIONS_H_
}

Your task is to analyze the provided code snippet. Please provide a clear and concise response that explains the purpose of the code, and its key components.

Please note that your analysis should be flexible enough to accommodate different types of code snippets, such as functions, classes, or algorithms. You should focus on providing a thorough and accurate assessment of the code, highlighting both its strengths and weaknesses.
"""

text_2 = """
Please analyze the VulnerableFunction1 function in the provided code. Your task is to determine the type of input parameters it accepts and the type of output it produces. Please provide a clear and concise response that accurately describes the input parameter type(s) and the output type of the VulnerableFunction1 function.

Please note that your response should be based on a careful analysis of the code provided.
"""

text_3 = """
Please create an function in C language that can invoke the VulnerableFunction1 function. The function should have the same input parameter of type as the VulnerableFunction1 function,and should return a result of type bool.

Your generated function should take the input parameter and perform the necessary operations to generate a result value. The specific implementation details and logic of the function should be based on the behavior of the VulnerableFunction1 function.

Please ensure that your generated function adheres to the requirements stated above and follows best practices for writing secure and efficient code.
"""
text_4 = """
Hello AI Assistant,

Now, I also need you to infer a function which can invoke `VulnerableFunction3` function. Please note that the `VulnerableFunction3` function has additional input parameters that accept a size_t variable.
"""
dwg_text1 = """
Analyze the following code : 
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2021 Free Software Foundation, Inc.                        */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * llvmfuzz.c: libfuzzer testing, esp. for oss-fuzz. with libfuzzer or
 * standalone written by Reini Urban
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
//#include <unistd.h>
#include <sys/stat.h>

#include <dwg.h>
#include "common.h"
#include "decode.h"
#include "encode.h"
#include "bits.h"
#ifndef DISABLE_DXF
#  include "out_dxf.h"
#  ifndef DISABLE_JSON
#    include "in_json.h"
#    include "out_json.h"
#  endif
#  include "in_dxf.h"
#endif

extern int LLVMFuzzerTestOneInput (const unsigned char *data, size_t size);

// libfuzzer limitation:
// Enforce NULL-termination of the input buffer, to avoid bogus reports. copy
// it. Problematic is mostly strtol(3) which also works with \n termination.
static int
enforce_null_termination (Bit_Chain *dat, bool enforce)
{
  unsigned char *copy;
  unsigned char c;
  if (!dat->size)
    return 0;
  c = dat->chain[dat->size - 1];
  // Allow \n termination without \0 in DXF? No, still crashes
  if (!enforce && ((c == '\n' && c + 1 == '\0') || c == '\0'))
    return 0;
#ifdef STANDALONE
  fprintf (stderr,
           "llvmfuzz_standalone: enforce libfuzzer buffer NULL termination\n");
#endif
  copy = malloc (dat->size + 1);
  memcpy (copy, dat->chain, dat->size);
  copy[dat->size] = '\0';
  dat->chain = copy;
  return 1;
}

int
LLVMFuzzerTestOneInput (const unsigned char *data, size_t size)
{
  Dwg_Data dwg;
  Bit_Chain dat = { NULL, 0, 0, 0, 0 };
  Bit_Chain out_dat = { NULL, 0, 0, 0, 0 };
  int copied = 0;
  struct ly_ctx *ctx = NULL;
  unsigned int possible_outputformats;
  int out;

  static char tmp_file[256];
  dat.chain = (unsigned char *)data;
  dat.size = size;
  memset (&dwg, 0, sizeof (dwg));

  possible_outputformats =
#ifdef DISABLE_DXF
#  ifdef DISABLE_JSON
      1;
#  else
      3;
#  endif
#else
      5;
#endif

  // Detect the input format: DWG, DXF or JSON
  if (dat.size > 2 && dat.chain[0] == 'A' && dat.chain[1] == 'C')
    {
      if (dwg_decode (&dat, &dwg) >= DWG_ERR_CRITICAL)
        {
          dwg_free (&dwg);
          return 0;
        }
    }
#ifndef DISABLE_JSON
  else if (dat.size > 1 && dat.chain[0] == '{')
    {
      copied = enforce_null_termination (&dat, true);
      if (dwg_read_json (&dat, &dwg) >= DWG_ERR_CRITICAL)
        {
          if (copied)
            bit_chain_free (&dat);
          dwg_free (&dwg);
          return 0;
        }
      dat.opts |= DWG_OPTS_INJSON;
      dwg.opts |= DWG_OPTS_INJSON;
    }
#endif
#ifndef DISABLE_DXF
  else
    {
      copied = enforce_null_termination (&dat, false);
      if (dwg_read_dxf (&dat, &dwg) >= DWG_ERR_CRITICAL)
        {
          if (copied)
            bit_chain_free (&dat);
          dwg_free (&dwg);
          return 0;
        }
    }
#else
  else
    return 0;
#endif

  memset (&out_dat, 0, sizeof (out_dat));
  bit_chain_set_version (&out_dat, &dat);
  if (copied)
    bit_chain_free (&dat);

#if 0
    snprintf (tmp_file, 255, "/tmp/llvmfuzzer%d.out", getpid());
    tmp_file[255] = '\0';
#elif defined _WIN32
  strcpy (tmp_file, "NUL");
#else
  strcpy (tmp_file, "/dev/null");
#endif
  out_dat.fh = fopen (tmp_file, "w");

  out = rand () % possible_outputformats;
#ifdef STANDALONE
  if (getenv ("OUT"))
    out = strtol (getenv ("OUT"), NULL, 10);
#endif
  switch (out)
    {
    case 0:
      {
        int ver = rand () % 6;
#ifdef STANDALONE
        if (getenv ("VER"))
          ver = strtol (getenv ("VER"), NULL, 10);
#endif
        switch (ver)
          {
          case 0:
            out_dat.version = dwg.header.version = R_13;
            break;
          case 1:
            out_dat.version = dwg.header.version = R_13c3;
            break;
          case 2:
            out_dat.version = dwg.header.version = R_14;
            break;
          case 3: // favor this one
          case 4:
          case 5:
          default:
            out_dat.version = dwg.header.version = R_2000;
            break;
          }
        dwg_encode (&dwg, &out_dat);
        free (out_dat.chain);
        break;
      }
#ifndef DISABLE_DXF
    case 1:
      dwg_write_dxf (&out_dat, &dwg);
      free (out_dat.chain);
      break;
    case 2: // experimental
      dwg_write_dxfb (&out_dat, &dwg);
      free (out_dat.chain);
      break;
#  ifndef DISABLE_JSON
    case 3:
      dwg_write_json (&out_dat, &dwg);
      free (out_dat.chain);
      break;
    case 4:
      dwg_write_geojson (&out_dat, &dwg);
      free (out_dat.chain);
      break;
#  endif
#endif
    default:
      break;
    }
  dwg_free (&dwg);
  fclose (out_dat.fh);
  // unlink (tmp_file);
  return 0;
}

#ifdef STANDALONE
/*
# ifdef __GNUC__
__attribute__((weak))
# endif
extern int LLVMFuzzerInitialize(int *argc, char ***argv);
*/

static int
usage (void)
{
  printf ("\nUsage: OUT=0 VER=3 llvmfuzz_standalone INPUT...");
  return 1;
}
// llvmfuzz_standalone reproducer, see OUT and VER env vars
int
main (int argc, char *argv[])
{
  if (argc <= 1 || !*argv[1])
    return usage ();
  /* works only on linux
  if (LLVMFuzzerInitialize)
    LLVMFuzzerInitialize (&argc, &argv);
  */
  for (int i = 1; i < argc; i++)
    {
      unsigned char *buf;
      FILE *f = fopen (argv[i], "rb");
      struct stat attrib;
      long len;
      size_t n_read;
      int fd;
      if (!f)
        {
          fprintf (stderr, "Illegal file argument %s\n", argv[i]);
          continue;
        }
      fd = fileno (f);
      if (fd < 0 || fstat (fd, &attrib)
          || !(S_ISREG (attrib.st_mode)
#  ifndef _WIN32
               || S_ISLNK (attrib.st_mode)
#  endif
                   ))
        {
          fprintf (stderr, "Illegal input file \"%s\"\n", argv[i]);
          continue;
        }
      // libFuzzer design bug, not zero-terminating its text buffer
      fseek (f, 0, SEEK_END);
      len = ftell (f);
      fseek (f, 0, SEEK_SET);
      if (len <= 0)
        continue;
      buf = (unsigned char *)malloc (len);
      n_read = fread (buf, 1, len, f);
      fclose (f);
      assert ((long)n_read == len);
      fprintf (stderr, "llvmfuzz_standalone %s [%zu]\n", argv[i], len);
      LLVMFuzzerTestOneInput (buf, len);
      free (buf);
      // Bit_Chain dat = { 0 };
      // dat_read_file (&dat, fp, argv[i]);
      // LLVMFuzzerTestOneInput (dat.chain, dat.size);
      // bit_free_chain (&dat);
    }
}
#endif

"""

dwg_text2 = """
Generate a function that can detect if the input format is DWG in C language.
The function should accept two input parameters of type as `const unsigned char *` and `size_t`. 
If it is DWG, return 1; if not, return 0.
"""

dwg_text3 = """
Generate a function that accept the result above and try to decode the input.
"""

libspng_text1 = """
Generate a function called LLVMFuzzerTestOneInput, which accpets a `const uint8_t*` and a `size_t` parameter as the inputs, 
and be able to invoke the function `spng_decode_image`.

Here's the decription of function `spng_decode_image`:
# spng_decode_image()
```c
int spng_decode_image(spng_ctx *ctx, void *out, size_t len, int fmt, int flags)
```

Decodes the PNG file and writes the image to `out`,
the image is converted from the PNG format to the destination format `fmt`.

Interlaced images are deinterlaced, 16-bit images are converted to host-endian.

`out` must point to a buffer of length `len`.

`len` must be equal to or greater than the number calculated with
`spng_decoded_image_size()` with the same output format.

If the `SPNG_DECODE_PROGRESSIVE` flag is set the decoder will be
initialized with `fmt` and `flags` for progressive decoding,
the values of `out`, `len` are ignored.

The `SPNG_DECODE_TRNS` flag is silently ignored if the PNG does not
contain a tRNS chunk or is not applicable for the color type.

This function can only be called once per context.

The information about `spng_decode_image` in the README.md is as follows:
/* Decode to 8-bit RGBA */
spng_decode_image(ctx, out, out_size, SPNG_FMT_RGBA8, 0);

And another example of its usage in example.c is as follows:
/* With SPNG_FMT_PNG indexed color images are output as palette indices,
       pick another format to expand them. */
    if(ihdr.color_type == SPNG_COLOR_TYPE_INDEXED) fmt = SPNG_FMT_RGB8;

    ret = spng_decoded_image_size(ctx, fmt, &image_size);

    if(ret) goto error;

    image = malloc(image_size);

    if(image == NULL) goto error;

    /* Decode the image in one go */
    /* ret = spng_decode_image(ctx, image, image_size, SPNG_FMT_RGBA8, 0);

    if(ret)
    {
        printf("spng_decode_image() error: %s\n", spng_strerror(ret));
        goto error;
    }*/

    /* Alternatively you can decode the image progressively,
       this requires an initialization step. */
    ret = spng_decode_image(ctx, NULL, 0, fmt, SPNG_DECODE_PROGRESSIVE);

    if(ret)
    {
        printf("progressive spng_decode_image() error: %s\n", spng_strerror(ret));
        goto error;
    }
"""


# define async function
async def chat(input_text: str) -> None:
    # Save new message in the context variables
    print(f"\033[93mUser: {input_text}\033[0m")
    context["user_input"] = input_text

    # Process the user message and get an answer
    answer = await chat_function.invoke_async(context=context)

    # Show the response
    print(f"\033[32mChatBot: {answer}\n\033[0m")

    # Append the new interaction to the chat history
    context["history"] += f"\nUser: {input_text}\nChatBot: {answer}\n"

async def main():
    # user_input1 = input("")
    # user_input2 = input("input2: ")
    # user_input3 = input("input3: ")
    # user_input4 = input("input4: ")
    await chat(libspng_text1)
    # await chat(libspng_text2)
    #await chat(user_input2)
    #await chat(user_input3)
    #await chat(user_input4)

# 使用 asyncio.run 运行 main 协程
asyncio.run(main())

# 先成功调用这个函数
# 成功调用a, 调用b, 调用C
# 假设有了dependency
