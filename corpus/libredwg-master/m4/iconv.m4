# iconv.m4
dnl Copyright (C) 2000-2002 Free Software Foundation, Inc.
dnl This file is free software, distributed under the terms of the GNU
dnl General Public License.  As a special exception to the GNU General
dnl Public License, this file may be distributed as part of a program
dnl that contains a configuration script generated by Autoconf, under
dnl the same distribution terms as the rest of that program.

dnl From Bruno Haible.
dnl with modifications to support building with in-tree libiconv
dnl and modernizing AC_TRY_LINK

AC_DEFUN([AM_ICONV_LINKFLAGS_BODY],
[
  dnl Prerequisites of AC_LIB_LINKFLAGS_BODY.
  AC_REQUIRE([AC_LIB_PREPARE_PREFIX])
  AC_REQUIRE([AC_LIB_RPATH])

  dnl Search for libiconv and define LIBICONV, LTLIBICONV and INCICONV
  dnl accordingly.
  AC_LIB_LINKFLAGS_BODY([iconv])
])

AC_DEFUN([AM_ICONV_LINK],
[
  dnl Some systems have iconv in libc, some have it in libiconv (OSF/1 and
  dnl those with the standalone portable GNU libiconv installed).

  dnl Search for libiconv and define LIBICONV, LTLIBICONV and INCICONV
  dnl accordingly.
  AC_REQUIRE([AM_ICONV_LINKFLAGS_BODY])

  AC_CACHE_CHECK(for iconv, am_cv_func_iconv, [
    am_cv_func_iconv="no, consider installing GNU libiconv"
    am_cv_lib_iconv=no
    if test "$host_alias" != powerpc64-linux-gnu -o "$cross_compiling" != yes; then
     dnl Add $INCICONV to CPPFLAGS before performing the first check,
     dnl because if the user has installed libiconv and not disabled its use
     dnl via --without-libiconv-prefix, he wants to use it. This first
     dnl AC_TRY_LINK will then fail, the second AC_TRY_LINK will succeed.
     am_save_CPPFLAGS="$CPPFLAGS"
     CPPFLAGS="$CPPFLAGS $INCICONV"
     AC_LINK_IFELSE(
      [AC_LANG_PROGRAM([[#include <stdlib.h>
#include <iconv.h>]],
        [[iconv_t cd = iconv_open("UTF-8","ISO-8859-1");
          iconv(cd,NULL,NULL,NULL,NULL);
          iconv_close(cd);]])],
      am_cv_func_iconv=yes)
     CPPFLAGS="$am_save_CPPFLAGS"
     if test "$am_cv_func_iconv" != yes && test -d ../libiconv; then
      for _libs in .libs _libs; do
        am_save_CPPFLAGS="$CPPFLAGS"
        am_save_LIBS="$LIBS"
        CPPFLAGS="$CPPFLAGS -I../libiconv/include"
        LIBS="$LIBS ../libiconv/lib/$_libs/libiconv.a"
        AC_LINK_IFELSE(
          [AC_LANG_PROGRAM([[#include <stdlib.h>
#include <iconv.h>]],
            [[iconv_t cd = iconv_open("UTF-8","ISO-8859-1");
              iconv(cd,NULL,NULL,NULL,NULL);
              iconv_close(cd);]])],
          INCICONV="-I../libiconv/include"
          LIBICONV='${top_builddir}'/../libiconv/lib/$_libs/libiconv.a
          LTLIBICONV='${top_builddir}'/../libiconv/lib/libiconv.la
          am_cv_lib_iconv=yes
          am_cv_func_iconv=yes)
        CPPFLAGS="$am_save_CPPFLAGS"
        LIBS="$am_save_LIBS"
        if test "$am_cv_func_iconv" = "yes"; then
          break
        fi
      done
     fi
    fi

    if test "$am_cv_func_iconv" != yes; then
     if test -a "$host_alias" != powerpc64-linux-gnu -o "$cross_compiling" != yes; then
      am_save_CPPFLAGS="$CPPFLAGS"
      am_save_LIBS="$LIBS"
      CPPFLAGS="$CPPFLAGS $INCICONV"
      LIBS="$LIBS $LIBICONV"
      AC_LINK_IFELSE(
        [AC_LANG_PROGRAM([[#include <stdlib.h>
#include <iconv.h>]],
          [[iconv_t cd = iconv_open("UTF-8","ISO-8859-1");
            iconv(cd,NULL,NULL,NULL,NULL);
            iconv_close(cd);]])],
        am_cv_func_iconv=yes)
      CPPFLAGS="$am_save_CPPFLAGS"
      LIBS="$am_save_LIBS"
     fi
    fi
  ])
  if test "$am_cv_func_iconv" = yes; then
    AC_DEFINE(HAVE_ICONV, 1, [Define if you have the iconv() function.])
  fi
  if test "$am_cv_lib_iconv" = yes; then
    AC_LIB_APPENDTOVAR([CPPFLAGS], [$INCICONV])
    AC_MSG_CHECKING([how to link with libiconv])
    AC_MSG_RESULT([$LIBICONV])
  else
    LIBICONV=
    LTLIBICONV=
  fi
  AC_SUBST(LIBICONV)
  AC_SUBST(LTLIBICONV)
])

AC_DEFUN([AM_ICONV],
[
  AM_ICONV_LINK
  if test "$am_cv_func_iconv" = yes; then
    AC_MSG_CHECKING([for iconv declaration])
    AC_CACHE_VAL(am_cv_proto_iconv, [
      AC_TRY_COMPILE([
#include <stdlib.h>
#include <iconv.h>
extern
#ifdef __cplusplus
"C"
#endif
#if defined(__STDC__) || defined(__cplusplus)
size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
#else
size_t iconv();
#endif
], [], am_cv_proto_iconv_arg1="", am_cv_proto_iconv_arg1="const")
      am_cv_proto_iconv="extern size_t iconv (iconv_t cd, $am_cv_proto_iconv_arg1 char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);"])
    am_cv_proto_iconv=`echo "[$]am_cv_proto_iconv" | tr -s ' ' | sed -e 's/( /(/'`
    AC_MSG_RESULT([$]{ac_t:-
         }[$]am_cv_proto_iconv)
    AC_DEFINE_UNQUOTED(ICONV_CONST, $am_cv_proto_iconv_arg1,
      [Define as const if the declaration of iconv() needs const.])
  fi
])
