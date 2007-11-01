/*
# AUTOGENERATED DO NOT EDIT

# If you edit this file, delete the AUTOGENERATED line to prevent re-generation
# BUILD api_versions [0x001]
*/

%module packed_depth_stencil

#define __version__ "$Revision: 1.1.2.1 $"
#define __date__ "$Date: 2004/11/15 07:38:07 $"
#define __api_version__ API_VERSION
#define __author__ "PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>"
#define __doc__ ""

%{
/**
 *
 * GL.NV.packed_depth_stencil Module for PyOpenGL
 * 
 * Authors: PyOpenGL Developers <pyopengl-devel@lists.sourceforge.net>
 * 
***/
%}

%include util.inc
%include gl_exception_handler.inc

%{
#ifdef CGL_PLATFORM
# include <OpenGL/glext.h>
#else
# include <GL/glext.h>
#endif

#if !EXT_DEFINES_PROTO || !defined(GL_NV_packed_depth_stencil)

#endif
%}

/* FUNCTION DECLARATIONS */


/* CONSTANT DECLARATIONS */
#define            GL_DEPTH_STENCIL_NV 0x84F9
#define        GL_UNSIGNED_INT_24_8_NV 0x84FA


%{
static char *proc_names[] =
{
#if !EXT_DEFINES_PROTO || !defined(GL_NV_packed_depth_stencil)

#endif
	NULL
};

#define glInitPackedDepthStencilNV() InitExtension("GL_NV_packed_depth_stencil", proc_names)
%}

int glInitPackedDepthStencilNV();
DOC(glInitPackedDepthStencilNV, "glInitPackedDepthStencilNV() -> bool")

%{
PyObject *__info()
{
	if (glInitPackedDepthStencilNV())
	{
		PyObject *info = PyList_New(0);
		return info;
	}
	
	Py_INCREF(Py_None);
	return Py_None;
}
%}

PyObject *__info();

