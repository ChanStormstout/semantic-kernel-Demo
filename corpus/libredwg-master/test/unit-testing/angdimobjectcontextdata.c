// TODO DEBUGGING
#define DWG_TYPE DWG_TYPE_ANGDIMOBJECTCONTEXTDATA
#include "common.c"

void
api_process (dwg_object *obj)
{
  int error, isnew;
  ANNOTSCALEOBJECTCONTEXTDATA_fields;
  Dwg_OCD_Dimension dimension;
  BITCODE_3BD arc_pt;

  Dwg_Version_Type dwg_version = obj->parent->header.version;
#ifdef DEBUG_CLASSES
  dwg_obj_angdimobjectcontextdata *_obj
      = dwg_object_to_ANGDIMOBJECTCONTEXTDATA (obj);

  CHK_ENTITY_TYPE (_obj, ANGDIMOBJECTCONTEXTDATA, class_version, BS);
  CHK_ENTITY_TYPE (_obj, ANGDIMOBJECTCONTEXTDATA, is_default, B);
  CHK_ENTITY_H (_obj, ANGDIMOBJECTCONTEXTDATA, scale);

  CHK_SUBCLASS_2RD (_obj->dimension, OCD_Dimension, def_pt);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, b293, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, is_def_textloc, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, text_rotation, BD);
  CHK_SUBCLASS_H (_obj->dimension, OCD_Dimension, block);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, dimtofl, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, dimosxd, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, dimatfit, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, dimtix, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, dimtmove, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, override_code, RC);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, has_arrow2, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, flip_arrow2, B);
  CHK_SUBCLASS_TYPE (_obj->dimension, OCD_Dimension, flip_arrow1, B);

  CHK_ENTITY_3RD (_obj, ANGDIMOBJECTCONTEXTDATA, arc_pt);
#endif
}
