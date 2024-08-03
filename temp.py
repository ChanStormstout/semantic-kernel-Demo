import re

# CFG内容
cfg_content = """
"1161176" [label = <(avifDiagnosticsClearError,avifDiagnosticsClearError(&amp;decoder-&gt;diag))<SUB>4121</SUB>> ]
"1161215" [label = <(avifDecoderCleanup,avifDecoderCleanup(decoder))<SUB>4133</SUB>> ]
"1161217" [label = <(&lt;operator&gt;.assignment,decoder-&gt;data = avifDecoderDataCreate())<SUB>4138</SUB>> ]
"1161222" [label = <(AVIF_CHECKERR,AVIF_CHECKERR(decoder-&gt;data != NULL, AVIF_RESUL...)<SUB>4139</SUB>> ]
"1161238" [label = <(&lt;operator&gt;.assignment,decoder-&gt;data-&gt;diag = &amp;decoder-&gt;diag)<SUB>4140</SUB>> ]
"1161248" [label = <(AVIF_CHECKRES,AVIF_CHECKRES(avifParse(decoder)))<SUB>4142</SUB>> ]
"1161269" [label = <(&lt;operator&gt;.assignment,* data = decoder-&gt;data)<SUB>4145</SUB>> ]
"1161486" [label = <(RETURN,return avifDecoderReset(decoder);,return avifDecoderReset(decoder);)<SUB>4189</SUB>> ]
"1161177" [label = <(&lt;operator&gt;.addressOf,&amp;decoder-&gt;diag)<SUB>4121</SUB>> ]
"1161182" [label = <(&lt;operator&gt;.logicalOr,(decoder-&gt;imageSizeLimit &gt; AVIF_DEFAULT_IMAGE_S...)<SUB>4125</SUB>> ]
"1161201" [label = <(&lt;operator&gt;.logicalOr,!decoder-&gt;io || !decoder-&gt;io-&gt;read)<SUB>4128</SUB>> ]
"1161218" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;data)<SUB>4138</SUB>> ]
"1161221" [label = <(avifDecoderDataCreate,avifDecoderDataCreate())<SUB>4138</SUB>> ]
"1161239" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;data-&gt;diag)<SUB>4140</SUB>> ]
"1161244" [label = <(&lt;operator&gt;.addressOf,&amp;decoder-&gt;diag)<SUB>4140</SUB>> ]
"1161249" [label = <(avifParse,avifParse(decoder))<SUB>4142</SUB>> ]
"1161271" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;data)<SUB>4145</SUB>> ]
"1161280" [label = <(&lt;operator&gt;.lessThan,itemIndex &lt; data-&gt;meta-&gt;items.count)<SUB>4146</SUB>> ]
"1161289" [label = <(&lt;operator&gt;.preIncrement,++itemIndex)<SUB>4146</SUB>> ]
"1161487" [label = <(avifDecoderReset,avifDecoderReset(decoder))<SUB>4189</SUB>> ]
"1161178" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;diag)<SUB>4121</SUB>> ]
"1161183" [label = <(&lt;operator&gt;.greaterThan,decoder-&gt;imageSizeLimit &gt; AVIF_DEFAULT_IMAGE_SI...)<SUB>4125</SUB>> ]
"1161192" [label = <(&lt;operator&gt;.equals,decoder-&gt;imageSizeLimit == 0)<SUB>4125</SUB>> ]
"1161198" [label = <(RETURN,return AVIF_RESULT_NOT_IMPLEMENTED;,return AVIF_RESULT_NOT_IMPLEMENTED;)<SUB>4126</SUB>> ]
"1161202" [label = <(&lt;operator&gt;.logicalNot,!decoder-&gt;io)<SUB>4128</SUB>> ]
"1161206" [label = <(&lt;operator&gt;.logicalNot,!decoder-&gt;io-&gt;read)<SUB>4128</SUB>> ]
"1161213" [label = <(RETURN,return AVIF_RESULT_IO_NOT_SET;,return AVIF_RESULT_IO_NOT_SET;)<SUB>4129</SUB>> ]
"1161220" [label = <(FIELD_IDENTIFIER,data,data)<SUB>4138</SUB>> ]
"1161240" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;data)<SUB>4140</SUB>> ]
"1161243" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4140</SUB>> ]
"1161245" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;diag)<SUB>4140</SUB>> ]
"1161273" [label = <(FIELD_IDENTIFIER,data,data)<SUB>4145</SUB>> ]
"1161277" [label = <(&lt;operator&gt;.assignment,itemIndex = 0)<SUB>4146</SUB>> ]
"1161282" [label = <(&lt;operator&gt;.fieldAccess,data-&gt;meta-&gt;items.count)<SUB>4146</SUB>> ]
"1161293" [label = <(&lt;operator&gt;.assignment,* item = data-&gt;meta-&gt;items.item[itemIndex])<SUB>4147</SUB>> ]
"1161318" [label = <(&lt;operator&gt;.assignment,isGrid = (memcmp(item-&gt;type, &quot;grid&quot;, 4) == 0))<SUB>4155</SUB>> ]
"1161341" [label = <(&lt;operator&gt;.assignment,* ispeProp = avifPropertyArrayFind(&amp;item-&gt;prope...)<SUB>4161</SUB>> ]
"1161180" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4121</SUB>> ]
"1161184" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;imageSizeLimit)<SUB>4125</SUB>> ]
"1161187" [label = <(AVIF_DEFAULT_IMAGE_SIZE_LIMIT,AVIF_DEFAULT_IMAGE_SIZE_LIMIT)<SUB>4125</SUB>> ]
"1161193" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;imageSizeLimit)<SUB>4125</SUB>> ]
"1161203" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;io)<SUB>4128</SUB>> ]
"1161207" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;io-&gt;read)<SUB>4128</SUB>> ]
"1161242" [label = <(FIELD_IDENTIFIER,data,data)<SUB>4140</SUB>> ]
"1161247" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4140</SUB>> ]
"1161283" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;meta-&gt;items)<SUB>4146</SUB>> ]
"1161288" [label = <(FIELD_IDENTIFIER,count,count)<SUB>4146</SUB>> ]
"1161295" [label = <(&lt;operator&gt;.indirectIndexAccess,data-&gt;meta-&gt;items.item[itemIndex])<SUB>4147</SUB>> ]
"1161305" [label = <(&lt;operator&gt;.logicalNot,!item-&gt;size)<SUB>4148</SUB>> ]
"1161312" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;hasUnsupportedEssentialProperty)<SUB>4151</SUB>> ]
"1161320" [label = <(&lt;operator&gt;.equals,memcmp(item-&gt;type, &quot;grid&quot;, 4) == 0)<SUB>4155</SUB>> ]
"1161329" [label = <(&lt;operator&gt;.logicalAnd,(avifGetCodecType(item-&gt;type) == AVIF_CODEC_TYP...)<SUB>4156</SUB>> ]
"1161343" [label = <(avifPropertyArrayFind,avifPropertyArrayFind(&amp;item-&gt;properties, &quot;ispe&quot;))<SUB>4161</SUB>> ]
"1161350" [label = <(IDENTIFIER,ispeProp,if (ispeProp))<SUB>4162</SUB>> ]
"1161186" [label = <(FIELD_IDENTIFIER,imageSizeLimit,imageSizeLimit)<SUB>4125</SUB>> ]
"1161195" [label = <(FIELD_IDENTIFIER,imageSizeLimit,imageSizeLimit)<SUB>4125</SUB>> ]
"1161205" [label = <(FIELD_IDENTIFIER,io,io)<SUB>4128</SUB>> ]
"1161208" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;io)<SUB>4128</SUB>> ]
"1161211" [label = <(FIELD_IDENTIFIER,read,read)<SUB>4128</SUB>> ]
"1161256" [label = <(&lt;operator&gt;.assignment,const avifResult)<SUB>4142</SUB>> ]
"1161284" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;meta)<SUB>4146</SUB>> ]
"1161287" [label = <(FIELD_IDENTIFIER,items,items)<SUB>4146</SUB>> ]
"1161296" [label = <(&lt;operator&gt;.fieldAccess,data-&gt;meta-&gt;items.item)<SUB>4147</SUB>> ]
"1161306" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;size)<SUB>4148</SUB>> ]
"1161314" [label = <(FIELD_IDENTIFIER,hasUnsupportedEssentialProperty,hasUnsupportedEssentialProperty)<SUB>4151</SUB>> ]
"1161321" [label = <(memcmp,memcmp(item-&gt;type, &quot;grid&quot;, 4))<SUB>4155</SUB>> ]
"1161330" [label = <(&lt;operator&gt;.equals,avifGetCodecType(item-&gt;type) == AVIF_CODEC_TYPE...)<SUB>4156</SUB>> ]
"1161336" [label = <(&lt;operator&gt;.logicalNot,!isGrid)<SUB>4156</SUB>> ]
"1161344" [label = <(&lt;operator&gt;.addressOf,&amp;item-&gt;properties)<SUB>4161</SUB>> ]
"1161352" [label = <(&lt;operator&gt;.assignment,item-&gt;width = ispeProp-&gt;u.ispe.width)<SUB>4163</SUB>> ]
"1161363" [label = <(&lt;operator&gt;.assignment,item-&gt;height = ispeProp-&gt;u.ispe.height)<SUB>4164</SUB>> ]
"1161189" [label = <(&lt;operator&gt;.multiplication,16384 * 16384)<SUB>4125</SUB>> ]
"1161210" [label = <(FIELD_IDENTIFIER,io,io)<SUB>4128</SUB>> ]
"1161228" [label = <(&lt;operator&gt;.logicalNot,!(decoder-&gt;data != NULL))<SUB>4139</SUB>> ]
"1161258" [label = <(avifParse,avifParse(decoder))<SUB>4142</SUB>> ]
"1161261" [label = <(&lt;operator&gt;.notEquals,result__ != AVIF_RESULT_OK)<SUB>4142</SUB>> ]
"1161286" [label = <(FIELD_IDENTIFIER,meta,meta)<SUB>4146</SUB>> ]
"1161297" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;meta-&gt;items)<SUB>4147</SUB>> ]
"1161302" [label = <(FIELD_IDENTIFIER,item,item)<SUB>4147</SUB>> ]
"1161308" [label = <(FIELD_IDENTIFIER,size,size)<SUB>4148</SUB>> ]
"1161322" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;type)<SUB>4155</SUB>> ]
"1161331" [label = <(avifGetCodecType,avifGetCodecType(item-&gt;type))<SUB>4156</SUB>> ]
"1161345" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;properties)<SUB>4161</SUB>> ]
"1161353" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;width)<SUB>4163</SUB>> ]
"1161356" [label = <(&lt;operator&gt;.fieldAccess,ispeProp-&gt;u.ispe.width)<SUB>4163</SUB>> ]
"1161364" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;height)<SUB>4164</SUB>> ]
"1161367" [label = <(&lt;operator&gt;.fieldAccess,ispeProp-&gt;u.ispe.height)<SUB>4164</SUB>> ]
"1161375" [label = <(&lt;operator&gt;.logicalOr,(item-&gt;width == 0) || (item-&gt;height == 0))<SUB>4166</SUB>> ]
"1161404" [label = <(avifDimensionsTooLarge,avifDimensionsTooLarge(item-&gt;width, item-&gt;heigh...)<SUB>4170</SUB>> ]
"1161437" [label = <(&lt;operator&gt;.assignment,* auxCProp = avifPropertyArrayFind(&amp;item-&gt;prope...)<SUB>4175</SUB>> ]
"1161229" [label = <(&lt;operator&gt;.notEquals,decoder-&gt;data != NULL)<SUB>4139</SUB>> ]
"1161235" [label = <(RETURN,AVIF_CHECKERR(decoder-&gt;data != NULL, AVIF_RESUL...,AVIF_CHECKERR(decoder-&gt;data != NULL, AVIF_RESUL...)<SUB>4139</SUB>> ]
"1161265" [label = <(RETURN,AVIF_CHECKRES(avifParse(decoder)),AVIF_CHECKRES(avifParse(decoder)))<SUB>4142</SUB>> ]
"1161298" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;meta)<SUB>4147</SUB>> ]
"1161301" [label = <(FIELD_IDENTIFIER,items,items)<SUB>4147</SUB>> ]
"1161324" [label = <(FIELD_IDENTIFIER,type,type)<SUB>4155</SUB>> ]
"1161332" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;type)<SUB>4156</SUB>> ]
"1161347" [label = <(FIELD_IDENTIFIER,properties,properties)<SUB>4161</SUB>> ]
"1161355" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4163</SUB>> ]
"1161357" [label = <(&lt;operator&gt;.fieldAccess,ispeProp-&gt;u.ispe)<SUB>4163</SUB>> ]
"1161362" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4163</SUB>> ]
"1161366" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4164</SUB>> ]
"1161368" [label = <(&lt;operator&gt;.fieldAccess,ispeProp-&gt;u.ispe)<SUB>4164</SUB>> ]
"1161373" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4164</SUB>> ]
"1161376" [label = <(&lt;operator&gt;.equals,item-&gt;width == 0)<SUB>4166</SUB>> ]
"1161381" [label = <(&lt;operator&gt;.equals,item-&gt;height == 0)<SUB>4166</SUB>> ]
"1161387" [label = <(avifDiagnosticsPrintf,avifDiagnosticsPrintf(data-&gt;diag, &quot;Item ID [%u]...)<SUB>4167</SUB>> ]
"1161401" [label = <(RETURN,return AVIF_RESULT_BMFF_PARSE_FAILED;,return AVIF_RESULT_BMFF_PARSE_FAILED;)<SUB>4168</SUB>> ]
"1161405" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;width)<SUB>4170</SUB>> ]
"1161408" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;height)<SUB>4170</SUB>> ]
"1161411" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;imageSizeLimit)<SUB>4170</SUB>> ]
"1161414" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;imageDimensionLimit)<SUB>4170</SUB>> ]
"1161418" [label = <(avifDiagnosticsPrintf,avifDiagnosticsPrintf(data-&gt;diag, &quot;Item ID [%u]...)<SUB>4171</SUB>> ]
"1161432" [label = <(RETURN,return AVIF_RESULT_BMFF_PARSE_FAILED;,return AVIF_RESULT_BMFF_PARSE_FAILED;)<SUB>4172</SUB>> ]
"1161439" [label = <(avifPropertyArrayFind,avifPropertyArrayFind(&amp;item-&gt;properties, &quot;auxC&quot;))<SUB>4175</SUB>> ]
"1161446" [label = <(&lt;operator&gt;.logicalAnd,auxCProp &amp;&amp; isAlphaURN(auxCProp-&gt;u.auxC.auxType))<SUB>4176</SUB>> ]
"1161230" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;data)<SUB>4139</SUB>> ]
"1161300" [label = <(FIELD_IDENTIFIER,meta,meta)<SUB>4147</SUB>> ]
"1161334" [label = <(FIELD_IDENTIFIER,type,type)<SUB>4156</SUB>> ]
"1161358" [label = <(&lt;operator&gt;.indirectFieldAccess,ispeProp-&gt;u)<SUB>4163</SUB>> ]
"1161361" [label = <(FIELD_IDENTIFIER,ispe,ispe)<SUB>4163</SUB>> ]
"1161369" [label = <(&lt;operator&gt;.indirectFieldAccess,ispeProp-&gt;u)<SUB>4164</SUB>> ]
"1161372" [label = <(FIELD_IDENTIFIER,ispe,ispe)<SUB>4164</SUB>> ]
"1161377" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;width)<SUB>4166</SUB>> ]
"1161382" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;height)<SUB>4166</SUB>> ]
"1161388" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;diag)<SUB>4167</SUB>> ]
"1161392" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;id)<SUB>4167</SUB>> ]
"1161395" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;width)<SUB>4167</SUB>> ]
"1161398" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;height)<SUB>4167</SUB>> ]
"1161407" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4170</SUB>> ]
"1161410" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4170</SUB>> ]
"1161413" [label = <(FIELD_IDENTIFIER,imageSizeLimit,imageSizeLimit)<SUB>4170</SUB>> ]
"1161416" [label = <(FIELD_IDENTIFIER,imageDimensionLimit,imageDimensionLimit)<SUB>4170</SUB>> ]
"1161419" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;diag)<SUB>4171</SUB>> ]
"1161423" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;id)<SUB>4171</SUB>> ]
"1161426" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;width)<SUB>4171</SUB>> ]
"1161429" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;height)<SUB>4171</SUB>> ]
"1161440" [label = <(&lt;operator&gt;.addressOf,&amp;item-&gt;properties)<SUB>4175</SUB>> ]
"1161448" [label = <(isAlphaURN,isAlphaURN(auxCProp-&gt;u.auxC.auxType))<SUB>4176</SUB>> ]
"1161232" [label = <(FIELD_IDENTIFIER,data,data)<SUB>4139</SUB>> ]
"1161360" [label = <(FIELD_IDENTIFIER,u,u)<SUB>4163</SUB>> ]
"1161371" [label = <(FIELD_IDENTIFIER,u,u)<SUB>4164</SUB>> ]
"1161379" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4166</SUB>> ]
"1161384" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4166</SUB>> ]
"1161390" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4167</SUB>> ]
"1161394" [label = <(FIELD_IDENTIFIER,id,id)<SUB>4167</SUB>> ]
"1161397" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4167</SUB>> ]
"1161400" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4167</SUB>> ]
"1161421" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4171</SUB>> ]
"1161425" [label = <(FIELD_IDENTIFIER,id,id)<SUB>4171</SUB>> ]
"1161428" [label = <(FIELD_IDENTIFIER,width,width)<SUB>4171</SUB>> ]
"1161431" [label = <(FIELD_IDENTIFIER,height,height)<SUB>4171</SUB>> ]
"1161441" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;properties)<SUB>4175</SUB>> ]
"1161449" [label = <(&lt;operator&gt;.fieldAccess,auxCProp-&gt;u.auxC.auxType)<SUB>4176</SUB>> ]
"1161458" [label = <(&lt;operator&gt;.and,decoder-&gt;strictFlags &amp; AVIF_STRICT_ALPHA_ISPE_R...)<SUB>4177</SUB>> ]
"1161476" [label = <(avifDiagnosticsPrintf,avifDiagnosticsPrintf(data-&gt;diag, &quot;Item ID [%u]...)<SUB>4184</SUB>> ]
"1161484" [label = <(RETURN,return AVIF_RESULT_BMFF_PARSE_FAILED;,return AVIF_RESULT_BMFF_PARSE_FAILED;)<SUB>4185</SUB>> ]
"1161443" [label = <(FIELD_IDENTIFIER,properties,properties)<SUB>4175</SUB>> ]
"1161450" [label = <(&lt;operator&gt;.fieldAccess,auxCProp-&gt;u.auxC)<SUB>4176</SUB>> ]
"1161455" [label = <(FIELD_IDENTIFIER,auxType,auxType)<SUB>4176</SUB>> ]
"1161459" [label = <(&lt;operator&gt;.indirectFieldAccess,decoder-&gt;strictFlags)<SUB>4177</SUB>> ]
"1161464" [label = <(avifDiagnosticsPrintf,avifDiagnosticsPrintf(data-&gt;diag,
             ...)<SUB>4178</SUB>> ]
"1161472" [label = <(RETURN,return AVIF_RESULT_BMFF_PARSE_FAILED;,return AVIF_RESULT_BMFF_PARSE_FAILED;)<SUB>4181</SUB>> ]
"1161477" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;diag)<SUB>4184</SUB>> ]
"1161481" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;id)<SUB>4184</SUB>> ]
"1161451" [label = <(&lt;operator&gt;.indirectFieldAccess,auxCProp-&gt;u)<SUB>4176</SUB>> ]
"1161454" [label = <(FIELD_IDENTIFIER,auxC,auxC)<SUB>4176</SUB>> ]
"1161461" [label = <(FIELD_IDENTIFIER,strictFlags,strictFlags)<SUB>4177</SUB>> ]
"1161465" [label = <(&lt;operator&gt;.indirectFieldAccess,data-&gt;diag)<SUB>4178</SUB>> ]
"1161469" [label = <(&lt;operator&gt;.indirectFieldAccess,item-&gt;id)<SUB>4180</SUB>> ]
"1161479" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4184</SUB>> ]
"1161483" [label = <(FIELD_IDENTIFIER,id,id)<SUB>4184</SUB>> ]
"1161453" [label = <(FIELD_IDENTIFIER,u,u)<SUB>4176</SUB>> ]
"1161467" [label = <(FIELD_IDENTIFIER,diag,diag)<SUB>4178</SUB>> ]
"1161471" [label = <(FIELD_IDENTIFIER,id,id)<SUB>4180</SUB>> ]
"1161173" [label = <(METHOD,avifDecoderParse)<SUB>4119</SUB>> ]
"1161489" [label = <(METHOD_RETURN,avifResult)<SUB>4119</SUB>> ]
  "1161176" -> "1161186" 
  "1161215" -> "1161220" 
  "1161217" -> "1161222" 
  "1161222" -> "1161232" 
  "1161222" -> "1161242" 
  "1161238" -> "1161249" 
  "1161248" -> "1161258" 
  "1161248" -> "1161273" 
  "1161269" -> "1161277" 
  "1161486" -> "1161489" 
  "1161177" -> "1161176" 
  "1161182" -> "1161198" 
  "1161182" -> "1161205" 
  "1161201" -> "1161213" 
  "1161201" -> "1161215" 
  "1161218" -> "1161221" 
  "1161221" -> "1161217" 
  "1161239" -> "1161247" 
  "1161244" -> "1161238" 
  "1161249" -> "1161248" 
  "1161271" -> "1161269" 
  "1161280" -> "1161300" 
  "1161280" -> "1161487" 
  "1161289" -> "1161286" 
  "1161487" -> "1161486" 
  "1161178" -> "1161177" 
  "1161183" -> "1161182" 
  "1161183" -> "1161195" 
  "1161192" -> "1161182" 
  "1161198" -> "1161489" 
  "1161202" -> "1161201" 
  "1161202" -> "1161210" 
  "1161206" -> "1161201" 
  "1161213" -> "1161489" 
  "1161220" -> "1161218" 
  "1161240" -> "1161243" 
  "1161243" -> "1161239" 
  "1161245" -> "1161244" 
  "1161273" -> "1161271" 
  "1161277" -> "1161286" 
  "1161282" -> "1161280" 
  "1161293" -> "1161308" 
  "1161318" -> "1161334" 
  "1161341" -> "1161350" 
  "1161180" -> "1161178" 
  "1161184" -> "1161187" 
  "1161187" -> "1161183" 
  "1161187" -> "1161189" 
  "1161193" -> "1161192" 
  "1161203" -> "1161202" 
  "1161207" -> "1161206" 
  "1161242" -> "1161240" 
  "1161247" -> "1161245" 
  "1161283" -> "1161288" 
  "1161288" -> "1161282" 
  "1161295" -> "1161293" 
  "1161305" -> "1161289" 
  "1161305" -> "1161314" 
  "1161312" -> "1161289" 
  "1161312" -> "1161324" 
  "1161320" -> "1161318" 
  "1161329" -> "1161289" 
  "1161329" -> "1161347" 
  "1161343" -> "1161341" 
  "1161350" -> "1161355" 
  "1161350" -> "1161443" 
  "1161186" -> "1161184" 
  "1161195" -> "1161193" 
  "1161205" -> "1161203" 
  "1161208" -> "1161211" 
  "1161211" -> "1161207" 
  "1161256" -> "1161261" 
  "1161284" -> "1161287" 
  "1161287" -> "1161283" 
  "1161296" -> "1161295" 
  "1161306" -> "1161305" 
  "1161314" -> "1161312" 
  "1161321" -> "1161320" 
  "1161330" -> "1161329" 
  "1161330" -> "1161336" 
  "1161336" -> "1161329" 
  "1161344" -> "1161343" 
  "1161352" -> "1161366" 
  "1161363" -> "1161379" 
  "1161189" -> "1161183" 
  "1161210" -> "1161208" 
  "1161228" -> "1161232" 
  "1161228" -> "1161242" 
  "1161228" -> "1161235" 
  "1161258" -> "1161256" 
  "1161261" -> "1161258" 
  "1161261" -> "1161273" 
  "1161261" -> "1161265" 
  "1161286" -> "1161284" 
  "1161297" -> "1161302" 
  "1161302" -> "1161296" 
  "1161308" -> "1161306" 
  "1161322" -> "1161321" 
  "1161331" -> "1161330" 
  "1161345" -> "1161344" 
  "1161353" -> "1161360" 
  "1161356" -> "1161352" 
  "1161364" -> "1161371" 
  "1161367" -> "1161363" 
  "1161375" -> "1161390" 
  "1161375" -> "1161407" 
  "1161404" -> "1161421" 
  "1161404" -> "1161289" 
  "1161437" -> "1161446" 
  "1161437" -> "1161453" 
  "1161229" -> "1161228" 
  "1161235" -> "1161489" 
  "1161265" -> "1161489" 
  "1161298" -> "1161301" 
  "1161301" -> "1161297" 
  "1161324" -> "1161322" 
  "1161332" -> "1161331" 
  "1161347" -> "1161345" 
  "1161355" -> "1161353" 
  "1161357" -> "1161362" 
  "1161362" -> "1161356" 
  "1161366" -> "1161364" 
  "1161368" -> "1161373" 
  "1161373" -> "1161367" 
  "1161376" -> "1161375" 
  "1161376" -> "1161384" 
  "1161381" -> "1161375" 
  "1161387" -> "1161401" 
  "1161401" -> "1161489" 
  "1161405" -> "1161410" 
  "1161408" -> "1161413" 
  "1161411" -> "1161416" 
  "1161414" -> "1161404" 
  "1161418" -> "1161432" 
  "1161432" -> "1161489" 
  "1161439" -> "1161437" 
  "1161446" -> "1161461" 
  "1161446" -> "1161479" 
  "1161230" -> "1161229" 
  "1161300" -> "1161298" 
  "1161334" -> "1161332" 
  "1161358" -> "1161361" 
  "1161361" -> "1161357" 
  "1161369" -> "1161372" 
  "1161372" -> "1161368" 
  "1161377" -> "1161376" 
  "1161382" -> "1161381" 
  "1161388" -> "1161394" 
  "1161392" -> "1161397" 
  "1161395" -> "1161400" 
  "1161398" -> "1161387" 
  "1161407" -> "1161405" 
  "1161410" -> "1161408" 
  "1161413" -> "1161411" 
  "1161416" -> "1161414" 
  "1161419" -> "1161425" 
  "1161423" -> "1161428" 
  "1161426" -> "1161431" 
  "1161429" -> "1161418" 
  "1161440" -> "1161439" 
  "1161448" -> "1161446" 
  "1161232" -> "1161230" 
  "1161360" -> "1161358" 
  "1161371" -> "1161369" 
  "1161379" -> "1161377" 
  "1161384" -> "1161382" 
  "1161390" -> "1161388" 
  "1161394" -> "1161392" 
  "1161397" -> "1161395" 
  "1161400" -> "1161398" 
  "1161421" -> "1161419" 
  "1161425" -> "1161423" 
  "1161428" -> "1161426" 
  "1161431" -> "1161429" 
  "1161441" -> "1161440" 
  "1161449" -> "1161448" 
  "1161458" -> "1161467" 
  "1161458" -> "1161289" 
  "1161476" -> "1161484" 
  "1161484" -> "1161489" 
  "1161443" -> "1161441" 
  "1161450" -> "1161455" 
  "1161455" -> "1161449" 
  "1161459" -> "1161458" 
  "1161464" -> "1161472" 
  "1161472" -> "1161489" 
  "1161477" -> "1161483" 
  "1161481" -> "1161476" 
  "1161451" -> "1161454" 
  "1161454" -> "1161450" 
  "1161461" -> "1161459" 
  "1161465" -> "1161471" 
  "1161469" -> "1161464" 
  "1161479" -> "1161477" 
  "1161483" -> "1161481" 
  "1161453" -> "1161451" 
  "1161467" -> "1161465" 
  "1161471" -> "1161469" 
  "1161173" -> "1161180" 
}
"""

# 正则表达式来解析节点和边
node_pattern = re.compile(r'\"(\d+)\"\s+\[label\s+=\s+<\(([^>]+)\)')
edge_pattern = re.compile(r'\"(\d+)\"\s+->\s+\"(\d+)\"')

# 解析节点，存储id和label的映射
nodes = {}
for match in node_pattern.finditer(cfg_content):
    node_id, label = match.groups()
    nodes[node_id] = label

# 解析边，使用节点的label替换id
edges = []
for match in edge_pattern.finditer(cfg_content):
    source_id, target_id = match.groups()
    source_label = nodes[source_id]
    target_label = nodes[target_id]
    edges.append(f'("{source_label}") -> ("{target_label}")')

# 输出结果
for edge in edges:
    print(edge)
