# -*- coding: utf-8 -*-
# 上面的代码不是简简单单的注释，它能防止解释器以ASCII编码打开这个文件，导致编码错误

import sys
import os
import matplotlib.pyplot as plt
import numpy  # 我觉得numpy五个字母不长，没必要as np

import constant  # 常量单独放一个文件里面定义，不要每次用常量都复制粘贴一串数字


class Plot2pt:
    # 定义变量要避免单字母，变量名称要有实际含义
    # 变量的命名用下划线命名
    effective_mass = numpy.zeros([constant.NUMBER_OF_CONFIGURATION, constant.NUMBER_OF_TIME_SEPARATION])
    mean_of_effective_mass = numpy.zeros(constant.NUMBER_OF_TIME_SEPARATION)
    error_of_effective_mass = numpy.zeros(constant.NUMBER_OF_TIME_SEPARATION)

    def __init__(self, data_dir):
        self.data = numpy.loadtxt(data_dir)

    def calculate_effective_mass(self, configuration_number, time_separation):
        try:
            if time_separation < constant.NUMBER_OF_TIME_SEPARATION - 1:
                target_line = configuration_number * constant.NUMBER_OF_TIME_SEPARATION + time_separation
                # 每一行代码的长度不能超过121，超过应换行
                self.effective_mass[configuration_number, time_separation] = constant.A0 * numpy.log(
                    self.data[target_line][7] / self.data[target_line + 1][7])

        except ZeroDivisionError:
            print("Error: Division by Zero, Abort!")
            sys.exit(1)

    def calculate_mean_of_effective_mass(self):
        for time in range(constant.NUMBER_OF_TIME_SEPARATION):
            self.mean_of_effective_mass[time] = numpy.mean(self.effective_mass[:, time])

    def calculate_error_of_effective_mass(self):
        for time in range(constant.NUMBER_OF_TIME_SEPARATION):
            self.error_of_effective_mass[time] = numpy.std(self.effective_mass[:, time])

    def plot_result(self):
        plt.figure(dpi=150)
        plt.xlim(0, constant.NUMBER_OF_TIME_SEPARATION)
        x_data = numpy.arange(constant.NUMBER_OF_TIME_SEPARATION)  # 不要用linspace了，这是间断的整数，而且step是1
        y_data = self.mean_of_effective_mass
        y_error = self.error_of_effective_mass
        plt.errorbar(x_data, y_data, yerr=y_error)
        plt.ylabel("effective mass")
        plt.xlabel("time separation in Lattice unit")
        if not os.path.exists("figs"):
            os.mkdir("figs")
        plt.savefig("figs/output.png")
        plt.show()
