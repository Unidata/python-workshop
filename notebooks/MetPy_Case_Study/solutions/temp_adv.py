# Temperature Advection
tmpc_adv_850 = mpcalc.advection(tmpk_850, [uwnd_850, vwnd_850],
                                (dx, dy), dim_order='yx').to('degC/s')
