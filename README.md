﻿# Sublime Rainmeter

<a href="https://thatsich.github.io/sublime-rainmeter/"><img src="https://cloud.githubusercontent.com/assets/2210496/22306580/06ebd838-e340-11e6-8c23-c1b85435fbe4.png" align="left" hspace="10" vspace="6" /></a>

This [Sublime Text 3](https://www.sublimetext.com/3) plugin written in [Python 3](https://www.python.org/) provides an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) like environment for creating and editing [Rainmeter][rainmeter homepage] skins. It elevates the pain of context switching from Editor to Desktop, back and forth by integrating features like build tools to streamline the skinning process.

![Image of Sublime Text in Action](https://cloud.githubusercontent.com/assets/2210496/21537848/947dc284-cd96-11e6-8b04-2e2a95ff687e.png)

## Project Status

[![Maintenance](https://img.shields.io/maintenance/yes/2021.svg)](https://github.com/thatsIch/sublime-rainmeter)
[<img src="https://packagecontrol.herokuapp.com/downloads/Rainmeter.svg">](https://packagecontrol.io/packages/Rainmeter)
[![Build status](https://ci.appveyor.com/api/projects/status/2nbuwdg8qktcuy6q/branch/master?svg=true)](https://ci.appveyor.com/project/thatsIch/sublime-rainmeter/branch/master)

[![Coverage Status](https://coveralls.io/repos/github/thatsIch/sublime-rainmeter/badge.svg?branch=HEAD)](https://coveralls.io/github/thatsIch/sublime-rainmeter?branch=HEAD)
[![Code Health](https://landscape.io/github/thatsIch/sublime-rainmeter/master/landscape.svg?style=flat)](https://landscape.io/github/thatsIch/sublime-rainmeter/master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/thatsIch/sublime-rainmeter/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/thatsIch/sublime-rainmeter/?branch=master)
[![codecov](https://codecov.io/gh/thatsIch/sublime-rainmeter/branch/master/graph/badge.svg)](https://codecov.io/gh/thatsIch/sublime-rainmeter)
[![Code Climate](https://codeclimate.com/github/thatsIch/sublime-rainmeter/badges/gpa.svg)](https://lima.codeclimate.com/github/thatsIch/sublime-rainmeter)
[![Test Coverage](https://codeclimate.com/github/thatsIch/sublime-rainmeter/badges/coverage.svg)](https://lima.codeclimate.com/github/thatsIch/sublime-rainmeter/coverage?sort=covered_percent&sort_direction=asc)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a35810c0df5a4132a4c50d96d596114d)](https://www.codacy.com/app/thatsIch/sublime-rainmeter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thatsIch/sublime-rainmeter&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/a35810c0df5a4132a4c50d96d596114d)](https://www.codacy.com/app/thatsIch/sublime-rainmeter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=thatsIch/sublime-rainmeter&amp;utm_campaign=Badge_Coverage)

## Resources

* [Installation](https://github.com/thatsIch/sublime-rainmeter/wiki/Installation)
* [Configuration](https://github.com/thatsIch/sublime-rainmeter/wiki/Configuration)
* [Bindings](https://github.com/thatsIch/sublime-rainmeter/wiki/Bindings)
* [Release Notes](https://github.com/thatsIch/sublime-rainmeter/releases)
* [Contributions](https://github.com/thatsIch/sublime-rainmeter/wiki/Contributions)


## Features

| Feature | Description | Details |
|---------|-------------|---------|
| Syntax Highlighting | highlight keywords and errors | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Syntax-Highlighting) |
| Theme Switcher | quickly switch Rainmeter themes |  [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Theme-Switcher) |
| Code Completion | suggest all possible keywords | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Code-Completion) |
| Snippets | preconstructed code blocks via keywords | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Snippets) |
| Smart Code Completion | context-sensitive auto suggestions | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Smart-Code-Completion) |
| Goto Symbol | quick goto section | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Goto-Symbol) |
| Auto Indention | enables code folding | |
| Code Folding | hide sections | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Code-Folding) |
| Color Picker | pick and replace colors | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Color-Picker) |
| New Skin | quick new skin scaffolding | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/New-Skin) |
| Refresh Skin/Rainmeter | update rainmeter without leaving ST3 | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Refresh-Skin-Rainmeter#configuration) |
| Open Skins Folder | quick access to Rainmeter skins folder | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Open-Skins-Folder) |
| Open Paths | open relative skin files | [details](https://github.com/thatsIch/sublime-rainmeter/wiki/Open-Paths-in-Rainmeter-Files) |

## Installation

### With Package Control

* open the command palette (default <kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>p</kbd>)
* run `Package Control: Install Package` command
* search for `Rainmeter` and hit enter

The package will now be installed and kept up-
to-date automatically.

### Alternatives

* using [git](https://github.com/thatsIch/sublime-rainmeter/wiki/Installation#using-git)
* using [.sublime-package](https://github.com/thatsIch/sublime-rainmeter/wiki/Installation#manual-package-installation)
* using [zip](https://github.com/thatsIch/sublime-rainmeter/wiki/Installation#manual-zip-installation)

## Acknowledgements

* [Sublime Rainmeter plugin by merlinthered](https://github.com/merlinthered/sublime-rainmeter), base of this fork
* [Color Highlighter plugin by Monnoroch](https://github.com/Monnoroch/ColorHighlighter), using the color picker
* [RainLexer by poiru](https://github.com/poiru/rainlexer), which is another awesome tool for developing
  Rainmeter skins, for the inspiration and one of the color schemes.
* [Monokai Color Scheme by Wimer Hazenberg](http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/), for providing such an amazing
  composition of colors.
* [Kaelri](https://github.com/Kaelri) for contributing the "Nexus" color
  scheme.
* [The Rainmeter Community][rainmeter homepage], for being awesome and testing this package.

[rainmeter homepage]: https://www.rainmeter.net/ "Rainmeter"
