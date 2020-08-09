# -*- coding: utf-8 -*-
# 上面的代码不是简简单单的注释，它能防止解释器以ASCII编码打开这个文件，导致编码错误

import Plot2pt
import itertools
import constant

if __name__ == "__main__":
    plot_object = Plot2pt.Plot2pt("data/pion_gamma15_p0_t0_1.txt")
    for configuration, time in itertools.product(range(constant.NUMBER_OF_CONFIGURATION),
                                                 range(constant.NUMBER_OF_TIME_SEPARATION)):
        plot_object.calculate_effective_mass(configuration, time)
    plot_object.calculate_mean_of_effective_mass()
    plot_object.calculate_error_of_effective_mass()
    plot_object.plot_result()



