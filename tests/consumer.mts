import { createElement, createRef, type ComponentRef } from 'react';
import { SearchIcon } from '@hugocxl/icons/react';
import { TerminalIcon } from '@hugocxl/icons/react/terminal';

createElement(SearchIcon, { size: 24, ref: createRef<SVGSVGElement>(), 'aria-label': 'Search' });
createElement(TerminalIcon, { color: 'red', onClick: event => event.currentTarget.focus() });
// @ts-expect-error size must be numeric
createElement(SearchIcon, { size: 'large' });

import { SearchIcon as searchSvg } from '@hugocxl/icons/js';
import { SearchIcon as rootSvg } from '@hugocxl/icons';
const svg: string = searchSvg;
const same: string = rootSvg;

import { SearchIcon as SolidSearchIcon } from '@hugocxl/icons/react/solid';
import { SearchIcon as StrokeSearchIcon } from '@hugocxl/icons/react/stroke/search';
import { SearchIcon as DuotoneSearchIcon } from '@hugocxl/icons/react/duotone/search';
import { SearchIcon as solidSvg } from '@hugocxl/icons/js/solid';
createElement(SolidSearchIcon, { ref: createRef<SVGSVGElement>(), 'aria-label': 'Search' });
createElement(StrokeSearchIcon, { size: 16 });
createElement(DuotoneSearchIcon, { size: 32 });
const styledSvg: string = solidSvg;
// @ts-expect-error retained brands are not exported as invented stroke variants
import { GithubIcon } from '@hugocxl/icons/react/stroke';

import { defaultColor } from '@hugocxl/icons/colors';
createElement(TerminalIcon, { color: defaultColor('terminal') });
