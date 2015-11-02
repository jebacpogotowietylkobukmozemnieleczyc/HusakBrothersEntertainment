#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
import matplotlib
matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np


from matplotlib import colors


def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    #rc('text', usetex=True)
    #rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)


    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.pdf')

def hsv2rgb(h, s, v):
    C = v * s
    X = C * (1-abs((h/60) % 2 - 1))
    m = v - C

    if h < 60:
        r = C
        g = X
        b = 0
    elif h < 120:
        r = X
        g = C
        b = 0
    elif h < 180:
        r = 0
        g = C
        b = X
    elif h < 240:
        r = 0
        g = X
        b = C
    elif h < 300:
        r = X
        g = 0
        b = C
    else:
        r = C
        g = 0
        b = X

    return (r+m, g+m, b+m)


def gradient_rgb_bw(v):
    r=v
    g=v
    b=v
    return (r, g, b)


def gradient_rgb_gbr(v):
    if v<1/2:
        r=0
        g=1-v*2
        b=v*2
    else:
        r=(v-0.5)*2
        g=0
        # b=1-2*v
        b=1-(v-0.5)*2
    return (r, g, b)

def gradient_rgb_gbr_full(v):
    if v<1/4:
        r=0
        g=1
        b=v*4
    elif v<1/2:
        r=0
        g=1-(v-0.25)*4
        b=1
    elif v<3/4:
        r=(v-0.5)*4
        g=0
        b=1
    else:
        r= 1
        g=0
        b=1-(v-0.75)*4
    return (r, g, b)

def gradient_rgb_wb_custom(v):
    if v < 1/7:
        r = 1
        g = 1-v*7
        b = 1
    elif v < 2/7:
        r = 1-(v-1/7)*7
        g = 0
        b = 1
    elif v < 3/7:
        r = 0
        g = (v-2/7)*7
        b = 1
    elif v < 4/7:
        r = 0
        g = 1
        b = 1-(v-3/7)*7
    elif v < 5/7:
        r = (v-4/7)*7
        g = 1
        b = 0
    elif v < 6/7:
        r = 1
        g = 1-(v-5/7)*7
        b = 0
    else:
        r = 1-(v-6/7)*7
        g = 0
        b = 0
    return (r, g, b)

def gradient_hsv_bw(v):
    h = 0
    s = 0
    b = v
    return hsv2rgb(h, s, b)


def gradient_hsv_gbr(v):
    h = (v*720)/3 + 120
    s = 1
    b = 1
    return hsv2rgb(h, s, b)

def gradient_hsv_unknown(v):
    h = (1-v)*120
    s = 0.5
    b = 1
    return hsv2rgb(h, s, b)


def gradient_hsv_custom(v):
    h = v*360
    s = v
    b = 1
    return hsv2rgb(h, s, b)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])


