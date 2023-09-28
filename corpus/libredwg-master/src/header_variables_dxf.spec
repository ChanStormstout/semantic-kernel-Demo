/* -*- c -*- */
/*****************************************************************************/
/*  LibreDWG - free implementation of the DWG file format                    */
/*                                                                           */
/*  Copyright (C) 2018-2023 Free Software Foundation, Inc.                   */
/*                                                                           */
/*  This library is free software, licensed under the terms of the GNU       */
/*  General Public License as published by the Free Software Foundation,     */
/*  either version 3 of the License, or (at your option) any later version.  */
/*  You should have received a copy of the GNU General Public License        */
/*  along with this program.  If not, see <http://www.gnu.org/licenses/>.    */
/*****************************************************************************/

/*
 * header_variables_dxf.spec: DXF header variables specification
 * written by Reini Urban
 */

#include "spec.h"

  SECTION (HEADER);

  HEADER_VALUE_TV (ACADVER, 1, dwg_version_codes (dwg->header.version));

  if (minimal) {
    HEADER_VALUE (HANDSEED, RL, 5, _obj->HANDSEED->handleref.value);
    ENDSEC ();
    return 0;
  }

  VERSIONS (R_13b1, R_2013) {
    HEADER_VALUE (ACADMAINTVER, RS, 70, dwg->header.maint_version);
  }
  SINCE (R_2018) {
    HEADER_VALUE (ACADMAINTVER, RL, 90, dwg->header.maint_version);
  }
  SINCE (R_13b1) {
    HEADER_VALUE_TV (DWGCODEPAGE, 3, codepage);
  }
  SINCE (R_2004) {
    // usually only since 2010
    HEADER_VALUE_TU0 (TITLE, 1, dwg->summaryinfo.TITLE);
    HEADER_VALUE_TU0 (SUBJECT, 1, dwg->summaryinfo.SUBJECT);
    HEADER_VALUE_TU0 (AUTHOR, 1, dwg->summaryinfo.AUTHOR);
    HEADER_VALUE_TU0 (KEYWORDS, 1, dwg->summaryinfo.KEYWORDS);
    HEADER_VALUE_TU0 (COMMENTS, 1, dwg->summaryinfo.COMMENTS);
    HEADER_VALUE_TU0 (LASTSAVEDBY, 1, dwg->summaryinfo.LASTSAVEDBY);
    HEADER_VALUE_TU0 (REVISIONNUMBER, 1, dwg->summaryinfo.REVISIONNUMBER);
    for (rcount2 = 0; rcount2 < dwg->summaryinfo.num_props; rcount2++)
      {
        if (!bit_empty_T (dat, (BITCODE_T)dwg->summaryinfo.props[rcount2].tag))
          {
            HEADER_VALUE_TU (CUSTOMPROPERTYTAG, 1, dwg->summaryinfo.props[rcount2].tag);
            HEADER_VALUE_TU (CUSTOMPROPERTY, 1, dwg->summaryinfo.props[rcount2].value);
          }
      }
  }
  SINCE (R_2013) {
    HEADER_BLL (REQUIREDVERSIONS, 160);
  }
  UNTIL (R_9) {
    HEADER_2D (INSBASE);
  } LATER_VERSIONS {
    HEADER_3D (INSBASE);
  }
  UNTIL (R_10) {
    HEADER_2D (EXTMIN);
    HEADER_2D (EXTMAX);
  } LATER_VERSIONS {
    HEADER_3D (EXTMIN);
    HEADER_3D (EXTMAX);
  }
  HEADER_2D (LIMMIN);
  HEADER_2D (LIMMAX);
  PRE (R_9) { // tested r2.6
    HEADER_2D (VIEWCTR);
    HEADER_RD (VIEWSIZE, 40);
    HEADER_RS (SNAPMODE, 70);
    HEADER_2D (SNAPUNIT);
    HEADER_2D (SNAPBASE);
    HEADER_RD (SNAPANG, 50);
    HEADER_RS (SNAPSTYLE, 70);
    HEADER_RS (SNAPISOPAIR, 70);
    HEADER_RS (GRIDMODE, 70);
    HEADER_2D (GRIDUNIT);
  }
  HEADER_RS (ORTHOMODE, 70);
  HEADER_RS (REGENMODE, 70);
  HEADER_RS (FILLMODE, 70);
  HEADER_RS (QTEXTMODE, 70);
  SINCE (R_9c1) {
    HEADER_RS (MIRRTEXT, 70);
  }
  UNTIL (R_14) {
    HEADER_RS (DRAGMODE, 70);
  }
  HEADER_RD (LTSCALE, 40);
  UNTIL (R_14) {
    HEADER_RS (OSMODE, 70);
  }
  HEADER_RS (ATTMODE, 70);
  HEADER_RD (TEXTSIZE, 40);
  HEADER_RD (TRACEWID, 40);

  UNTIL (R_2_10) {
    HEADER_HANDLE_NAME (TEXTSTYLE, 8, STYLE);
    HEADER_HANDLE_NAME (CLAYER, 7, LAYER);
  } LATER_VERSIONS {
    HEADER_HANDLE_NAME (TEXTSTYLE, 7, STYLE);
    HEADER_HANDLE_NAME (CLAYER, 8, LAYER);
  }
  SINCE (R_2_21) { // r2.10 not, r2.6 yes
    HEADER_HANDLE_NAME (CELTYPE, 6, LTYPE);
    HEADER_CMC (CECOLOR, 62);
  }
  SINCE (R_13b1) {
    HEADER_RD (CELTSCALE, 40);
    UNTIL (R_14) {
      HEADER_RS (DELOBJ, 70);
    }
    HEADER_RS (DISPSILH, 70); // this is WIREFRAME
  }
  HEADER_RD (DIMSCALE, 40);
  HEADER_RD (DIMASZ, 40);
  HEADER_RD (DIMEXO, 40);
  HEADER_RD (DIMDLI, 40);
  SINCE (R_2_21) { // r2.10 not, r2.6 yes
    HEADER_RD (DIMRND, 40);
    HEADER_RD (DIMDLE, 40);
  }
  HEADER_RD (DIMEXE, 40);
  HEADER_RD (DIMTP, 40);
  HEADER_RD (DIMTM, 40);
  HEADER_RD (DIMTXT, 40);
  HEADER_RD (DIMCEN, 40);
  HEADER_RD (DIMTSZ, 40);
  HEADER_RS (DIMTOL, 70);
  HEADER_RS (DIMLIM, 70);
  HEADER_RS (DIMTIH, 70);
  HEADER_RS (DIMTOH, 70);
  HEADER_RS (DIMSE1, 70);
  HEADER_RS (DIMSE2, 70);
  HEADER_RS (DIMTAD, 70);
  SINCE (R_2_21) { // r2.10 not, r2.6 yes
    HEADER_RS (DIMZIN, 70);
    HEADER_HANDLE_NAME (DIMBLK, 1, BLOCK_HEADER);
    HEADER_RS (DIMASO, 70);
    HEADER_RS (DIMSHO, 70);
    //HEADER_RS (DIMSAV, 70); // not in DXF
    HEADER_T (DIMPOST, 1);
    HEADER_T (DIMAPOST, 1);
  }
  SINCE (R_2010) {
    HEADER_T0 (DIMALTMZS, 1);
    HEADER_T0 (DIMMZS, 1);
  }
  SINCE (R_2_21) { // r2.10 not, r2.6 yes
    HEADER_RS (DIMALT, 70);
    HEADER_RS (DIMALTD, 70);
    HEADER_RD (DIMALTF, 40);
    HEADER_RD (DIMLFAC, 40);
  }
  SINCE (R_9) {
    HEADER_RS (DIMTOFL, 70);
    HEADER_RD (DIMTVP, 40);
    HEADER_RS (DIMTIX, 70);
    HEADER_RS (DIMSOXD, 70);
    HEADER_RS (DIMSAH, 70);
    HEADER_HANDLE_NAME (DIMBLK1, 1,  BLOCK_HEADER);
    HEADER_HANDLE_NAME (DIMBLK2, 1,  BLOCK_HEADER);
  }
  SINCE (R_11) {
    HEADER_HANDLE_NAME (DIMSTYLE, 2, DIMSTYLE);
    HEADER_CMC (DIMCLRD, 70);
    HEADER_CMC (DIMCLRE, 70);
    HEADER_CMC (DIMCLRT, 70);
    HEADER_RD (DIMTFAC, 40);
    HEADER_RD (DIMGAP, 40);
  }
  SINCE (R_13b1) {
    HEADER_RS (DIMJUST, 70);
    HEADER_RS (DIMSD1, 70);
    HEADER_RS (DIMSD2, 70);
    HEADER_RS (DIMTOLJ, 70);
    HEADER_RS (DIMTZIN, 70);
    HEADER_RS (DIMALTZ, 70);
    HEADER_RS (DIMALTTZ, 70);
    HEADER_RS0 (DIMFIT, 70);
    HEADER_RS (DIMUPT, 70);
    HEADER_RS0 (DIMUNIT, 70);
    HEADER_RS (DIMDEC, 70);
    HEADER_RS (DIMTDEC, 70);
    HEADER_RS (DIMALTU, 70);
    HEADER_RS (DIMALTTD, 70);
    HEADER_HANDLE_NAME (DIMTXSTY, 7, STYLE);
    HEADER_RS (DIMAUNIT, 70);
  }
  SINCE (R_2000) {
    HEADER_RS (DIMADEC, 70);
    HEADER_RD (DIMALTRND, 40);
    HEADER_RS (DIMAZIN, 70);
    HEADER_RS (DIMDSEP, 70);
    HEADER_RS (DIMATFIT, 70);
    HEADER_RS (DIMFRAC, 70);
    HEADER_HANDLE_NAME (DIMLDRBLK, 1, BLOCK_HEADER);
    HEADER_RS (DIMLUNIT, 70);
    //HEADER_RS (DIMLWD, 70); convert from unsigned to signed
    //HEADER_RS (DIMLWE, 70);
    HEADER_BSd (DIMLWD, 70);
    HEADER_BSd (DIMLWE, 70);
    HEADER_RS (DIMTMOVE, 70);
  }
  SINCE (R_2007) {
    HEADER_BD (DIMFXL, 40);
    HEADER_B (DIMFXLON, 70);
    HEADER_BD (DIMJOGANG, 40);
    HEADER_BS (DIMTFILL, 70);
    HEADER_CMC (DIMTFILLCLR, 70);
    HEADER_BS (DIMARCSYM, 70);
    HEADER_HANDLE_NAME (DIMLTYPE, 6, LTYPE);
    HEADER_HANDLE_NAME (DIMLTEX1, 6, LTYPE);
    HEADER_HANDLE_NAME (DIMLTEX2, 6, LTYPE);
  }
  SINCE (R_2010)
    HEADER_RS (DIMTXTDIRECTION, 70);
  HEADER_RS (LUNITS, 70);
  HEADER_RS (LUPREC, 70);
  HEADER_RS (AXISMODE, 70);
  HEADER_2D (AXISUNIT);
  HEADER_RD (SKETCHINC, 40);
  HEADER_RD (FILLETRAD, 40);
  HEADER_RS (AUNITS, 70);
  HEADER_RS (AUPREC, 70);
  HEADER_TV (MENU, 1);
  HEADER_RD (ELEVATION, 40);
  SINCE (R_11b1)
    HEADER_RD (PELEVATION, 40);
  HEADER_RD (THICKNESS, 40);
  PRE (R_9) {
    HEADER_3D (VIEWDIR);
  }
  HEADER_RS (LIMCHECK, 70);
  UNTIL (R_14) {
    HEADER_RS0 (BLIPMODE, 70); //documented but nowhere found
  }
  HEADER_RD (CHAMFERA, 40);
  HEADER_RD (CHAMFERB, 40);
  SINCE (R_13) { //0x10
    HEADER_RD (CHAMFERC, 40);
    HEADER_RD (CHAMFERD, 40);
  }
  PRE (R_2_21) { // r2.10 not, r2.6 yes
    ENDSEC ();
    return 0;
  }
  PRE (R_9)
    HEADER_RS (FASTZOOM, 70);
  HEADER_RS (SKPOLY, 70);

  HEADER_TIMEBLL (TDCREATE, 40);
  SINCE (R_2000)
    HEADER_TIMEBLL (TDUCREATE, 40);
  HEADER_TIMEBLL (TDUPDATE, 40);
  SINCE (R_2000)
    HEADER_TIMEBLL (TDUUPDATE, 40);
  HEADER_TIMEBLL (TDINDWG, 40);
  HEADER_TIMEBLL (TDUSRTIMER, 40);

  HEADER_VALUE (USRTIMER, RS, 70, 1); // 1
  HEADER_RD (ANGBASE, 50);
  HEADER_RS (ANGDIR, 70);
  HEADER_RS (PDMODE, 70);
  HEADER_RD (PDSIZE, 40);
  HEADER_RD (PLINEWID, 40);
  UNTIL (R_14)
    HEADER_RS (COORDS, 70); // 2
  SINCE (R_9) {
    HEADER_RS (SPLFRAME, 70);
    HEADER_RS (SPLINETYPE, 70);
    HEADER_RS (SPLINESEGS, 70);
  }
  VERSIONS (R_9, R_14) {
    HEADER_RS (ATTDIA, 70);   // default 1
    HEADER_RS (ATTREQ, 70);
    HEADER_RS (HANDLING, 70); // default 1
  }
  //HEADER_H (HANDSEED, 5); //default: 20000, before r13: 0xB8BC
  SINCE (R_9) {
    FIELD_DATAHANDLE (HANDSEED, 0, 5);
    HEADER_RS (SURFTAB1, 70); // 6
    HEADER_RS (SURFTAB2, 70); // 6
    HEADER_RS (SURFTYPE, 70); // 6
    HEADER_RS (SURFU, 70); // 6
    HEADER_RS (SURFV, 70); // 6
  }
  SINCE (R_2000) {
    HEADER_HANDLE_NAME (UCSBASE, 2, UCS);
  }
  VERSION (R_10) {
    HEADER_RS (FLATLAND, 70);
  }
  SINCE (R_9) {
    HEADER_HANDLE_NAME (UCSNAME, 2, UCS);
    HEADER_3D (UCSORG);
    PRE (R_11)
    {
      HEADER_9 (UCSXORI);
      VALUE_3BD (dwg->header_vars.UCSXDIR, 10);
      HEADER_9 (UCSYORI);
      VALUE_3BD (dwg->header_vars.UCSYDIR, 10);
    }
    LATER_VERSIONS
    {
      HEADER_3D (UCSXDIR);
      HEADER_3D (UCSYDIR);
    }
  }
  SINCE (R_2000) {
    HEADER_HANDLE_NAME (UCSORTHOREF, 2, UCS);
    HEADER_RS (UCSORTHOVIEW, 70);
    HEADER_3D (UCSORGTOP);
    HEADER_3D (UCSORGBOTTOM);
    HEADER_3D (UCSORGLEFT);
    HEADER_3D (UCSORGRIGHT);
    HEADER_3D (UCSORGFRONT);
    HEADER_3D (UCSORGBACK);
    HEADER_HANDLE_NAME (PUCSBASE, 2, UCS);
  }
  SINCE (R_11b1) {
    HEADER_HANDLE_NAME (PUCSNAME, 2, UCS);
    HEADER_3D (PUCSORG);
    HEADER_3D (PUCSXDIR);
    HEADER_3D (PUCSYDIR);
  }
  SINCE (R_2000) {
    HEADER_HANDLE_NAME (PUCSORTHOREF, 2, UCS);
    HEADER_RS (PUCSORTHOVIEW, 70);
    HEADER_3D (PUCSORGTOP);
    HEADER_3D (PUCSORGBOTTOM);
    HEADER_3D (PUCSORGLEFT);
    HEADER_3D (PUCSORGRIGHT);
    HEADER_3D (PUCSORGFRONT);
    HEADER_3D (PUCSORGBACK);
  }

  HEADER_RSd (USERI1, 70);
  HEADER_RSd (USERI2, 70);
  HEADER_RSd (USERI3, 70);
  HEADER_RSd (USERI4, 70);
  HEADER_RSd (USERI5, 70);
  HEADER_RD (USERR1, 40);
  HEADER_RD (USERR2, 40);
  HEADER_RD (USERR3, 40);
  HEADER_RD (USERR4, 40);
  HEADER_RD (USERR5, 40);

  SINCE (R_9)
    HEADER_RS (WORLDVIEW, 70);
  UNTIL (R_10) {
    ENDSEC ();
    return 0;
  }

  //VERSION (R_13b1) {
  //  HEADER_RS (WIREFRAME, 70); //Undocumented
  //}
  HEADER_RS (SHADEDGE, 70);
  HEADER_RS (SHADEDIF, 70);
  HEADER_RS (TILEMODE, 70);
  HEADER_RS (MAXACTVP, 70);

  SINCE (R_9) // ?
    HEADER_3D (PINSBASE);
  HEADER_RS (PLIMCHECK, 70);
  HEADER_3D (PEXTMIN);
  HEADER_3D (PEXTMAX);
  HEADER_2D (PLIMMIN);
  HEADER_2D (PLIMMAX);

  HEADER_RS (UNITMODE, 70);
  HEADER_RS (VISRETAIN, 70);
  VERSION (R_13b1) // undocumented and unhandled in ODA
    HEADER_RS (DELOBJ, 70);
  HEADER_RS (PLINEGEN, 70);
  HEADER_RS (PSLTSCALE, 70);

  HEADER_RS (TREEDEPTH, 70);
  VERSIONS (R_11b1, R_12) {
    HEADER_VALUE_TV (DWGCODEPAGE, 3, codepage);
  }
  VERSIONS (R_10, R_2000) {
    HEADER_RS0 (PICKSTYLE, 70);
  }
  HEADER_HANDLE_NAME (CMLSTYLE, 2, MLINESTYLE); //default: Standard
  HEADER_RS (CMLJUST, 70);
  HEADER_RD (CMLSCALE, 40); //default: 20
  VERSION (R_13b1) {
    HEADER_9 (SAVEIMAGES);
    VALUE (1, RS, 70);
  }
  SINCE (R_13c3) {
    HEADER_RS (PROXYGRAPHICS, 70);
    HEADER_RS (MEASUREMENT, 70);
  }
  SINCE (R_2000) {
    HEADER_RS (CELWEIGHT, 370);
    HEADER_RS (ENDCAPS, 280);
    HEADER_RS (JOINSTYLE, 280);
    HEADER_B (LWDISPLAY, 290);
    HEADER_RS (INSUNITS, 70);
    HEADER_T (HYPERLINKBASE, 1);
    HEADER_T (STYLESHEET, 1);
    HEADER_B (XEDIT, 290);
    HEADER_RS (CEPSNTYPE, 380);
    if (dwg->header_vars.CEPSNTYPE == 3) {
      HEADER_HANDLE_NAME (CPSNID, 390, LTYPE);
    }
    HEADER_B (PSTYLEMODE, 290);
    HEADER_T (FINGERPRINTGUID, 2);
    HEADER_T (VERSIONGUID, 2);
    HEADER_B (EXTNAMES, 290);
    HEADER_RD (PSVPSCALE, 40);
    HEADER_B (OLESTARTUP, 290);
  }

  SINCE (R_2004) {
    HEADER_RC (SORTENTS, 280);
    HEADER_RC (INDEXCTL, 280);
    HEADER_RC (HIDETEXT, 280);
    SINCE (R_2010) {
      HEADER_RC (XCLIPFRAME, 280);
    } else {
      HEADER_B (XCLIPFRAME, 290);
    }
    PRE (R_2007) {
      HEADER_RC (DIMASSOC, 280);
    }
    HEADER_RC (HALOGAP, 280);
    HEADER_RS (OBSCOLOR, 70);
    HEADER_RC (OBSLTYPE, 280);
    HEADER_RC (INTERSECTIONDISPLAY, 280);
    HEADER_RS (INTERSECTIONCOLOR, 70);
    HEADER_RC (DIMASSOC, 280);
    HEADER_T (PROJECTNAME, 1);
  }

  SINCE (R_2007) {
    HEADER_B (CAMERADISPLAY, 290);
    HEADER_BD (LENSLENGTH, 40);
    HEADER_BD (CAMERAHEIGHT, 40);
    HEADER_BD (STEPSPERSEC, 40);
    HEADER_BD (STEPSIZE, 40);
    HEADER_VALUE (3DDWFPREC, BD, 40, _obj->_3DDWFPREC);
    HEADER_BD (PSOLWIDTH, 40);
    HEADER_BD (PSOLHEIGHT, 40);
    HEADER_BD (LOFTANG1, 40); //no rad2deg, ok
    HEADER_BD (LOFTANG2, 40); //no rad2deg, ok
    HEADER_BD (LOFTMAG1, 40);
    HEADER_BD (LOFTMAG2, 40);
    HEADER_RS (LOFTPARAM, 70);
    HEADER_RC (LOFTNORMALS, 280);
    HEADER_BD (LATITUDE, 40);
    HEADER_BD (LONGITUDE, 40);
    HEADER_BD (NORTHDIRECTION, 40);
    HEADER_BLd (TIMEZONE, 70);
    HEADER_RC (LIGHTGLYPHDISPLAY, 280);
    HEADER_RC (TILEMODELIGHTSYNCH, 280);
    HEADER_H0 (CMATERIAL, 347);
    HEADER_RC (SOLIDHIST, 280);
    HEADER_RC (SHOWHIST, 280);
    HEADER_RC (DWFFRAME, 280);
    HEADER_RC (DGNFRAME, 280);
    HEADER_B (REALWORLDSCALE, 290);
    HEADER_CMC (INTERFERECOLOR, 62);
    HEADER_H0 (INTERFEREOBJVS, 345);
    HEADER_H0 (INTERFEREVPVS, 346);
    HEADER_H0 (DRAGVS, 349);
    HEADER_RC (CSHADOW, 280);
    HEADER_BD (SHADOWPLANELOCATION, 40);
  }

  ENDSEC ();
