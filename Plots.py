import numpy as np
import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import os
import matplotlib.animation as animation
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import MaxNLocator
import glob

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern"]})

import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)

SMALL_SIZE = 16
MEDIUM_SIZE = 18
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=MEDIUM_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


class PlotFlow:
    def __init__(self, X, Y, t) -> None:

        self.Nx = int(np.size(X))
        self.Ny = int(np.size(Y))
        self.Nt = int(np.size(t))

        self.X = X
        self.Y = Y
        self.t = t

        # Prepare the space-time grid for 1D plots
        self.X_1D_grid, self.t_grid = np.meshgrid(X, t)
        self.X_1D_grid = self.X_1D_grid.T
        self.t_grid = self.t_grid.T

        # Prepare the space grid for 2D plots
        self.X_2D_grid, self.Y_2D_grid = np.meshgrid(X, Y)
        self.X_2D_grid = np.transpose(self.X_2D_grid)
        self.Y_2D_grid = np.transpose(self.Y_2D_grid)

    def plot1D(self, Q, name, immpath):
        os.makedirs(immpath, exist_ok=True)

        # Plot the snapshot matrix for conserved variables for original model
        fig = plt.figure(figsize=(5, 5))
        ax1 = fig.add_subplot(111)
        im1 = ax1.pcolormesh(self.X_1D_grid, self.t_grid, Q, cmap='YlOrRd')
        ax1.axis('off')
        ax1.set_title(r"$q(x, t)$")
        divider = make_axes_locatable(ax1)
        cax = divider.append_axes('right', size='10%', pad=0.08)
        fig.colorbar(im1, cax=cax, orientation='vertical')

        fig.supylabel(r"time $t$")
        fig.supxlabel(r"space $x$")

        fig.savefig(immpath + name, dpi=300, transparent=True)

    def plot1D_FOM_converg(self, J, immpath):

        os.makedirs(immpath, exist_ok=True)

        fig1 = plt.figure(figsize=(8, 8))
        ax1 = fig1.add_subplot(111, label="1")
        ax1.semilogy(np.arange(len(J)), J, color="C0", label=r"$\mathcal{J}$")
        ax1.set_xlabel(r"$n_{\mathrm{iter}}$", color="C0")
        ax1.set_ylabel(r"$J$", color="C0")
        ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax1.tick_params(axis='x', colors="C0")
        ax1.tick_params(axis='y', colors="C0")
        fig1.savefig(immpath + "J", dpi=300, transparent=True)

    def plot1D_ROM_converg(self, J, immpath):

        os.makedirs(immpath, exist_ok=True)

        fig1 = plt.figure(figsize=(8, 8))
        ax1 = fig1.add_subplot(111, label="1")
        ax1.semilogy(np.arange(len(J)), J, color="C0", label=r"$\mathcal{J}$")
        ax1.set_xlabel(r"$n_{\mathrm{iter}}$", color="C0")
        ax1.set_ylabel(r"$J$", color="C0")
        ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax1.tick_params(axis='x', colors="C0")
        ax1.tick_params(axis='y', colors="C0")
        ax1.legend()
        fig1.savefig(immpath + "J", dpi=300, transparent=True)
