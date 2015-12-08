/* //////////////////////////////////////////////////////////////////////////////////////
 * includes
 */ 
#include "tbox/tbox.h"

/* //////////////////////////////////////////////////////////////////////////////////////
 * main
 */ 
tb_int_t main(tb_int_t argc, tb_char_t** argv)
{
    // init tbox
    if (!tb_init(tb_null, tb_null, tb_null, 0)) return -1;

    // trace
    tb_trace_i("hello tbox!");

    // exit tbox
    tb_exit();
    return 0;
}