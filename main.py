# import numpy as np
# import math
# import matplotlib.pyplot as plt
#
# data = np.loadtxt('./data/pion_gamma15_p0_t0_1.txt')
# cfg = int(len(data) / 64)
# a0 = 0.197 / 0.12
# m = np.zeros([cfg, 63])
# M = np.zeros(63)
# Err = np.zeros(63)
# for i in range(cfg):
#     for j in range(1, 63):
#         m[i, j] = a0 * (np.log(data[i][7]/ data[i + 2][7]))
#         print("i={}, numerator= {},  denominator={}".format(i, data[i][7], data[i+2][7]))
#
# for i in range(63):
#     M[i] = np.mean(m[:, i])
#     Err[i] = np.std(m[:, i])
#
# plt.figure(dpi=150)
# plt.xlim(0, 28)
# x = np.linspace(2, 27, 26)
# # plt.errorbar(x, M[i])
# plt.plot(np.linspace(2, 27, 26), 0.3)
# plt.show()

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



