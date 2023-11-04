int LLVMFuzzerTestOneInput(const uint8_t* data, size_t size)
{
    // ... [其他代码]

    // 创建一个新的libspng上下文。SPNG_CTX_IGNORE_ADLER32选项告诉libspng忽略ADLER-32校验和（这对于某些PNG文件是必要的）
    spng_ctx *ctx = spng_ctx_new(SPNG_CTX_IGNORE_ADLER32);
    // 如果无法创建上下文，则立即返回
    if(ctx == NULL) return 0;

    // ... [设置解码参数和其他上下文选项]

    size_t out_size;

    // 调用spng_decoded_image_size来预估解码后的图像数据所需的大小
    if(spng_decoded_image_size(ctx, fmt, &out_size)) goto err;

    // 如果预估的输出大小超过了预定义的上限（这里是80MB），则为了避免分配太多内存和潜在的DoS攻击，终止处理并跳转到错误处理
    if(out_size > 80000000) goto err;

    // 根据预估的大小为解码的图像数据分配内存
    out = (unsigned char*)malloc(out_size);
    // 如果内存分配失败，则跳转到错误处理
    if(out == NULL) goto err;

    // ... [获取其他块信息]

    // 根据progressive标志决定如何进行解码
    if(progressive)
    {
        // 如果是渐进式PNG，则使用另一种方法进行逐行解码，这里并没有直接调用spng_decode_image()
        // ... [逐行解码的代码]
    }
    else 
    {
        // 对整个图像进行解码。这是我们关心的部分，因为它直接调用了spng_decode_image()
        if(spng_decode_image(ctx, out, out_size, fmt, flags)) goto err;
    }

    // ... [处理其他块和数据]

err:
    // 错误处理部分，释放所有分配的资源
    spng_ctx_free(ctx);
    free(out);

    return 0;
}
