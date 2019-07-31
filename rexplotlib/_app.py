#!/usr/bin/env python3

"""
Script to make matplotlib plots from TRExFitter output.
"""


# fmt: off
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as font_manager
#import os
#if os.environ.get("HELVETICA_MPL"):
#    curdir = os.path.dirname(os.path.abspath(__file__))
#    print(curdir)
#    fontprop_reg = font_manager.FontProperties(fname="{}/Helvetica/Regular.ttf".format(curdir))
#    fontprop_atl = font_manager.FontProperties(fname="{}/Helvetica/Bold_Italic.ttf".format(curdir))
#    matplotlib.rcParams["font.family"] = fontprop_reg.get_name()
#    print(fontprop_reg.get_name())
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams["axes.labelsize"] = 14
matplotlib.rcParams["font.size"] = 12
matplotlib.rcParams["xtick.top"] = True
matplotlib.rcParams["ytick.right"] = True
matplotlib.rcParams["xtick.direction"] = "in"
matplotlib.rcParams["ytick.direction"] = "in"
matplotlib.rcParams["xtick.labelsize"] = 12
matplotlib.rcParams["ytick.labelsize"] = 12
matplotlib.rcParams["xtick.minor.visible"] = True
matplotlib.rcParams["ytick.minor.visible"] = True
matplotlib.rcParams["xtick.major.width"] = 0.8
matplotlib.rcParams["xtick.minor.width"] = 0.8
matplotlib.rcParams["xtick.major.size"] = 7.0
matplotlib.rcParams["xtick.minor.size"] = 4.0
matplotlib.rcParams["xtick.major.pad"] = 1.5
matplotlib.rcParams["xtick.minor.pad"] = 1.4
matplotlib.rcParams["ytick.major.width"] = 0.8
matplotlib.rcParams["ytick.minor.width"] = 0.8
matplotlib.rcParams["ytick.major.size"] = 7.0
matplotlib.rcParams["ytick.minor.size"] = 4.0
matplotlib.rcParams["ytick.major.pad"] = 1.5
matplotlib.rcParams["ytick.minor.pad"] = 1.4
matplotlib.rcParams["legend.frameon"] = False
matplotlib.rcParams["legend.numpoints"] = 1
matplotlib.rcParams["legend.fontsize"] = 11
matplotlib.rcParams["legend.handlelength"] = 1.5
matplotlib.rcParams["axes.formatter.limits"] = [-4, 4]
matplotlib.rcParams["axes.formatter.use_mathtext"] = True
# fmt: on

import argparse
from rexplotlib.pulls import run_pulls
from rexplotlib.stack import run_stacks


def get_args():
    # fmt: off
    parser = argparse.ArgumentParser()
    subcommands = parser.add_subparsers(dest="topcommand")

    stacks = subcommands.add_parser("stacks", help="Generate stack plots")
    stacks.add_argument("workspace", type=str, help="TRExFitter workspace")
    stacks.add_argument("config", type=str, help="wt-stat configuration file")
    stacks.add_argument("-o", "--out-dir", type=str, help="output directory for plots")
    stacks.add_argument("--lumi", type=str, default="139", help="Integrated lumi. for text")
    stacks.add_argument("--do-postfit", action="store_true", help="produce post fit plots as well")
    stacks.add_argument("--skip-regions", type=str, default=None, help="skip regions based on regex")
    stacks.add_argument("--shrink", action="store_true", help="shrink output PDFs via ghostscript")
    stacks.set_defaults(func=run_stacks)

    pulls = subcommands.add_parser("pulls", help="pull plots")
    pulls.add_argument("workspace", type=str, help="TRExFitter workspace")
    pulls.add_argument("config", type=str, help="TRExFitter config")
    pulls.add_argument("-o", "--out-dir", type=str, help="output directory")
    pulls.add_argument("--no-text", action="store_true", help="don't print values on plots")
    pulls.add_argument("--shrink", action="store_true", help="shrink output PDFs via ghostscript")
    pulls.set_defaults(func=run_pulls)
    # fmt: on

    return (parser.parse_args(), parser)


def cli():
    args, parser = get_args()
    if args.topcommand is None:
        parser.print_help()
        return 0
    args.func(args)
    return 0
