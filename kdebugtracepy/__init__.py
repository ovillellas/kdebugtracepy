"""kdebugtracepy

Some basic bindings for kdebug_trace functionality (for use with
Apple Instruments, for example).
"""

from cffi import FFI as _FFI
import warnings


_ffi = _FFI()


# C interfaces for the functions to use... from
# https://opensource.apple.com/source/xnu/xnu-4570.41.2/bsd/sys/kdebug_signpost.h.auto.html

_ffi.cdef("""
int kdebug_signpost(uint32_t code, uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4);
int kdebug_signpost_start(uint32_t code, uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4);
int kdebug_signpost_end(uint32_t code,  uintptr_t arg1, uintptr_t arg2, uintptr_t arg3, uintptr_t arg4);
""")

# These should be already present in the current process
_lib = _ffi.dlopen(None)

def _not_found_placeholder_function(*args):
    pass

def _get_fn_for(symbol_name):
    try:
        return getattr(_lib, symbol_name)
    except AttributeError:
        warnings.warn('Symbol {0} not found'.format(symbol_name), RuntimeWarning)
        return _not_found_placeholder_function


# The exported symbols. Note that a placeholder function is used if the corresponding
# symbol is not present in the process. In that case a warn should be issued.
kdebug_signpost = _get_fn_for('kdebug_signpost')
kdebug_signpost_start = _get_fn_for('kdebug_signpost_start')
kdebug_signpost_end = _get_fn_for('kdebug_signpost_end')
